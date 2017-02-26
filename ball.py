import pygame
import math
from gameobj import GameObject
from pygame.locals import *

# This is a ball object
class Ball(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self)
        self.image = pygame.image.load('assets/cat.gif').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def moveDown(self):
        pass
    def update(self):
        self.rect.y += 1

    def scale(self):
        pass

