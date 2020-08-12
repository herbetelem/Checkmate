# coding: utf-8

import pygame

# créer la classe des herbes
class Tour():
    """
        Architecture de l'herbe
    """

    def __init__(self, path, x, y):
        # Load le sprite de l'herbe
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (73, 73))
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
