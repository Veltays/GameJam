from PygameFonct import *
import pygame


class CreationBouton:

    def __init__(self):
        self.PyFonct = PyFonct()

    def Dessin(self):
        pygame.draw.polygon(self.PyFonct.screen, Const.BLACK, Const.BTNPLAY_ACCUEIL)
        pygame.draw.polygon(self.PyFonct.screen, Const.BLACK, Const.BTNSETTING_ACCUEIL)
        pygame.draw.polygon(self.PyFonct.screen, Const.BLACK, Const.BTNQUIT_ACCUEIL)




    def RangePolygone(self,polygon, point):
        x, y = point
        num_points = len(polygon)
        j = num_points - 1
        inside = False

        for i in range(num_points):
            xi, yi = polygon[i]
            xj, yj = polygon[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
                inside = not inside
            j = i

        return inside


