import pygame
from math import sin, cos, radians
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
        self.direction = random.randint(0,16) * 22.5

    def moveDown(self):
        pass

    def update(self):
        self.detectHit()

        if not self.wallHit == None:
            self.direction += 90
            if self.direction > 360:
                self.direction -= 360


        self.move()
    
    def move(self):
        self.rect.x += cos(radians(self.direction)) * self.speed
        self.rect.y -= sin(radians(self.direction)) * self.speed

    def detectHit(self):
        x = self.rect.x
        y = self.rect.y
        if x < 0 or x + self.rect.width > self.screen_width or y < 0 or y + self.rect.height > self.screen_height:
            self.wallHit = (x,y)
            # consider adding sound effect here
            return
        self.wallHit = None


