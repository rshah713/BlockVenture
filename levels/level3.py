import pygame
from game_data import SCREEN_SIZE


x = pygame.Rect(0, 0, 85, 5)
x.center = (SCREEN_SIZE[0]//2, 275)
platforms = [
    pygame.Rect(200, 155, 85, 5),
    x
]

cursor = pygame.Rect(210, 148, 8, 8)

target = pygame.Rect(0, 0, 20, 20)
target.center = (SCREEN_SIZE[0]//2, 300)

title = "Fearless Drop"