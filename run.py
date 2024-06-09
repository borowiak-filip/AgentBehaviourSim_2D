"""
Author: Filip Borowiak
Date: Sunday 9th of June 2024
"""
import pygame
import random
import time
from game_objects.Hero import Hero
from game_objects.Obstacle import Obstacle
from game_objects.Reward import Reward
from game_objects.Winnable import Winnable
from game_objects.Grass import Grass
from game_objects.AntiReward import AntiReward
from extras.RewardGenerator import generate_reward_positions
from extras.EnvironmentSetup import *


pygame.init()

WIDTH = 15
HEIGHT = 15
TILL = 50
SCREEN_WIDTH = WIDTH * TILL
SCREEN_HEIGHT = HEIGHT * TILL
GRID_COLOR = (173, 216, 230)
LINE_COLOR = (90, 90, 90)

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('2D Square Grid Simulation')
clock = pygame.time.Clock()

# define an agent 
hero = Hero(SCREEN_WIDTH, SCREEN_HEIGHT, TILL, stochastic=True)

# keep reference of starting position for other object placement overlap
starting_pos = (0,0) 

# get objects locations
env_var = EnvironmentVariables()

# Create sprite groups
all_sprites = pygame.sprite.Group()
grass_tiles = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
rewards = pygame.sprite.Group()
winnables = pygame.sprite.Group()
antiRewards = pygame.sprite.Group()

all_sprites.add(hero)

# Create and add grass tiles
for x in range(WIDTH):
    for y in range(HEIGHT):
        grass = Grass(x, y, TILL)
        grass_tiles.add(grass)
        
# Create and add obstacles
obstacle_positions = env_var.getObstacles()
for pos in obstacle_positions:
    obstacle = Obstacle(pos[0], pos[1], TILL)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Create and add winnables
winnable_positions = env_var.getWinnable()
for pos in winnable_positions:
    winnable = Winnable(pos[0], pos[1], TILL)
    all_sprites.add(winnable)
    winnables.add(winnable)
winnable_position = winnables.sprites()[0].rect.topleft    
  
# Create and add anti-reward fields
antiReward_positions =  env_var.getAntiRewards()
for pos in antiReward_positions:
    antiReward = AntiReward(pos[0], pos[1], TILL, -0.1)
    if (pos[0], pos[1]) not in obstacle_positions and (pos[0], pos[1]not in starting_pos):
        all_sprites.add(antiReward)
        antiRewards.add(antiReward)
 
# Create and add rewards
reward_positions = generate_reward_positions((int(winnable_position[0]/TILL), int(winnable_position[1]/TILL)), (WIDTH, HEIGHT))
for pos in reward_positions:
    reward = Reward(pos[0], pos[1], TILL, pos[2])
    if (pos[0], pos[1]) not in obstacle_positions and (pos[0], pos[1]) not in starting_pos and (pos[0], pos[1]) not in antiReward_positions:
        all_sprites.add(reward)
        rewards.add(reward)  

running = True
# Main loop   
while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Keyboard movement setup
        elif event.type == pygame.KEYDOWN and not hero.stochastic:
            if event.key == pygame.K_LEFT:
                hero.update('left', obstacles, winnable, rewards, antiRewards)
            elif event.key == pygame.K_RIGHT:
                hero.update('right', obstacles, winnable, rewards, antiRewards)
            elif event.key == pygame.K_UP:
                hero.update('up', obstacles, winnable, rewards, antiRewards)
            elif event.key == pygame.K_DOWN:
                hero.update('down', obstacles, winnable, rewards, antiRewards)
                
    # if agent has some other autonomous function (e.g., stochastic)
    if hero.stochastic:
        hero.update(random.choice(hero.movements), obstacles, winnable, rewards, antiRewards)
    # Draw all objects 
    grass_tiles.draw(screen)     
    all_sprites.draw(screen)
   
    # Draw the grid
    for x in range(0, SCREEN_WIDTH, TILL):
        pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, TILL):
        pygame.draw.line(screen, LINE_COLOR, (0, y), (SCREEN_WIDTH, y))

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
    time.sleep(0.01) # decrease to speed up visual simulation

pygame.quit()