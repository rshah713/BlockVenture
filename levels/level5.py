import pygame
from utils import start_on_platform
from game_data import SCREEN_SIZE
from Monsters import Monster

platforms = [
    pygame.Rect(160, 255, 85, 5),
    pygame.Rect(280, 280, 85, 5),
    pygame.Rect(395, 255, 85, 5)
]
green_platforms = [
    pygame.Rect(400, 240, 85, 5),
    pygame.Rect(285,220, 85, 5),
    pygame.Rect(165, 195, 85, 5)
]

cursor = start_on_platform(platforms[0])

target = pygame.Rect(195, 145, 20, 20)
platform_switch = pygame.Rect(450, 190, 20, 20)

monsters = [Monster('flyer', pos=(260,130), range_y=170)]

title = "Uncharted Territory"