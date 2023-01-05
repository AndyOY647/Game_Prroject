import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *


class Level:
    def __init__(self):
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        layout = {

            'little_decor': import_csv_layout('csv/map_little decor.csv'),
            'object': import_csv_layout('csv/map_house&trees.csv')
        }
        graphics ={
            'object': import_folder('images/other')
        }
        print(graphics)
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * tile_size
                        y = row_index * tile_size
                    if style == 'object':
                        surf = graphics['object'][int(col)]
                        Tile((x,y), [self.visible_sprites,self.obstacle_sprites],'object',surf )
                        print(col)
                # if col == 'x':
                #     Tile((x,y), [self.visible_sprites,self.obstacle_sprites])
                # if col == 'p':
        self.player = Player((144, 220),[self.visible_sprites], self.obstacle_sprites)

    def run(self):
        #update and draw
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)


class YsortCameraGroup(pygame.sprite.Group):  # camera following the character
    def __init__(self):
        #  setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surface = pygame.image.load('images/map/map.png').convert_alpha()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))




    def custom_draw(self, player):

        #  getting the offset
        self.offset.x = player.rect.centerx - self.half_width  # without subtracting the half_width and half_height
        self.offset.y = player.rect.centery - self.half_height  # the whole map will be moving

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)