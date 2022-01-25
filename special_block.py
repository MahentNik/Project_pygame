import pygame


class SpecialBlock(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tile_width, tile_height, image,  *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
