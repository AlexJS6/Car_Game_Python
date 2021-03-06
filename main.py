#https://onlinepngtools.com/create-transparent-png
import pygame
import os
import time
import random
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trafic')

CRASH_SOUND = pygame.mixer.Sound('assets/crash.mp3')

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

    def get_width(self):
        return self.img.get_width()
    
    def get_height(self):
        return self.img.get_height()


class Player(Car):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = PLAYER_CAR
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
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    
def main():
    run = True
    FPS = 60
    lives = 3
    score = 0
    main_font = pygame.font.SysFont('comicsans', 50)
    lost_font = pygame.font.SysFont('comicsans', 60)

    enemies = []
    enemy_vel = 3

    player_vel = 4.5

    player = Player(260, 630) 

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0, 0))

        lives_label = main_font.render(f'Lives: {lives}', 1, (150, 0, 0))
        score_label = main_font.render(f'Score: {int(score)}', 1, (150, 0, 0))

        WIN.blit(lives_label, (10, HEIGHT - 40))
        WIN.blit(score_label, (WIDTH - score_label.get_width() -10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render('YOU LOST!!!', 1, (255, 0, 0))
            WIN.blit(lost_label, (WIDTH/2 -lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS *3:
                run = False
            else:
                continue

        if len(enemies) <= 3:
            enemy_vel += 0.3
            score += 30* enemy_vel
            for i in range(4):
                enemy = Enemy(random.choice([110, 180, 260, 335]), random.randrange(-2000, -500), random.choice(['red', 'yellow', 'blue', 'green']))
                #pass # enemy = Enemy(choice(x), choice(y), choice(color))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel -80 > 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() +80 < WIDTH:
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel

        for i, enemy in enumerate(enemies[:]): # try without [:]
            enemy.move(enemy_vel)

            '''if collide(enemy, enemies[i -1]):
                print('removed:',enemy.y, 'other:', enemies[i -1].y, i)
                enemies.remove(enemy)'''

            if collide(enemy, player):
                print('player:', player.y, 'enemy:', enemy.y)
                CRASH_SOUND.play()
                time.sleep(1)
                CRASH_SOUND.stop()
                lives -= 1
                enemies.remove(enemy)
            elif enemy.y > HEIGHT:
                enemies.remove(enemy)
            
# maybe launch in waves
def main_menu():
    title_font = pygame.font.SysFont("comicsans", 50)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()

# cars can't be 1 on another
