
import pygame
from pygame.locals import *

class Text(pygame.sprite.Sprite):

    def __init__(self, x, y, text, size):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", size)
        self.image = self.font.render(text, 1, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def changeText(self, text):
        self.image = self.font.render(text, 1, (0,0,0))
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        pass
