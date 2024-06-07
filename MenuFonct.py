import pygame

from Constante import *


class MenuFonct:
    def __init__(self):
        # Initialisation de pygame
        pygame.init()
        # --------------------------------------------------------------------------------------------------------------
        # -----------------------------Chargement des images -----------------------------------------------------------
        # -----------------------------Relatif au Menu et la fenetre ---------
        self.logo = pygame.image.load(Const.LOGO)
        self.accueil = pygame.image.load(Const.ECRANACCUEIL)
        self.triangle_selection = pygame.image.load(Const.TRIANGLE_SELECTION)
        self.choixniveau = pygame.image.load(Const.CHOIXNIV)

        self.BackChoixHover = pygame.image.load(Const.HOVERBACKCHOIX)
        self.choixHover = pygame.image.load(Const.HOVERCHOIX)
        self.accueilHover = pygame.image.load(Const.HOVERACCUEIL)
        self.musiqueHover = pygame.image.load(Const.HOVERMUSIQE)
        # ---------------------------Reste du bordel--------------------------------------------------------------------
        # ---------------------------Dimensions de la fenêtre----------------
        self.screen = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT))
        # ---------------------------Nom de la fenetre----------------------
        pygame.display.set_caption("Menu")
        # ---------------------------Icone de la fenetre----------------------
        pygame.display.set_icon(self.logo)

    def mouseCOORD(self):
        return pygame.mouse.get_pos()

    def recupererCoordonnerClick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    return event.pos

    def afficherImage(self, x, y, image):
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.screen.blit(image, rect)

    def dessin(self, ConstFORME):
        pygame.draw.polygon(self.screen, Const.WHITE, ConstFORME)

    def rangePolygone(self, polygon, point):
        x, y = point
        num_points = len(polygon)
        j = num_points - 1
        inside = False

        for i in range(num_points):
            xi, yi = polygon[i]
            xj, yj = polygon[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
                inside = not inside
            j = i

        return inside

    def afficherAccueil(self):
        self.afficherImage(0, 0, Const.ECRANACCUEIL)
        self.actualiserFenetreGraphique()

    def actualiserFenetreGraphique(self):
        pygame.display.flip()

    def effacerImageInterne(self, image):
        self.screen.blit(image, (0, 0, 1016, 780), (0, 0, Const.WIDTH, Const.HEIGHT))
