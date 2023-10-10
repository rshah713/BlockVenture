import pygame, sys
from pygame.locals import *

from utils import *
from game_data import *
from levels import level1, level2, level3, level4

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 15)
smaller_font = pygame.font.Font('freesansbold.ttf', 12)
pygame.display.set_caption('DotVenture!')
screen.fill(BLACK)

cursor_state = None
level = 1
level_switch = True # is it time to switch levels

test = False # flag when developing
prev_test_coord = None


while True:
    if not test:
        screen.fill(BLACK)
    
    if level_switch:
        if level == 1:
            cursor = level1.cursor.copy()
            cursor_state = level1.cursor.copy()
            platforms = level1.platforms
            target = level1.target
            title = level1.title
            directions = "Arrow keys to move and jump"
            
        elif level == 2:
            cursor = level2.cursor.copy()
            cursor_state = level2.cursor.copy()
            platforms = level2.platforms
            target = level2.target
            title = level2.title
            directions = ""
        elif level == 3:
            cursor = level3.cursor.copy()
            cursor_state = level3.cursor.copy()
            platforms = level3.platforms
            target = level3.target
            title = level3.title
            directions = ""
        elif level == 4:
            cursor = level4.cursor.copy()
            cursor_state = level4.cursor.copy()
            platforms = level4.platforms
            target = level4.target
            title = level4.title
            directions = ""

        level_complete = False
        level_switch = False
        
        directions_text = smaller_font.render(directions, True, WHITE)
        directions_text_rect = directions_text.get_rect()
        directions_text_rect.midleft = (0, SCREEN_SIZE[1]//2)
        
        level_title = "Level {} - {}".format(level, title)
        level_score = font.render(level_title, True, WHITE)
        level_score_rect = level_score.get_rect()
        level_score_rect.topleft = (0, 0)
        
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)
        
    screen.blit(directions_text, directions_text_rect)
    screen.blit(level_score, level_score_rect)
    pygame.draw.rect(screen, WHITE, cursor)
    pygame.draw.rect(screen, YELLOW, target)
        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if test:
                pos = pygame.mouse.get_pos()
                print(pos)
                if prev_test_coord is None:
                    prev_test_coord = pos
                else:
                    pygame.draw.line(screen, WHITE, prev_test_coord, pos, 3)
                    prev_test_coord = None
                    print()
                pygame.draw.circle(screen, WHITE, pos, 3)
        if event.type == KEYDOWN:
            if event.key == K_UP:
                in_jump = True
            if event.key == K_d:
                test = not test

    if not in_jump and not in_valid_range(cursor, *platforms):
        level_failed = True

    if cursor.colliderect(target):
        level_complete = True
        level_failed = False
        print('you won')
    
    if level_complete:
        level_switch = True
        level += 1
        level_failed = False

    if level_failed:
        cursor.y += LEVEL_FAILED_FALL_SPEED
        if cursor.y > SCREEN_SIZE[1]:
            level_failed = False
            cursor = cursor_state.copy()
        # constantly check if we hit another platform
        if in_valid_range(cursor, *platforms):
#             calibrate_cursor(cursor, *platforms)
            level_failed = False

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
            calibrate_cursor(cursor, *platforms)
         # for smoother jump animation, let it catch the platform only on the way down (speed < 0)
        if speed['y'] < 0 and in_valid_range(cursor, *platforms):
            calibrate_cursor(cursor, *platforms)
            speed['y'] = MAX_JUMP_HEIGHT
            in_jump = False
            level_failed = False

    clock.tick(70)
    pygame.display.update()