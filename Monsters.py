import pygame
# study 2-3 tree
class Monster:
    
    def __init__(self, m_type='lava', pos=None, size=None, jump_height=None, speed=None, acceleration=None):
        self.m_type = m_type
        self.jump_height = jump_height
        self.speed = speed
        self.acceleration = acceleration
        self.pos = pos
        self.size = size
        self.create_monster()
        
    def create_monster(self):
        if self.m_type == 'lava':
            self.pos = (300, 200) if self.pos is None else self.pos
            self.size = (10, 10) if self.size is None else self.size
            self.jump_height = 10 if self.jump_height is None else self.jump_height
            self.speed = self.jump_height if self.speed is None else self.speed
            self.acceleration = 1 if self.acceleration is None else self.acceleration
            self.monster = pygame.Rect(*self.pos, *self.size)
            
    def get_monster(self):
        return self.monster
    
    def center_on_platform(self, platform):
        self.monster.midbottom = platform.midtop
        return self
    
    def move(self):
        if self.m_type == 'lava':
            self.monster.y -= self.speed
            self.speed -= self.acceleration
            # let y-speed increase until we get to max height
            # then we decrease y-speed until we reach negative jump height (bottom)
            if self.speed < -self.jump_height:
                self.speed = self.jump_height
    
        