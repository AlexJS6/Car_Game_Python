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

class Car:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def get_width():
        return self.img

    
def main():
    run = True
    FPS = 60
    lives = 3
    main_font = pygame.font.SysFont('comicsans', 50)
    lost_font = pygame.font.SysFont('comicsans', 60)
    