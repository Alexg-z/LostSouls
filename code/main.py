import pygame as py
import sys
from settings import *
#from debug import debug

class Game:
    def __init__(self):

        #Configuracion general
        py.init()
        self.screen = py.display.set_mode((WIDTH,HEIGTH))
        self.clock = py.time.Clock()

    def run(self):
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

            self.screen.fill('black')
            #debug('Hello :)')
            py.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()