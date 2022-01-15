import pygame


class Spike(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((tile_width, tile_height), pygame.SRCALPHA, 32)
        self.points = [[pos_x, pos_y + tile_height], [pos_x + tile_width // 2, pos_y],
                       [pos_x + tile_width, pos_y + tile_height]]
        pygame.draw.polygon(self.image, pygame.Color("red"), self.points)
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
