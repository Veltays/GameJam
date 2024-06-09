import pygame
from ChoixNiveau.choixNiv import *
from MenuFonct import *
from ConstanteMenu import *
import time

class Menu:
    def __init__(self):
        self.Const = Const()
        self.MenuFonct = MenuFonct()
        self.choixniv = ChoixLVL()
        self.BTNMUSIQUE = 'ON'

    def Running(self):

        while True:
            self.ClickMenu()
            self.Hover()
            self.MenuFonct.actualiserFenetreGraphique()

    def Hover(self):
        point = self.MenuFonct.mouseCOORD()
        if point is not None:
            if self.MenuFonct.rangePolygone(Const.BTNPLAY_ACCUEIL, point):
                self.MenuFonct.afficherImage(231, 229, self.MenuFonct.triangle_selection)
                self.MenuFonct.afficherImage(340, 213, self.MenuFonct.accueilHover)

            elif self.MenuFonct.rangePolygone(Const.BTNSETTING_ACCUEIL, point):
                self.MenuFonct.afficherImage(231, 368, self.MenuFonct.triangle_selection)
                self.MenuFonct.afficherImage(340, 356, self.MenuFonct.accueilHover)

            elif self.MenuFonct.rangePolygone(Const.BTNQUIT_ACCUEIL, point):
                self.MenuFonct.afficherImage(231, 515, self.MenuFonct.triangle_selection)
                self.MenuFonct.afficherImage(340, 499, self.MenuFonct.accueilHover)

            elif self.MenuFonct.rangePolygone(Const.BTNMUSIQUE_ACCUEIL, point):
                self.MenuFonct.afficherImage(867, 673, self.MenuFonct.musiqueHover)
            else:
                self.MenuFonct.effacerImageInterne(self.MenuFonct.accueil)

    def ClickMenu(self):
        point = self.MenuFonct.recupererCoordonnerClick()
        if point is not None:
            if self.MenuFonct.rangePolygone(Const.BTNPLAY_ACCUEIL, point):
                self.choixniv.demarer()
                self.choixniv.BoucleLVL = True

            elif self.MenuFonct.rangePolygone(Const.BTNSETTING_ACCUEIL, point):
                print("Bouton Setting cliquer") # x + 4 et y + 8

            elif self.MenuFonct.rangePolygone(Const.BTNMUSIQUE_ACCUEIL, point):
                print("rentrer")
                if self.BTNMUSIQUE == 'ON':
                    self.BTNMUSIQUE = 'OFF'
                    self.MenuFonct.accueil = pygame.image.load('Images/Menu/AccueilOFF.png')
                    self.MenuFonct.effacerImageInterne(self.MenuFonct.accueil)

                elif self.BTNMUSIQUE == 'OFF':
                    self.BTNMUSIQUE = 'ON'
                    self.MenuFonct.accueil = pygame.image.load('Images/Menu/AccueilON.png')
                    self.MenuFonct.effacerImageInterne(self.MenuFonct.accueil)

            elif self.MenuFonct.rangePolygone(Const.BTNQUIT_ACCUEIL, point):
                exit()

            self.MenuFonct.actualiserFenetreGraphique()

