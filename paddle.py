import pygame
from gameobj import GameObject
from pygame.locals import *
from math import sin, radians

#This is a paddle object
class Paddle(GameObject):
    def __init__(self, x, y, size):
        GameObject.__init__(self)
        self.image = pygame.image.load('assets/paddle.gif').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x + 1
        self.rect.y = y
        self.speed = 3; #need to change this according to how fast we want paddle to move
        self.screen_width =  size[0]
        self.screen_height = size[1]
        self.direction = 0

    def update(self):
        pass

    def move(self, upordown):
        if upordown == 'up':
            self.direction = 90
        elif upordown == 'down':
            self.direction = 270
        self.rect.y -= sin(radians(self.direction)) * self.speed
