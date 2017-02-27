
import pygame
import threading
#import subprocess
from pygame.locals import *
from text import Text
import random


class HUD(object):

    def __init__(self, screen):
        displayWidth = screen.get_width()
        displayHeight = screen.get_height()
        self.screen = screen
        self.bgColor = (150, 150, 150)
        self.height = (displayHeight * 7) / 100
        self.scoreText= Text(0,(0.9*displayHeight), str(0), (displayHeight / 15) )
        self.text = "hello"
        self.randomBar = Text((0.2*displayWidth),(0.9*displayHeight), self.text, (displayHeight / 20))

    def updateScore(self, score):
        self.scoreText.changeText(str(score))

        def runBot():
            out = "default nonsense text"
            if(random.random() > 0.5):
                out = "Supremely delicious rice-a-roni paellas!"
            else:
                out = "Colorless green thoughts sleep furiously!"
            # The fortune command isn't available on Windows!
            # Find another way to generate random strings
            """
            p = subprocess.Popen(['fortune', ''], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            out = str(out)
            out = out.replace("\"", '')
            out = out.replace("\\n", '')
            out = out.replace("\\t", '')
            out = ''.join([char for char in out if char.isalnum() or char == ' ' or char in ".,?!"])
            out = out[1:]
            end = out.find('.')
            out = out[0:end]
            if len(out) > 70:
                out = out[0:70]
                out += "..."

            """
            self.text = out

        thread = threading.Thread(target = runBot)
        thread.start()
        self.randomBar.changeText(self.text)

    def draw(self):
        self.screen.blit(self.scoreText.image, self.scoreText.rect)
        self.screen.blit(self.randomBar.image, self.randomBar.rect)



