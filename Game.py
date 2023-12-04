import pygame
from Joueur import Player


class Game:
    def __init__(self):
        # Generate our player
        self.player = Player()
        # Generate our group of monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        #self.spawn_monster()