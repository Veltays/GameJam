from Constante import *
from MenuFonct import *
from CrackheadSIM.CrackheadSIM import *
import pygame






class ChoixLVL:

        def __init__(self):
            self.MenuFonct = MenuFonct()
            self.Crackhead = Crackhead()
            self.BoucleLVL = True

        def demarer(self):
            while self.BoucleLVL:
                self.MenuFonct.effacerImageInterne(self.MenuFonct.choixniveau)

                self.ClickChoix()

                self.hoverChoix()

                self.MenuFonct.actualiserFenetreGraphique()


        def ClickChoix(self):
            point = self.MenuFonct.recupererCoordonnerClick()
            if point is not None:
                if self.MenuFonct.rangePolygone(Const.CHOIXCRACKEAD, point):
                    print("Bouton Crackhead Tycoon")
                    self.Crackhead.run_Crackhead()
                    self.Crackhead.boolCrack = True

                elif self.MenuFonct.rangePolygone(Const.CHOIXPARC, point):
                    print("Bouton Parc simulator")

                elif self.MenuFonct.rangePolygone(Const.CHOIXNERD, point):
                    print("Bouton NErd life")

                elif self.MenuFonct.rangePolygone(Const.CHOIXFEET, point):
                    print("Bouton Feet seeker")
                elif self.MenuFonct.rangePolygone(Const.BACKCHOIXBUTTON,point):
                    self.BoucleLVL = False

        def hoverChoix(self):
            point = self.MenuFonct.mouseCOORD()
            if point is not None:
                if self.MenuFonct.rangePolygone(Const.CHOIXCRACKEAD, point):
                    self.MenuFonct.afficherImage(230, 175, self.MenuFonct.choixHover)

                elif self.MenuFonct.rangePolygone(Const.CHOIXPARC, point):
                    self.MenuFonct.afficherImage(230, 311, self.MenuFonct.choixHover)

                elif self.MenuFonct.rangePolygone(Const.CHOIXNERD, point):
                    self.MenuFonct.afficherImage(230, 447, self.MenuFonct.choixHover)

                elif self.MenuFonct.rangePolygone(Const.CHOIXFEET, point):
                    self.MenuFonct.afficherImage(230, 583, self.MenuFonct.choixHover)

                elif self.MenuFonct.rangePolygone(Const.BACKCHOIXBUTTON, point):
                    self.MenuFonct.afficherImage(862, 50, self.MenuFonct.BackChoixHover)
