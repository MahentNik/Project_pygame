import pygame


class Air(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tile_width, tile_height, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((tile_width, tile_height))
        self.image.fill(pygame.Color(117, 238, 253))
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
