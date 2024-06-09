"""
Author: Filip Borowiak
Date: Sunday 9th of June 2024
"""
import pygame

class AntiReward(pygame.sprite.Sprite):
    def __init__(self, x, y, TILL, value):
        super().__init__()
        self.TILL = TILL
        self.value = value
        self.image = pygame.image.load('assets/damage.png')
        self.image = pygame.transform.scale(self.image, (self.TILL, self.TILL))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * self.TILL, y * self.TILL)  # Position based on grid coordinates
