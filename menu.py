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

            elif self.PyFonct.RangePolygone(Const.BTNSETTING_ACCUEIL, point):
                self.PyFonct.afficherImage(231, 368, self.PyFonct.triangle_selection)

            elif self.PyFonct.RangePolygone(Const.BTNQUIT_ACCUEIL, point):
                self.PyFonct.afficherImage(231, 515, self.PyFonct.triangle_selection)
            else:
                self.PyFonct.effacerImageInterne(self.PyFonct.accueil)

    def ClickMenu(self,point):
        if point is not None:
            print(point)
            if self.PyFonct.RangePolygone(Const.BTNPLAY_ACCUEIL, point):
                # On remplace l'image de fond et on va dans une nouvelle boucle While True qui sera celle de choixNiveau
                self.PyFonct.effacerImageInterne(self.PyFonct.choixniveau)
                self.PyFonct.actualiserFenetreGraphique()
                # En appelant choix niveau ici, on restera bloquer tant que la personne ne cliquera pas sur back
                self.choixniv.demarer()
                # en sortant on remet l'image de fond
                self.PyFonct.effacerImageInterne(self.PyFonct.accueil)
                self.PyFonct.actualiserFenetreGraphique()
                self.choixniv.BoucleLVL = True

            elif self.PyFonct.RangePolygone(Const.BTNSETTING_ACCUEIL, point):
                print("Bouton Setting cliquer") # x + 4 et y + 8

            elif self.PyFonct.RangePolygone(Const.BTNMUSIQUE_ACCUEIL,point):
                if self.BTNMUSIQUE == 'ON':
                    self.BTNMUSIQUE = 'OFF'
                    self.PyFonct.accueil = pygame.image.load('Images/Menu/AccueilON.png')

                elif self.BTNMUSIQUE == 'OFF':
                    self.BTNMUSIQUE = 'ON'
                    self.PyFonct.accueil = pygame.image.load('Images/Menu/AccueilOFF.png')

            elif self.PyFonct.RangePolygone(Const.BTNQUIT_ACCUEIL, point):
                exit()

            self.PyFonct.actualiserFenetreGraphique()

