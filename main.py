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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = None
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def get_width():
        return self.img.get_width()
    
    def get_height():
        return self.img.get_height()


class Player(Car):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = YELLOW_CAR
        self.mask = pygame.mask.from_surface(self.img)


class Enemy(Car):
    COLOR_MAP = {
        'red': RED_CAR,
        'green': GREEN_CAR,
        'blue': BLUE_CAR,
        'yellow': YELLOW_CAR
    }

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.img)

    def move(self, vel):
        self.y += vel


def collide(obj1, obj2):
    pass

    
def main():
    run = True
    FPS = 60
    lives = 3
    main_font = pygame.font.SysFont('comicsans', 50)
    lost_font = pygame.font.SysFont('comicsans', 60)

    enemies = []
    enemy_vel = 3

    player_vel = 5

    player = Player(0, 0) # Player(240, 650)

    clock = pygame.time.Clock()

    lost = False
    lost_live_count = 0

    def redraw_window():
        WIN.blit(BG, (0, 0))

        player.draw(WIN)

        if lost:
            pass

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0:
            pass

        if lost:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel

        for enemy in enemies:
            pass

def main_menu():
    pass

main()
