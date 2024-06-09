import time

from CrackheadSIM.CrackFonct import *
from ConstanteMenu import *
import pygame



class Crackhead:

    def __init__(self):
        self.boolCrack = True
        self.CrackFonct = FonctionCrack()
        self.compteurClick = 1
        self.upgradeClick = 1


    def run_Crackhead(self):
        pygame.init()
        font = pygame.font.Font(None, 50)

        while self.boolCrack:

            self.recupererLesEvenements()


            self.CrackFonct.effacerImageInterne(self.CrackFonct.crackheadFOND)
            self.AffichageScore(font)
            self.CrackFonct.actualiserFenetreGraphique()
            time.sleep(0.1)
            print(1)


    def recupererLesEvenements(self):
        evenement = self.CrackFonct.recupererEvenement()
        if evenement == pygame.K_ESCAPE:
            print("Échap détecté:", evenement)
            self.boolCrack = False
        if evenement == pygame.BUTTON_LEFT:
            self.compteurClick = self.compteurClick + self.upgradeClick
            point = None
            self.CrackFonct.screen.fill(Const.WHITE)
            # print(self.compteurClick)
            # print(self.CrackFonct.positionSourisCrack)

    def AffichageScore(self,font):
        score = font.render(str(self.compteurClick), 1, (0, 0, 0))  # style
        self.CrackFonct.screen.blit(score, (429, 37))  # Affichage