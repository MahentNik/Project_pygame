import pygame
from items import Coin

JUMP_POWER = 10
HERO_SPEED = 6
GRAVITY = 0.35
WATER_RESISTANCE = TO_GRAVITY, TO_SPEED = (0.3, 4.5)  # сопротивление движения в воде
# потом следует вычислять эти параметры в процентах (пока так)
HERO_HP = 3
HERO_OXYGEN = 6


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tile_width, tile_height, images, coin_im, coin_group, coin_box_group, all_sprites,
                 *groups):
        super().__init__(*groups)
        self.images = images
        self.image = self.images[0]
        self.mirrored_images = [pygame.transform.flip(frame, True, False) for frame in self.images]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)

        self.groups_for_coin = [coin_group, all_sprites]
        self.coin_im = coin_im
        self.coin_box_group = coin_box_group
        self.coin_group = coin_group

        # статы
        self.vx = 0
        self.vy = 0
        self.on_Ground = False

    def collide(self, vx, vy, lets):
        for tile in lets:
            if pygame.sprite.collide_rect(self, tile):
                if vx > 0:
                    self.rect.right = tile.rect.left
                if vx < 0:
                    self.rect.left = tile.rect.right
                if vy > 0:
                    self.rect.bottom = tile.rect.top
                    self.on_Ground = True
                    self.vy = 0

                if vy < 0:
                    if other_collide(self, self.coin_box_group):
                        sp = other_collide(self, self.coin_box_group, True)
                        for i in sp:
                            x, y = i.rect.x, i.rect.y
                            Coin(x, y, self.coin_im, *self.groups_for_coin)
                    self.rect.top = tile.rect.bottom
                    self.vy = 0

    def update(self, left, right, up, wat_up, wat_down, let_group, water_group, ladder_group, enemy_group,
               coin_group, air_group, coin_box_group, spikes_group, may_get_damage):
        if not other_collide(self, water_group) and not other_collide(self, ladder_group):
            self.ground_collide(up, left, right, let_group)
        elif other_collide(self, water_group):
            self.water_collide(wat_up, left, right, let_group)
        elif other_collide(self, ladder_group):
            self.ladder_collide(wat_up, wat_down, left, right, let_group)
        if other_collide(self, enemy_group) or other_collide(self, spikes_group):
            self.enemy_collide(enemy_group, spikes_group, let_group)

    # смена кадров
    def frame_changes(self, left, right):
        cur_frame = 0
        if left:
            cur_images = self.mirrored_images
        else:
            cur_images = self.images

        if self.on_Ground and not (left or right):
            self.image = cur_images[0]
        elif self.on_Ground and (left or right):
            cur_frame = (cur_frame + 1) % len(cur_images)
            self.image = cur_images[:2][cur_frame]
        else:
            self.image = cur_images[2]

    # столкновения с врагами
    def enemy_collide(self, enemy_group, spikes_group, let_group):
        sp = other_collide(self, spikes_group) + other_collide(self, enemy_group)
        for sprite in sp:
            if pygame.sprite.collide_mask(self, sprite):
                point = pygame.sprite.collide_mask(sprite, self)
                print(point)
                if point[0] < sprite.rect.width // 2:
                    self.vx = -15
                else:
                    self.vx = 15
                self.vy = -5

        self.rect.y += self.vy
        self.collide(0, self.vy, let_group)

        self.rect.x += self.vx
        self.collide(self.vx, 0, let_group)

    # столкновения с землей
    def ground_collide(self, up, left, right, let_group):
        if up:
            if self.on_Ground:
                self.vy = -JUMP_POWER
        if left:
            self.vx = -HERO_SPEED
        elif right:
            self.vx = HERO_SPEED
        if not (left or right):
            self.vx = 0
        if not self.on_Ground:
            self.vy += GRAVITY

        self.on_Ground = False

        self.rect.y += self.vy
        self.collide(0, self.vy, let_group)

        self.rect.x += self.vx
        self.collide(self.vx, 0, let_group)

    # столкновения с лестницами
    def ladder_collide(self, wat_up, wat_down, left, right, let_group):
        if wat_up:
            self.vy = -HERO_SPEED
        if wat_down:
            self.vy = HERO_SPEED
        if left:
            self.vx = -HERO_SPEED
        elif right:
            self.vx = HERO_SPEED
        if not (wat_up or wat_down):
            self.vy = 0
        if not (left or right):
            self.vx = 0

        self.rect.y += self.vy
        self.collide(0, self.vy, let_group)

        self.rect.x += self.vx
        self.collide(self.vx, 0, let_group)

    # столкновения с водой
    def water_collide(self, wat_up, left, right, let_group):
        self.vy += (GRAVITY - TO_GRAVITY)
        if wat_up:
            self.vy = -(HERO_SPEED - TO_SPEED)
        if left:
            self.vx = -(HERO_SPEED - TO_SPEED)
        elif right:
            self.vx = (HERO_SPEED - TO_SPEED)
        if not (left or right):
            self.vx = 0
        self.rect.y += self.vy
        self.collide(0, self.vy, let_group)

        self.rect.x += self.vx
        self.collide(self.vx, 0, let_group)

    # класс персонажа(игрока)
    # Показатели игрока (думаю они будут зависеть от сложности, но это уже совсем другая история) : 1) HP -- {3~5}
    #                    2) Пузырьки воздуха (этот показатель виден только в воде) {5~7}
    #                    (восполняетс по два пузырька в секунду)
    #                    3) Счетчик монет (от 0 до ...)
    #                    4) ...
    # еще один вопрос - будет ли наш персонаж атаковать? (можно убрать эту возможность) опять же по времени


def other_collide(player, group, status=False):
    return pygame.sprite.spritecollide(player, group, status)
