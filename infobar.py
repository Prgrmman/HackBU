
import pygame
import threading
import subprocess
from pygame.locals import *
from text import Text



class HUD(object):

    def __init__(self, screen):
        self.screen = screen
        self.bgColor = (150, 150, 150)
        self.height = 70 # height above bottom (y = 960)
        self.scoreText= Text(0,890, str(0), 100)
        self.text = "hello"
        self.randomBar = Text(150, 920, self.text, 40)

    def updateScore(self, score):
        self.scoreText.changeText(str(score))

        def runBot():
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


            self.text = out

        thread = threading.Thread(target = runBot)
        thread.start()
        self.randomBar.changeText(self.text)

    def draw(self):
        self.screen.blit(self.scoreText.image, self.scoreText.rect)
        self.screen.blit(self.randomBar.image, self.randomBar.rect)



