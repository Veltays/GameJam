import pygame

from JeuCrackheadSIM.CrackConst import *

from ConstanteMenu import *


class FonctionCrack:
    def __init__(self):
        # Initialisation de pygame
        pygame.init()
        # --------------------------------------------------------------------------------------------------------------
        # -----------------------------Chargement des images -----------------------------------------------------------
        # ----------------------------Relatif au jeu cracksim------------------
        self.logo = pygame.image.load(Const.LOGO)
        self.crackheadFOND = pygame.image.load(CrackConst.JEUCRACKED)
        # ---------------------------Reste du bordel--------------------------------------------------------------------
        # ---------------------------Dimensions de la fenêtre----------------
        self.screen = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT))
        # ---------------------------Nom de la fenetre----------------------
        pygame.display.set_caption("CrackHead Tycoon")
        # ---------------------------Icone de la fenetre----------------------
        pygame.display.set_icon(self.logo)
        self.positionSourisCrack = None
        # --------------------------Image du Jeu ----------------------------
        self.CulDuV = pygame.image.load(CrackConst.LECULDUV)

        # ------------------------Varible-------------------------------------------------------------------------------
        self.angle = 0
        self.CulDuV_Rect = self.CulDuV.get_rect(center=(Const.WIDTH // 2, Const.HEIGHT // 2))
        self.rotation_point = (Const.WIDTH // 2, Const.HEIGHT // 2)

    def dessinCrack(self, ConstFORME):
        pygame.draw.polygon(self.screen, Const.WHITE, ConstFORME)
    def recupererEvenement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    self.positionSourisCrack = event.pos
                    return event.button
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return event.key


    def afficherImage(self, x, y, image):
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.screen.blit(image, rect)

    def PresentationCul(self):
        rotated_image = pygame.transform.rotate(self.CulDuV, self.angle)
        new_rect = rotated_image.get_rect(center=self.CulDuV_Rect.center)
        self.screen.blit(rotated_image, new_rect.topleft)
        self.angle += 3
        if self.angle >= 360:
            self.angle = 0
        pygame.display.flip()

    def actualiserFenetreGraphique(self):
        pygame.display.flip()

    def effacerImageInterne(self, image):
        self.screen.blit(image, (0, 0, 1016, 780), (0, 0, Const.WIDTH, Const.HEIGHT))


