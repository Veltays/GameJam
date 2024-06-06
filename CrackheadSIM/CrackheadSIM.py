import time

from PygameFonct import *
from Constante import *
import pygame



class Crackhead:

    def __init__(self):
        self.boolCrack = True
        self.PyFonct = PyFonct()
        self.compteurClick = 1
        self.upgradeClick = 1


    def run_Crackhead(self):
        pygame.init()
        font = pygame.font.Font(None, 100)

        while self.boolCrack:
            self.recupererElementClavier()
            score = font.render(str(self.compteurClick), 1, (0, 0, 0))   #style
            self.CompteurDeClick()

            self.PyFonct.effacerImageInterne(self.PyFonct.crackheadFOND)
            self.PyFonct.screen.blit(score, (500, 350))  # Affichage
            self.PyFonct.actualiserFenetreGraphique()







    def CompteurDeClick(self):
        point = self.PyFonct.recupererEvenementSouris()
        if point != None:
            self.compteurClick = self.compteurClick + self.upgradeClick
            point = None
            self.PyFonct.screen.fill(Const.WHITE)
            print(self.compteurClick)


    def recupererElementClavier(self):
        evenement = self.PyFonct.recupererEvenementClavier()
        if evenement == pygame.K_ESCAPE:
            print("Échap détecté:", evenement)
            self.boolCrack = False