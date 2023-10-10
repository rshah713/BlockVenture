import pygame
from game_data import SCREEN_SIZE


platforms = [
    pygame.Rect(430, 280, 85, 5),
    pygame.Rect(200, 250, 85, 5),
    pygame.Rect(325, 250, 85, 5),
    pygame.Rect(60, 295, 85, 5),
    pygame.Rect(165, 215, 85, 5),
    pygame.Rect(220, 175, 85, 5)
]

cursor = pygame.Rect(500, 270, 8, 8)

target = pygame.Rect(0, 0, 20, 20)
target.center = (340, 125)

monsters = [None]

title = "Blazing Fury"