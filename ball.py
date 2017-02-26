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
        self.hit = None # marks where we hit a wall
        self.direction = random.randint(0,16) * 22.5
        self.angs = [x * 22.5 for x in list(range(0,17))]

    def moveDown(self):
        pass

    def update(self):
        if self.detectHit():
            self.sendHit()
        self.move()
    
    def move(self):
        assert(type(self.direction) is float)
        self.rect.x += cos(radians(self.direction)) * self.speed
        self.rect.y -= sin(radians(self.direction)) * self.speed

    def sendHit(self):
        self.hit = (self.rect.x, self.rect.y)
        changeDirection =  self.getDirection(self.findWall(self.hit)) * 1.0
        self.direction = changeDirection * 1.0
        #if self.direction > 360:
         #   self.direction -= 360

    def detectHit(self):
        x = self.rect.x
        y = self.rect.y
        if x < 0 or x + self.rect.width > self.screen_width or y < 0 or y + self.rect.height > self.screen_height - 70:
            return True
        return False

    def findWall(self,hit):
        x = hit[0]
        y = hit[1]
        if x <= 0:
            return 'left'
        elif x + self.rect.width >= self.screen_width:
            return 'right'
        elif y <= 0:
            return 'top'
        elif y + self.rect.height >= self.screen_height - 70:
            return 'bottom'

    def getDirection(self,wall):
        if wall == 'right':
            print("bottom")
            return self.angs[10]
        if wall == 'left':
            print("bottom")
            return self.angs[13]
        if wall == 'top':
            print("bottom")
            return self.angs[10]
        if wall == 'bottom':
            print("bottom")
            return self.angs[3]
        return self.angs[7]

