import time

import pygame


# Initialisation de Pygame
pygame.init()

# Définition des constantes
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Chargement de l'image
image = pygame.image.load('Images/CrackheadSIM/RoueCulDuV.png').convert_alpha()
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Point de rotation (centre de la fenêtre)
rotation_point = (WIDTH // 2, HEIGHT // 2)

# Angle de rotation en degrés
angle = 0

# Boucle principale
running = True


while running:
    # Remplir l'écran de blanc
    screen.fill(WHITE)

    # Calculer la nouvelle position de l'image
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image_rect.center)

    # Dessiner l'image tournée
    screen.blit(rotated_image, new_rect.topleft)

    # Mettre à jour l'angle de rotation
    angle += 3
    if angle >= 360:
        angle = 0

    # Mettre à jour l'affichage
    pygame.display.flip()
    time.sleep(0.01)

pygame.quit()