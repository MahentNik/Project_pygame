import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups, rect):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect().move(rect[0] * pos[0],
                                               rect[1] * pos[1])