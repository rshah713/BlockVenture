import pygame

def in_valid_range(cursor, *platforms):
    #if its on a platform its fine
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
            cursor.bottom = platform.top -2
            return
        
        
def control_lava_monster(m, screen):
    
    for monster in m:  
        monster.move()
        pygame.draw.rect(screen, (255, 0, 0), monster.get_monster())
        
        
def check_monster_hit(cursor, monsters):
    for monster in monsters:
        if monster.get_monster().colliderect(cursor):
            return True
    return False
        