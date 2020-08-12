# coding : utf-8
# IMPORT
import pygame

from game import Game
# INITIALISATION DE PYGAME

pygame.init()

# CREATION DE LA FENETRE
# Changer le titre de la fenêtre
pygame.display.set_caption("Checkmate")

# Dimensionner la fenêtre
screen = pygame.display.set_mode((600, 600))

# importer et charger le background
background = pygame.image.load('assets/plateau.jpg')
background = pygame.transform.scale(background, (600, 600))
game = Game()
running = True
while running :
    # appliquer le background
    screen.blit(background, (0,0))
    game.update(screen)
    for event in pygame.event.get() :
        # Si l'event généré par l'utilisateur est de quitter
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()