import pygame
from Monsters import Monster

platforms = [
    pygame.Rect(200, 250, 85, 5),
    pygame.Rect(325, 250, 85, 5)
]

cursor = pygame.Rect(200, 243, 8, 8)
platform_switch = pygame.Rect(0, 0, 0, 0)

target = pygame.Rect(0, 0, 20, 20)
target.center = (420, 195)

monsters = []

title = "Uncharted Territory"