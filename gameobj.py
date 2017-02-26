import pygame
from pygame.locals import *
'''
General class for game objects
Note: do not make direct objects from this class
'''
class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        super(GameObject, self).__init__()
        self.image = None
        self.speed = 0
        self.direction = 0.0 # degrees
    def update(self):
        pass

