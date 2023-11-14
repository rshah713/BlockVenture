import pygame
from utils import start_on_platform
from game_data import SCREEN_SIZE
from Monsters import Monster

platforms = [
    pygame.Rect(160, 255, 85, 5),
    pygame.Rect(280, 280, 85, 5),
    pygame.Rect(400, 255, 85, 5)
]

cursor = start_on_platform(platforms[0])

target = pygame.Rect(265, 125, 20, 20)

monsters = [Monster('flyer', pos=(260,130), range_y=170)]

title = "Uncharted Territory"