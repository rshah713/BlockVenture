import pygame

from utils import *

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

SCREEN_SIZE = (600, 350)

LEVEL_FAILED_FALL_SPEED = 4

MAX_JUMP_HEIGHT = 9
speed = {'x': 2, 'y': MAX_JUMP_HEIGHT}
Y_ACCELERATION = 1

in_jump = False
level_failed = False
level_complete = False