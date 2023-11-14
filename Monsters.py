import pygame
from game_data import FPS
class Monster:
    
    def __init__(self, m_type='lava', pos=None, size=None, jump_height=None, speed=None, acceleration=None, platform=None, range_y=None):
        '''
        m_type: the monster type to create
        pos: (optional), where to position the monster
        size: size of the monster
        jump_height: (lava, optional)
        speed: (optional) the speed of the monster in the vertical/horizontal direction
        acceleration: (optional) for both horizontal or vertical
        platform: (tiger), what platform to guard
        range_y: (flyer), representing the range in the y-direction, assume upward direction
        '''
        self.m_type = m_type
        self.jump_height = jump_height
        self.speed = speed
        self.acceleration = acceleration
        self.pos = pos
        self.size = size
        self.platform = platform
        self.range = range_y
        self.create_monster()
        
    def create_monster(self):
        if self.m_type == 'lava':
            self.color = (255, 0, 0)
            self.pos = (300, 200) if self.pos is None else self.pos
            self.size = (10, 10) if self.size is None else self.size
            self.speed = 5
            self.acceleration = .15
            self.monster = pygame.Rect(*self.pos, *self.size)
            self.init_speed = self.speed
            self.init_jump_y = self.pos[1]
        elif self.m_type == 'tiger':
            self.color = (255, 165, 0)
            self.pos = (0, 0) if self.pos is None else self.pos
            self.size = (15, 15) if self.size is None else self.size
            self.speed = 3 if self.speed is None else self.speed
            self.monster = pygame.Rect(*self.pos, *self.size)
            self.dir = 'right'
            self.center_on_platform(self.platform)
        elif self.m_type == 'flyer':
            self.color = (128, 0, 128)
            self.pos = (0, 0) if self.pos is None else self.pos
            self.size = (15, 15) if self.size is None else self.size
            self.speed = 4 if self.speed is None else self.speed
            self.monster = pygame.Rect(*self.pos, *self.size)
            self.dir = 'up'



    def get_monster(self):
        return self.monster
    
    def get_color(self):
        return self.color

    
    def center_on_platform(self, platform):
        self.monster.midbottom = platform.midtop
        self.init_jump_y = self.monster.y
        return self
    
    def move(self):
        if self.m_type == 'lava':
            self.monster.y -= self.speed * .014 * (FPS // 2)
            self.speed -= self.acceleration
            # let y-speed increase until we get to max height
            # then we decrease y-speed until we reach negative jump height (bottom)
            if self.monster.y >= self.init_jump_y:
                self.speed = self.init_speed
                self.monster.y = self.init_jump_y
        elif self.m_type == 'tiger':
            if self.dir == 'right':
                self.monster.x += self.speed
            elif self.dir == 'left':
                self.monster.x -= self.speed
            if not(self.platform.x <= self.monster.x <= self.platform.right):
                self.dir = 'right' if self.dir == 'left' else 'left'
        elif self.m_type == 'flyer':
            if self.dir == 'up':
                self.monster.y -= self.speed
            elif self.dir == 'down':
                self.monster.y += self.speed
            if not(self.pos[1] <= self.monster.y <= self.pos[1]+self.range):
                self.dir = 'up' if self.dir == 'down' else 'down'
                
    
        