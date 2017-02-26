
import pygame
from pygame.locals import *

class Text(pygame.sprite.Sprite):

    def __init__(self, x, y, text):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 100)
        self.image = self.font.render(text, 1, (0,0,0))
        self.rect = self.image.get_rect()

    def changeText(self, text):
        self.image = self.font.render(text, 1, (0,0,0))
        self.rect = self.image.get_rect()
    def update(self):
        pass
