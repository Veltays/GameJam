from PygameFonct import *
from Constante import *
import pygame



class Crackhead:

    def __init__(self):
        self.boolCrack = True
        self.PyFonct = PyFonct()
        self.compteurClick = 0
        self.upgradeClick = 15200000000000000000000000000


    def run_Crackhead(self):
        self.PyFonct.screen.fill(Const.WHITE)
        font = pygame.font.Font(None, 100)


        while self.boolCrack == True:


            score = font.render(str(self.compteurClick), 1, (0, 0, 0))   #style


            self.PyFonct.screen.blit(score, (500, 350))   # Affichage

            point = self.PyFonct.RecupererEvenementSouris()
            if point != None:
                self.compteurClick = self.compteurClick + self.upgradeClick
                point = None
                self.PyFonct.screen.fill(Const.WHITE)
            self.PyFonct.RecupererEvenementClavier()

            self.PyFonct.actualiserFenetreGraphique()



