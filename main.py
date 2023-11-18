import pygame, sys
from pygame.locals import *

from utils import *
from game_data import *
from levels import level1, level2, level3, level4, level5, level6, level7

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
switch = False
monster_hit = False

start_menu = True
offset = 10
font = pygame.font.Font('freesansbold.ttf', 20)
begin_font = pygame.font.Font('freesansbold.ttf', 35)
game_ttl = font.render('BlockVenture', True, BLACK)
game_ttl_r = game_ttl.get_rect()
game_ttl_r.center = (SCREEN_SIZE[0]//2+SCREEN_SIZE[0]//16, 100)
begin_btn = begin_font.render("[BEGIN]", True, WHITE)
begin_btn_r = begin_btn.get_rect()
begin_btn_r.center = (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2+SCREEN_SIZE[1]//10)


test = False # flag when developing
prev_test_coord = None



while True:
    if not test:
        screen.fill(BLACK)
    
    if start_menu:
        pygame.draw.polygon(screen, YELLOW, ((220, 55-offset), (220, 105-offset), (165, 105-offset), (165, 120-offset), 
                                             (220, 120-offset), (220, 165-offset), (230, 165-offset), (245,130-offset), 
                                             (420+10, 130-offset), (455+10, 110-offset),(420+10, 90-offset), 
                                             (245, 90-offset), (230, 55-offset)))
        screen.blit(game_ttl, game_ttl_r)
        screen.blit(begin_btn, begin_btn_r)
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if begin_btn_r.collidepoint(pos):
                    start_menu = False
        pygame.display.update()
        continue
    
    if level_switch:
        if level == 1:
            lev = level1
            cursor = level1.cursor.copy()
            cursor_state = level1.cursor.copy()
            platforms = level1.platforms
            target = level1.target
            platform_switch = level1.platform_switch
            title = level1.title
            monsters = level1.monsters
            directions = "Arrow keys to move and jump"
        elif level == 2:
            lev = level2
            cursor = level2.cursor.copy()
            cursor_state = level2.cursor.copy()
            platforms = level2.platforms
            target = level2.target
            platform_switch = level2.platform_switch
            title = level2.title
            monsters = level2.monsters
            directions = ""
        elif level == 3:
            lev = level3
            cursor = level3.cursor.copy()
            cursor_state = level3.cursor.copy()
            platforms = level3.platforms
            target = level3.target
            platform_switch = level3.platform_switch
            title = level3.title
            monsters = level3.monsters
        elif level == 4:
            lev = level4
            cursor = level4.cursor.copy()
            cursor_state = level4.cursor.copy()
            platforms = level4.platforms
            target = level4.target
            platform_switch = level4.platform_switch
            title = level4.title
            monsters = level4.monsters
        elif level == 5:
            lev = level5
            cursor = level5.cursor.copy()
            cursor_state = level5.cursor.copy()
            platforms = level5.platforms
            target = level5.target
            platform_switch = level5.platform_switch
            title = level5.title
            monsters = level5.monsters
            directions = ""
        elif level == 6:
            lev = level6
            cursor = level6.cursor.copy()
            cursor_state = level6.cursor.copy()
            platforms = level6.platforms
            target = level6.target
            platform_switch = level6.platform_switch
            title = level6.title
            monsters = level6.monsters

            

        level_complete = False
        level_switch = False
        
        directions_text = smaller_font.render(directions, True, WHITE)
        directions_text_rect = directions_text.get_rect()
        directions_text_rect.midleft = (0, SCREEN_SIZE[1]//2)
        
        level_title = "Level {} - {}".format(level, title)
        level_score = font.render(level_title, True, WHITE)
        level_score_rect = level_score.get_rect()
        level_score_rect.topleft = (0, 0)
        
        
    if not switch:
        for platform in platforms:
            pygame.draw.rect(screen, BLUE, platform)
        pygame.draw.rect(screen, GREEN, platform_switch)
        switch, platforms = check_platform_switch(cursor, platform_switch, platforms, lev)
    elif switch:
        for platform in platforms:
            pygame.draw.rect(screen, GREEN, platform)
    
    control_lava_monster(monsters, screen)
    if check_monster_hit(cursor, monsters):
#         cursor = cursor_state.copy()
        level_failed = True
        monster_hit = True
        
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
        switch = False

    if level_failed:
        cursor.y += LEVEL_FAILED_FALL_SPEED
        if cursor.y > SCREEN_SIZE[1] or monster_hit:
            level_failed = False
            cursor = cursor_state.copy()
            switch = False
            platforms = lev.platforms
            monster_hit = False
        # constantly check if we hit another platform
        if in_valid_range(cursor, *platforms):
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

    clock.tick(FPS)
    pygame.display.update()