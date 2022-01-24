import pygame


# класс рыбы
class Fish(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, image, *groups):
        super().__init__(*groups)
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.not_mirrored_image = pygame.transform.flip(self.image, True, False)
        self.mirror_image = self.image
        self.fish_speed = 3
        self.moves = 0
        self.flag = True
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)

    def update(self):
        if (self.moves // 50) % 2 == 0:
            self.flag = True
        else:
            self.flag = False

        if self.flag:
            self.image = self.not_mirrored_image
            self.rect = self.rect.move(self.fish_speed, 0)
            self.moves += 1
        else:
            self.image = self.mirror_image
            self.rect = self.rect.move(-self.fish_speed, 0)
            self.moves += 1
