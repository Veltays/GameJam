import pygame

from CreateButton import *
from PygameFonct import *
import time


class Menu:
    def __init__(self):
        self.PyFonct = PyFonct()

        self.Button = CreationBouton()
        self.Button.Dessin()

        self.PyFonct.AjouterFondMenu()

        self.PyFonct.actualiserFenetreGraphique()

    def Running(self):

        while True:

            point = self.PyFonct.RecupererEvenement()
            self.ClickMenu(point)

            self.Hover()


            self.PyFonct.actualiserFenetreGraphique()


    def Hover(self):
        point = self.PyFonct.MouseCOORD()
        if point is not None:
            if self.Button.RangePolygone(Const.BTNPLAY_ACCUEIL, point):
                self.PyFonct.afficherImage(231, 229,self.PyFonct.triangle_selection)

                # Afficher le choix de jeu

            elif self.Button.RangePolygone(Const.BTNSETTING_ACCUEIL, point):
                self.PyFonct.afficherImage(231, 368, self.PyFonct.triangle_selection)

            elif self.Button.RangePolygone(Const.BTNQUIT_ACCUEIL, point):
                self.PyFonct.afficherImage(231, 515, self.PyFonct.triangle_selection)
            else:
                self.PyFonct.effacerImageInterne(self.PyFonct.accueil)


    def ClickMenu(self,point):
        if point is not None:
            print(point)
            if self.Button.RangePolygone(Const.BTNPLAY_ACCUEIL, point):
                self.PyFonct.effacerImageInterne(self.PyFonct.choixniveau)

                # Afficher le choix de jeu

            elif self.Button.RangePolygone(Const.BTNSETTING_ACCUEIL, point):
                self.PyFonct.afficherImage(231, 344, self.PyFonct.triangle_selection)  # x + 4 et y + 8

            elif self.Button.RangePolygone(Const.BTNQUIT_ACCUEIL, point):
                exit()