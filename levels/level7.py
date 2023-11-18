import pygame
from utils import start_on_platform
from game_data import SCREEN_SIZE
from Monsters import Monster

platforms = [
    pygame.Rect(265, 285, 85, 5),
    pygame.Rect(280, 250, 85, 5),
    pygame.Rect(415, 230, 85, 5),
    pygame.Rect(230, 280, 145, 5)
]
green_platforms = [
    pygame.Rect(415, 250, 85, 5),
    pygame.Rect(230, 280, 145, 5),
    pygame.Rect(110, 280, 85, 5),
    pygame.Rect(110, 230, 85, 5),
    pygame.Rect(110, 180, 85, 5),
    pygame.Rect(110, 130, 85, 5)
]

cursor = start_on_platform(platforms[0])
sword = pygame.Rect(0,0,0,0)

target = pygame.Rect(130, 70, 20, 20)
platform_switch = pygame.Rect(455, 200, 20, 20)

monsters = [Monster('tiger', platform=platforms[3])]

title = "It's dangerous to go alone"