import pygame


class Snail(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, images, *groups):
        super().__init__(*groups)
        self.frames = images
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.not_mirrored_image = self.image
        self.mirror_image = pygame.transform.flip(self.image, True, False)
        self.snail_speed = 2
        self.moves = 0
        self.flag = True
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y + 39)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

        if (self.moves // 70) % 2 == 0:
            self.flag = True
            self.image = self.image
        else:
            self.flag = False
            self.image = self.mirror_image

        if self.flag:
            #self.image = self.not_mirrored_image
            self.rect = self.rect.move(-self.snail_speed, 0)
            self.moves += 1
        else:
            #self.image = self.mirror_image
            self.rect = self.rect.move(self.snail_speed, 0)
            self.moves += 1

    def frame_change(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
