import pygame
import math
from gameobj import GameObject
from pygame.locals import *

# This is a ball object
class Ball(GameObject):
    def __init__(self, x, y, size):
        GameObject.__init__(self)
        self.image = pygame.image.load('assets/cat.gif').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_width = size[0]
        self.screen_height = size[1]

    def moveDown(self):
        pass
    def update(self):
        self.rect.x += 5
        if self.rect.x > self.screen_width:
            self.rect.x = -100

    def scale(self):
        pass

