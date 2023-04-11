import pygame as py
from settings import *

class Tile(py.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = py.image.load('./graphics/test/rock2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)