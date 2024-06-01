import pygame
from Constante import *
from CreateButton import *


class PyFonct:
    def __init__(self):

        self.accueil = pygame.image.load(Const.ECRANACCUEIL)
        self.logo = pygame.image.load(Const.LOGO)
        self.triangle_selection = pygame.image.load(Const.TRIANGLE_SELECTION)

        # Initialisation de pygame
        pygame.init()
        # Dimensions de la fenêtre
        self.screen = pygame.display.set_mode((Const.WIDTH, Const.HEIGHT))
        pygame.display.set_caption("Menu")

        pygame.display.set_icon(self.logo)
        self.screen.fill(Const.WHITE)





    def MouseCOORD(self):
        return pygame.mouse.get_pos()




    def RecupererEvenement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return event.pos


    def AjouterFondMenu(self):
        self.screen.blit(self.accueil, (0, 0))

    def afficherImage(self, x, y, image):
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.screen.blit(image, rect)


    def actualiserFenetreGraphique(self):
        pygame.display.update()

    def effacerImageInterne(self):
        self.screen.blit(self.accueil, (0, 0, 1016, 780), (0, 0, Const.WIDTH, Const.HEIGHT))