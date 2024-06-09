"""
Author: Filip Borowiak
Date: Sunday 9th of June 2024
"""
import pygame

class Hero(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, TILL, stochastic = False):
       super().__init__()
       self.stochastic = stochastic
       self.TILL = TILL
       self.SCREEN_WIDTH = SCREEN_WIDTH
       self.SCREEN_HEIGHT = SCREEN_HEIGHT
       self.win = False
       # Create an image of the block, and fill it with a color.
       # This could also be an loaded image.
       self.image = pygame.image.load('assets/robot.png')
       self.image = pygame.transform.scale(self.image, (TILL, TILL)) 

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.topleft = (100, 100)
       self.rewards_collected = 0
       self.movements = ['left', 'right', 'up', 'down']
       
    '''
    It determines how agent behaves in the environment
    The default is a standard movement of value: 1
    ''' 
    def update(self, direction, obstacles, winnable, rewards, antiRewards):
        original_position = self.rect.topleft
        if direction == 'left' and self.rect.left > 0:
            self.rect.x -= self.TILL
        elif direction == 'right' and self.rect.right < self.SCREEN_WIDTH:
            self.rect.x += self.TILL
        elif direction == 'up' and self.rect.top > 0:
            self.rect.y -= self.TILL
        elif direction == 'down' and self.rect.bottom < self.SCREEN_HEIGHT:
            self.rect.y += self.TILL
                   
        if pygame.sprite.spritecollideany(self, obstacles) or not self.rect.colliderect(
            pygame.Rect(0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)):
            self.rect.topleft = original_position
        
        else:
            self.check_win(winnable) # check if you won
            self.collect_antiRewards(antiRewards) # check if collected any anti reward
            self.collect_rewards(rewards)# check if collected reward
            
    def collect_antiRewards(self, antiRewards):
        collected = pygame.sprite.spritecollide(self, antiRewards, True)
        if len(collected) > 0:
            self.rewards_collected += collected[0].value
            print(f"Anti reward: {collected[0].value:.2f}")
            print(f"Total value of collected rewards: {self.rewards_collected:.2f}")    
                
    def collect_rewards(self, rewards):
        if not self.win:
            collected = pygame.sprite.spritecollide(self, rewards, True)
            if len(collected) > 0:
                self.rewards_collected += collected[0].value
                print(f"Collected value of: {collected[0].value:.2f}")
                print(f"Total value of collected rewards: {self.rewards_collected:.2f}")
        
    def check_win(self, winnable):
        if self.rect.colliderect(winnable):
            print("You win!")
            self.win = True
            quit()
            
            