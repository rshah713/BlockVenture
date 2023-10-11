import pygame
from Monsters import Monster

platforms = [
    pygame.Rect(200, 250, 85, 5),
    pygame.Rect(325, 250, 85, 5)
]

cursor = pygame.Rect(200, 243, 8, 8)

target = pygame.Rect(0, 0, 20, 20)
target.center = (420, 195)

# monsters = []
monsters = [Monster('lava'), Monster('lava', pos=(400, 200), jump_height=10)]


title = "Uncharted Territory"