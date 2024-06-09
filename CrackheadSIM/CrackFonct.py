import pygame

from ConstanteMenu import *




class FonctionCrack:
    def __init__(self):
        # Initialisation de pygame
        pygame.init()
        # --------------------------------------------------------------------------------------------------------------
        # -----------------------------Chargement des images -----------------------------------------------------------
        # ----------------------------Relatif au jeu cracksim------------------
        self.logo = pygame.image.load(Const.LOGO)
        self.crackheadFOND = pygame.image.load(Const.JEUCRACKED)
        # ---------------------------Reste du bordel--------------------------------------------------------------------
        # ---------------------------Dimensions de la fenêtre----------------
        self.screen = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT))
        # ---------------------------Nom de la fenetre----------------------
        pygame.display.set_caption("CrackHead Tycoon")
        # ---------------------------Icone de la fenetre----------------------
        pygame.display.set_icon(self.logo)
        self.positionSourisCrack = None

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

    def actualiserFenetreGraphique(self):
        pygame.display.flip()

    def effacerImageInterne(self, image):
        self.screen.blit(image, (0, 0, 1016, 780), (0, 0, Const.WIDTH, Const.HEIGHT))


