import pygame as py
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        # Display surfaces
        self.display_surface = py.display.get_surface()

        # Sprite set up
        self.visible_sprites = py.sprite.Group()
        self.obstacles_sprites = py.sprite.Group()

        # Sprite set up
        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE 
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacles_sprites)


    def run(self):
        # Update & draw
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)