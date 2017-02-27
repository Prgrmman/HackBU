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
        self.speed = 5
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

    def sendHit(self): #fix this for collisions with paddle
        self.hit = (self.rect.x, self.rect.y)
        changeDirection =  self.getDirection(self.findWall(self.hit)) * 1.0
        self.direction = changeDirection * 1.0
        #if self.direction > 360:
         #   self.direction -= 360

    def catHit(self): # reverse direction of cat
        print("Cat Hit")
    def detectHit(self):
        x = self.rect.x
        y = self.rect.y
        if x < 0 or x + self.rect.width > self.screen_width or y < 0 or y + self.rect.height > self.screen_height - 70:
            return True
        return False

    def findWall(self,hit):
        x = hit[0]
        y = hit[1]
        if x < 0:
            return 'left'
        elif x + self.rect.width >= self.screen_width:
            return 'right'
        elif y <= 0:
            return 'top'
        elif y + self.rect.height >= self.screen_height - 70:
            return 'bottom'
        else:
            return 'pad'

    def getDirection(self,wall): #add to change depending on imcoming angle
        angs = self.angs
        if wall == 'right':
            if self.direction == angs[3]:
                return self.angs[5]
            if self.direction == angs[2]:
                return self.angs[6]
            if self.direction == angs[1]:
                return self.angs[7]
            if self.direction == angs[0]:
                return self.angs[7]
            if self.direction == angs[15]:
                return self.angs[9]
            if self.direction == angs[14]:
                return self.angs[10]
            if self.direction == angs[13]:
                return self.angs[11]
            return self.angs[10]
        if wall == 'left' or wall == 'pad':
            if self.direction == angs[5]:
                return self.angs[3]
            if self.direction == angs[6]:
                return self.angs[2]
            if self.direction == angs[7]:
                return self.angs[1]
            if self.direction == angs[8]:
                return self.angs[1]
            if self.direction == angs[9]:
                return self.angs[15]
            if self.direction == angs[10]:
                return self.angs[14]
            if self.direction == angs[11]:
                return self.angs[13]
            return self.angs[0]
        if wall == 'top':
            if self.direction == angs[7]:
                return self.angs[9]
            if self.direction == angs[6]:
                return self.angs[10]
            if self.direction == angs[5]:
                return self.angs[11]
            if self.direction == angs[4]:
                return self.angs[11]
            if self.direction == angs[3]:
                return self.angs[13]
            if self.direction == angs[2]:
                return self.angs[14]
            if self.direction == angs[1]:
                return self.angs[15]
            return self.angs[10]
        if wall == 'bottom':
            if self.direction == angs[9]:
                return self.angs[7]
            if self.direction == angs[10]:
                return self.angs[6]
            if self.direction == angs[11]:
                return self.angs[5]
            if self.direction == angs[12]:
                return self.angs[3]
            if self.direction == angs[13]:
                return self.angs[2]
            if self.direction == angs[14]:
                return self.angs[2]
            if self.direction == angs[15]:
                return self.angs[1]
            return self.angs[3]
        return self.angs[2]

