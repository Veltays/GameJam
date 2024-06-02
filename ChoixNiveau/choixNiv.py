from Constante import *
from PygameFonct import *
import pygame






class ChoixLVL:

        def __init__(self):
            self.PyFonct = PyFonct()
            self.BoucleLVL = True
        def demarer(self):
            while self.BoucleLVL:
                self.PyFonct.effacerImageInterne(self.PyFonct.choixniveau)

                point = self.PyFonct.RecupererEvenementSouris()
                self.ClickChoix(point)

                self.hoverChoix()

                self.PyFonct.actualiserFenetreGraphique()

        def ClickChoix(self, point):
                if point is not None:
                    print(point)
                    if self.PyFonct.RangePolygone(Const.CHOIXCRACKEAD, point):
                        print("Bouton Crackhead Tycoon")

                    elif self.PyFonct.RangePolygone(Const.CHOIXPARC, point):
                        print("Bouton Parc simulator")

                    elif self.PyFonct.RangePolygone(Const.CHOIXNERD, point):
                        print("Bouton NErd life")

                    elif self.PyFonct.RangePolygone(Const.CHOIXFEET, point):
                        print("Bouton Feet seeker")
                    elif self.PyFonct.RangePolygone(Const.BACKCHOIXBUTTON,point):
                        self.BoucleLVL = False

        def hoverChoix(self):
            point = self.PyFonct.MouseCOORD()
            if point is not None:
                if self.PyFonct.RangePolygone(Const.CHOIXCRACKEAD, point):
                    self.PyFonct.afficherImage(230, 175, self.PyFonct.choixHover)

                elif self.PyFonct.RangePolygone(Const.CHOIXPARC, point):
                    self.PyFonct.afficherImage(230, 311, self.PyFonct.choixHover)

                elif self.PyFonct.RangePolygone(Const.CHOIXNERD, point):
                    self.PyFonct.afficherImage(230, 447, self.PyFonct.choixHover)

                elif self.PyFonct.RangePolygone(Const.CHOIXFEET, point):
                    self.PyFonct.afficherImage(230, 583, self.PyFonct.choixHover)

                elif self.PyFonct.RangePolygone(Const.BACKCHOIXBUTTON, point):
                    self.PyFonct.afficherImage(862, 50, self.PyFonct.BackChoixHover)
