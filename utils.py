import pygame

def in_valid_range(cursor, *platforms):
    #if its on a platform its fine
    for platform in platforms:
        if cursor.colliderect(platform):
            return True
    return False