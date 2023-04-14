import pygame as py
import sys
from settings import *
from level import Level

class Game:
	def __init__(self):

		# general setup
		py.init()
		self.screen = py.display.set_mode((WIDTH,HEIGTH))
		py.display.set_caption('Lost Souls')
		self.clock = py.time.Clock()

		self.level = Level()
	
	def run(self):
		while True:
			for event in py.event.get():
				if event.type == py.QUIT:
					py.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			py.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()