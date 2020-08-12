# coding : utf-8

# * import des libs
import pygame
from pion import Pion
from tour import Tour
from cavalier import Cavalier
from fou import Fou
from roi import Roi
from reine import Reine


# créer la classe game
class Game:
    
    def __init__(self):
        # je créer la liste de mes pieces
        self.pion_n = []
        self.pion_b = []
        self.reine_b = []
        self.reine_n = []
        self.roi_b = []
        self.roi_n = []
        self.cavalier_b = []
        self.cavalier_n = []
        self.fou_b = []
        self.fou_n = []
        self.tour_b = []
        self.tour_n = []
        
        # je vais créer les pieces en objet
        self.create_piece()

    # Fonction pour créer les pieces
    def create_piece(self):
        # pion
        y = 76
        x = 1
        for pion in range (8):
            pion = Pion("assets/pion_b.png", x, y)
            x += 75
            self.pion_b.append(pion)
        y = 451
        x = 1
        for pion in range (8):
            pion = Pion("assets/pion_n.png", x, y)
            x += 75
            self.pion_n.append(pion)

        # tour
        self.tour_b.append(Tour("assets/tour_b.png", 1, 1))
        self.tour_b.append(Tour("assets/tour_b.png", 526, 1))
        self.tour_n.append(Tour("assets/tour_n.png", 1, 526))
        self.tour_n.append(Tour("assets/tour_n.png", 526, 526))
        
        # cavalier
        self.cavalier_b.append(Cavalier("assets/cavalier_b.png", 76, 1))
        self.cavalier_b.append(Cavalier("assets/cavalier_b.png", 451, 1))
        self.cavalier_n.append(Cavalier("assets/cavalier_n.png", 76, 526))
        self.cavalier_n.append(Cavalier("assets/cavalier_n.png", 451, 526))
        
        # fou
        self.fou_b.append(Fou("assets/fou_b.png", 151, 1))
        self.fou_b.append(Fou("assets/fou_b.png", 376, 1))
        self.fou_n.append(Fou("assets/fou_n.png", 151, 526))
        self.fou_n.append(Fou("assets/fou_n.png", 376, 526))
        
        # roi
        self.roi_b.append(Roi("assets/roi_b.png", 226, 1))
        self.roi_n.append(Roi("assets/roi_n.png", 301, 526))
        
        # reine
        self.reine_b.append(Reine("assets/reine_b.png", 301, 1))
        self.reine_n.append(Reine("assets/reine_n.png", 226, 526))

    def update(self, screen):
        # update les pions
        for pion in range(8):
            screen.blit(self.pion_b[pion].image, self.pion_b[pion].rect)
            screen.blit(self.pion_n[pion].image, self.pion_n[pion].rect)
        
        # update les tours, cavaliers, fous
        for piece in range(2):
            # tour
            screen.blit(self.tour_b[piece].image, self.tour_b[piece].rect)
            screen.blit(self.tour_n[piece].image, self.tour_n[piece].rect)
            
            # cavalier
            screen.blit(self.cavalier_b[piece].image, self.cavalier_b[piece].rect)
            screen.blit(self.cavalier_n[piece].image, self.cavalier_n[piece].rect)
            
            # fou
            screen.blit(self.fou_b[piece].image, self.fou_b[piece].rect)
            screen.blit(self.fou_n[piece].image, self.fou_n[piece].rect)
            
        # roi
        screen.blit(self.roi_b[0].image, self.roi_b[0].rect)
        screen.blit(self.roi_n[0].image, self.roi_n[0].rect)
            
        # reine
        screen.blit(self.reine_b[0].image, self.reine_b[0].rect)
        screen.blit(self.reine_n[0].image, self.reine_n[0].rect)