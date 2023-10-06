import pygame


def reset_cursor():
    # later we can pass starting level pos in here
    return pygame.Rect(200, 243, 8, 8)


def in_valid_range(cursor, *platforms):
    #if its on a platform its fine
    for platform in platforms:
        if cursor.colliderect(platform):
            return True
    return False
