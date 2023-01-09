import pygame

from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type,surface = pygame.Surface((tile_size,tile_size))):  # default surface
        super().__init__(groups)
        # tile image ID+1 because spritesheet ID starts at 1 not 0
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)  # Rect with the full size of the entire image
        self.sprite_type = sprite_type
        # hitbox is needed for any overlapping in the game
        # Code below change the size of the rect used for the image
        # Hitbox is smaller than the drawing box by shrinking 5 px top and bottom
        # Still bigger than the character hitbox
        self.hitbox = self.rect.inflate(0,-23)

