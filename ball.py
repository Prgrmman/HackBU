import pygame
from pygame.locals import *

# This is a ball object
class Ball:
    def __init__(self):
        self.image = pygame.image.load("cat.gif").convert()
        self.position = (0,0)
    def moveDown(self):
        x = self.position[0]
        y = self.position[1]
        self.position = (x, y+10)
    def scale(self):
        """shrink the image by 5 percent"""
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(0.95 * width), int(0.95 * height)))

