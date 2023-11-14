import pygame

def in_valid_range(cursor, *platforms):
    '''
    check whether the cursor is currently touching any platforms
    '''
    for platform in platforms:
        if cursor.colliderect(platform):
            return True
    return False


def calibrate_cursor(cursor, *platforms):
    '''
    calibrate the cursor to the top of the platform so it stops getting stuck
    '''
    for platform in platforms:
        if cursor.colliderect(platform):
            cursor.bottom = platform.top - 2
            return
        
        
def control_lava_monster(m, screen):
    '''
    helper function to move every monster on the screen and redraw it
    '''
    for monster in m:  
        monster.move()
        pygame.draw.rect(screen, monster.get_color(), monster.get_monster())
        
        
def check_monster_hit(cursor, monsters):
    '''
    helper function to check whether any monsters have hit the cursor
    '''
    for monster in monsters:
        if monster.get_monster().colliderect(cursor):
            return True
    return False

def start_on_platform(platform):
    '''
    allow the cursor to begin in the center of a platform
    '''
    cursor = pygame.Rect(0, 0, 8, 8)
    cursor.midbottom = platform.midtop
    return cursor
        
    
def check_platform_switch(cursor, p_switch, plats, lev):
    '''
    check whether its time to switch onto green platforms
    '''
    if p_switch.topleft == (0,0):
        return False, plats # costly to do colliderect when we know it fails
    if cursor.colliderect(p_switch):
        return True, lev.green_platforms
    return False, plats