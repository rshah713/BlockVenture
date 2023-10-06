import pygame, sys
from pygame.locals import *

from utils import *

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

SCREEN_SIZE = (600, 350)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Dot Adventures!')
screen.fill(BLACK)

LEVEL_FAILED_FALL_SPEED = 4

MAX_JUMP_HEIGHT = 10
cursor = reset_cursor()
speed = {'x': 2, 'y': MAX_JUMP_HEIGHT}
Y_ACCELERATION = 1

platform1 = pygame.Rect(200, 250, 85, 5)
platform2 = pygame.Rect(325, 250, 85, 5)
target = pygame.Rect(0, 0, 20, 20)
target.center = (420, 195)

in_jump = False
level_failed = False
level_complete = False
while True:
    screen.fill(BLACK)

    pygame.draw.rect(screen, BLUE, platform1)
    pygame.draw.rect(screen, BLUE, platform2)
    pygame.draw.rect(screen, WHITE, cursor)
    pygame.draw.rect(screen, YELLOW, target)
        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 1)
        if event.type == KEYDOWN:
            if event.key == K_UP:
                in_jump = True

    if not in_jump and not in_valid_range(cursor, platform1, platform2):
        level_failed = True

    if cursor.colliderect(target):
        level_complete = True
        print('you won!')
        pygame.time.wait(1000)

    if level_failed:
        cursor.y += LEVEL_FAILED_FALL_SPEED
        if cursor.y > SCREEN_SIZE[1]:
            level_failed = False
            cursor = reset_cursor()

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        cursor.x += speed['x']
    if keys[K_LEFT]:
        cursor.x -= speed['x']

    if in_jump:
        cursor.y -= speed['y']
        speed['y'] -= Y_ACCELERATION
        # let y-speed increase until we get to max height
        # then we decrease y-speed until we reach negative jump height (bottom)
        if speed['y'] < -MAX_JUMP_HEIGHT:
            in_jump = False
            speed['y'] = MAX_JUMP_HEIGHT
            
            
        

    clock.tick(100)
    pygame.display.update()
