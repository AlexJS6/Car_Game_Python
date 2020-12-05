#https://onlinepngtools.com/create-transparent-png
import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 500, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trafic')

# Images
PLAYER_CAR = pygame.image.load(os.path.join('assets', 'player.png'))
YELLOW_CAR = pygame.image.load(os.path.join('assets', 'yellow.png'))
RED_CAR = pygame.image.load(os.path.join('assets', 'red.png'))
BLUE_CAR = pygame.image.load(os.path.join('assets', 'blue.png'))
GREEN_CAR = pygame.image.load(os.path.join('assets', 'green.png'))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background.png')), (WIDTH, HEIGHT))

