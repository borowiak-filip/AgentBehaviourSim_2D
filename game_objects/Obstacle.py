"""
Author: Filip Borowiak
Date: Sunday 9th of June 2024
"""
import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, TILL):
        super().__init__()
        self.TILL = TILL
        self.image = pygame.image.load('assets/wall_till.png')
        self.image = pygame.transform.scale(self.image, (self.TILL, self.TILL)) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * self.TILL, y * self.TILL)
