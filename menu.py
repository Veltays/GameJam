import pygame
from ChoixNiveau.choixNiv import *
from PygameFonct import *
from Constante import *
import time



class Menu:
    def __init__(self):
        self.PyFonct = PyFonct()
        self.PyFonct.AjouterFondMenuON()
        self.choixniv = ChoixLVL()
        self.PyFonct.actualiserFenetreGraphique()

        self.BTNMUSIQUE = 'ON'

    def Running(self):

        while True:

            point = self.PyFonct.RecupererEvenementSouris()
            self.ClickMenu(point)

            self.Hover()

            self.PyFonct.actualiserFenetreGraphique()

    def Hover(self):
        point = self.PyFonct.MouseCOORD()
        if point is not None:
            if self.PyFonct.RangePolygone(Const.BTNPLAY_ACCUEIL, point):
                self.PyFonct.afficherImage(231, 229, self.PyFonct.triangle_selection)
                self.PyFonct.afficherImage(340, 213, self.PyFonct.accueilHover)

            elif self.PyFonct.RangePolygone(Const.BTNSETTING_ACCUEIL, point):
                self.PyFonct.afficherImage(231, 368, self.PyFonct.triangle_selection)
                self.PyFonct.afficherImage(340, 356, self.PyFonct.accueilHover)

            elif self.PyFonct.RangePolygone(Const.BTNQUIT_ACCUEIL, point):
                self.PyFonct.afficherImage(231, 515, self.PyFonct.triangle_selection)
                self.PyFonct.afficherImage(340, 499, self.PyFonct.accueilHover)

            elif self.PyFonct.RangePolygone(Const.BTNMUSIQUE_ACCUEIL, point):
                self.PyFonct.afficherImage(867, 673, self.PyFonct.musiqueHover)
            else:
                self.PyFonct.effacerImageInterne(self.PyFonct.accueil)

    def ClickMenu(self,point):
        if point is not None:
            print(point)
            if self.PyFonct.RangePolygone(Const.BTNPLAY_ACCUEIL, point):
                self.choixniv.demarer()
                self.choixniv.BoucleLVL = True

            elif self.PyFonct.RangePolygone(Const.BTNSETTING_ACCUEIL, point):
                print("Bouton Setting cliquer") # x + 4 et y + 8

            elif self.PyFonct.RangePolygone(Const.BTNMUSIQUE_ACCUEIL, point):
                if self.BTNMUSIQUE == 'ON':
                    self.BTNMUSIQUE = 'OFF'
                    print(self.BTNMUSIQUE)
                    self.PyFonct.accueil = pygame.image.load('Images/Menu/AccueilON.png')
                    print(self.BTNMUSIQUE)

                elif self.BTNMUSIQUE == 'OFF':
                    self.BTNMUSIQUE = 'ON'
                    print(self.BTNMUSIQUE)
                    self.PyFonct.accueil = pygame.image.load('Images/Menu/AccueilOFF.png')
                    print(self.BTNMUSIQUE)

            elif self.PyFonct.RangePolygone(Const.BTNQUIT_ACCUEIL, point):
                exit()

            self.PyFonct.actualiserFenetreGraphique()

