# coding: utf-8

import pygame

# créer la classe des Cavalier
class Cavalier():

    def __init__(self, path, x, y):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (73, 73))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
