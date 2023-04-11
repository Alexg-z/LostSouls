import pygame as py
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *

class Level:
    def __init__(self):

        # Display surfaces
        self.display_surface = py.display.get_surface()

        # Sprite set up
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = py.sprite.Group()

        # Sprite set up
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('./map/map_FloorBlocks.csv')
        }

        for style,layout in layouts.items():
            for row_index,row in enumerate(WORLD_MAP):
                for col_index, col in enumerate(row):
                    x = col_index * TILESIZE 
                    y = row_index * TILESIZE
                if style == 'boundary':
                        Tile((x,y),[self.visible_sprites,self.obstacles_sprites],'invisible')
        #         if col == 'x':
        #             Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
        #         if col == 'p':
        #             self.player = Player((x,y),[self.visible_sprites],self.obstacles_sprites)
        self.player = Player((2000,1430),[self.visible_sprites],self.obstacles_sprites)

    def run(self):
        # Update & draw
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        

class YSortCameraGroup(py.sprite.Group):
    def __init__(self):
        # general set up
        super().__init__()
        self.display_surface = py.display.get_surface()
        self.half_width =self.display_surface.get_size()[0] // 2
        self.half_height =self.display_surface.get_size()[1] // 2
        self.offset = py.math.Vector2()

        # creating floor
        self.floor_surf = py.image.load('./graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    
    def custom_draw(self,player):

        #Getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)


        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
