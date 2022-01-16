import pygame


class Screen(pygame.sprite.Sprite):

    def __init__(self, groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self):
        if self.rect.x < 0:
            self.rect = self.rect.move(100, 0)
