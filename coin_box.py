import pygame


class CoinBox(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_width, tile_height, coin_box_im, *groups):
        super().__init__(groups)
        self.image = coin_box_im
        self.rect = self.image.get_rect().move(tile_width * x,
                                               tile_height * y)