import pygame as pyg
from Constante import *


class Init_Menu():
    def __init__(self):
        pyg.init()
        pyg.display.set_caption("Untilted Game")
        self.ecran = pyg.display.set_mode((100, 800))
        self.AfficherAccueil()




        self.actualiserFenetreGraphique()



    def AfficherAccueil(self):
        self.afficherImage(0, 0, Const.ECRANACCUEIL)
        self.actualiserFenetreGraphique()
    def afficherImage(self, x, y, image):
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.ecran.blit(image, rect)
        print('3')

    def actualiserFenetreGraphique(self):
        pyg.display.update()

