import pygame
from game_data import SCREEN_SIZE

platforms = [
    pygame.Rect(200, 155, 85, 5)
]

cursor = pygame.Rect(210, 148, 8, 8)

target = pygame.Rect(0, 0, 20, 20)
target.center = (SCREEN_SIZE[0]//2, 300)

monsters = []

title = "Fearless Drop"