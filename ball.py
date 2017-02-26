import pygame
import math
import random
from gameobj import GameObject
from pygame.locals import *

# This is a ball object
class Ball(GameObject):
    def __init__(self, x, y, size):
        GameObject.__init__(self)
        self.image = pygame.image.load('assets/cat.gif').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x + 1
        self.rect.y = y
        self.speed = 3
        self.screen_width = size[0]
        self.screen_height = size[1]
        self.wallHit = None # marks where we hit a wall
        self.direction = random.randint(0,360)
        print(self.direction)

    def moveDown(self):
        pass

    def update(self):
        self.detectHit()

        if not self.wallHit == None:
            if self.wallHit[0] >= self.screen_width - self.rect.width:
                self.direction = 180.0
            elif self.wallHit[0] <= 0:
                self.direction = 0
            print(self.direction)
    
    def detectHit(self):
        x = self.rect.x
        y = self.rect.y
        if x < 0 or x + self.rect.width > self.screen_width or y < 0 or y > self.screen_height:
            self.wallHit = (x,y)
            return
        self.wallHit = None


