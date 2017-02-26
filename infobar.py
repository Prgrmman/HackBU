
import pygame
from pygame.locals import *
from text import Text
from chatterbot import ChatBot


class HUD(object):

    def __init__(self, screen):
        self.screen = screen
        self.bgColor = (150, 150, 150)
        self.height = 70 # height above bottom (y = 960)
        self.scoreText= Text(0,890, str(0))
        self.text = "hello"
        self.randomBar = Text(500, 890, self.text)
        self.chatbot = ChatBot('Ron Obious', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
        self.chatbot.train("chatterbot.corpus.english")

    def updateScore(self, score):
        self.scoreText.changeText(str(score))
    def draw(self):
        self.screen.blit(self.scoreText.image, self.scoreText.rect)
        self.screen.blit(self.randomBar.image, self.randomBar.rect)



