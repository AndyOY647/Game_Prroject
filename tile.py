import pygame

from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type,surface = pygame.Surface((tile_size,tile_size))):  # default surface
        super().__init__(groups)
        # tile image ID+1 because spritesheet ID starts at 1 not 0
        self.image = surface
          # Rect with the full size of the entire image
        self.sprite_type = sprite_type
        if sprite_type == 'house':
            self.rect = self.image.get_rect(topleft = (pos[0]-tile_size*0.1, pos[1] - tile_size*2.65))
        elif sprite_type == 'tree':
                self.rect = self.image.get_rect(topleft=(pos[0] + tile_size *0.5, pos[1] - tile_size * 1.5))
        else:
            self.rect = self.image.get_rect(topleft=pos)
        # hitbox is needed for any overlapping in the game
        # Code below change the size of the rect used for the image
        # Hitbox is smaller than the drawing box by shrinking 5 px top and bottom
        # Still bigger than the character hitbox
        if sprite_type == 'house':
            self.hitbox = self.rect.inflate(-48,-100)
        elif sprite_type == 'flower':
            self.hitbox = self.rect.inflate(-20,-20)
        else:
            self.hitbox = self.rect.inflate(-30, -30)


