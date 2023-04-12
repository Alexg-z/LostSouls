import pygame as py
from settings import *

class Tile(py.sprite.Sprite):
    def __init__(self,pos,groups,sprite_type,surface = py.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.sprites_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            # offset
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10) #change the size of the tile