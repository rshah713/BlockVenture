import pygame
from utils import start_on_platform
from game_data import SCREEN_SIZE
from Monsters import Monster

platforms = [
    pygame.Rect(200, 215, 85, 5),
    pygame.Rect(300, 170, 125, 5)
]

cursor = start_on_platform(platforms[0])

target = pygame.Rect(265, 125, 20, 20)
platform_switch = pygame.Rect(0, 0, 0, 0)

monsters = [Monster('tiger', platform=platforms[1])]

title = "Wild Tiger"