import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Définition de la taille de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clics de Souris")


# Fonction pour afficher un message à l'écran
def afficher_message(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)


# Boucle principale du programme
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Récupération des coordonnées du clic de souris
            mouse_pos = pygame.mouse.get_pos()
            print("Clic détecté aux coordonnées :", mouse_pos)

    # Effacer l'écran
    screen.fill(WHITE)
    # Afficher un message à l'écran
    afficher_message("Cliquez n'importe où !")
    # Rafraîchir l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()