import pygame
from utils import start_on_platform
from game_data import SCREEN_SIZE
from Monsters import Monster

platforms = [ 
    pygame.Rect(280, 250, 85, 5),
    pygame.Rect(365, 190, 85, 5),
    pygame.Rect(410, 240, 85, 5)
]
green_platforms = []

cursor = start_on_platform(platforms[0])
sword = pygame.Rect(0,0,0,0)

target = pygame.Rect(130, 70, 20, 20)
platform_switch = pygame.Rect(405, 175, 20, 20)

monsters = [Monster('lava').center_on_platform(platforms[1])]

title = "It's dangerous to go alone"