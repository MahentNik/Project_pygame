import pygame
import math

JUMP_POWER = 10
HERO_SPEED = 6
GRAVITY = 0.35
WATER_RESISTANCE = TO_GRAVITY, TO_SPEED = (0.3, 4.5)  # сопротивление движения в воде


# потом следует вычислять эти параметры в процентах (пока так)


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tile_width, tile_height, hero_im, *groups):
        super().__init__(groups)
        self.image = hero_im
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)

        # статы
        self.vx = 0
        self.vy = 0
        self.on_Ground = False

        self.special_items = {  # (1 показатель - найден предмет или нет) (2 показатель - активирован или нет)
            # (3 показатель - откатился ли == готов к использованию)
            1: [False, False, False],
            2: [False, False, False],
            3: [False, False, False]
        }

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
                    self.rect.top = tile.rect.bottom
                    self.vy = 0

    def other_collide(self, player, group, status=False):
        return pygame.sprite.spritecollide(player, group, status)

    def update(self, left, right, up, wat_up, wat_down, let_group, water_group, ladder_group, enemy_group,
               coin_group, air_group):
        if not self.other_collide(self, water_group) and not self.other_collide(self, ladder_group):
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
        elif self.other_collide(self, water_group):
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
        elif self.other_collide(self, ladder_group):
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

        """if collide(self, let_group):
            if self.vx < 0:
                self.rect.x += -self.xvel
            elif self.vx > 0:
                self.rect.x += -self.xvel
            if self.vy > 0:
                self.rect.y += -self.yvel
                self.onGround = True
            elif self.vy < 0:
                self.vy = 0"""
    # класс персонажа(игрока)
    # Показатели игрока (думаю они будут зависеть от сложности, но это уже совсем другая история) : 1) HP -- {3~5}
    #                    2) Пузырьки воздуха (этот показатель виден только в воде) {5~7}
    #                    (восполняетс по два пузырька в секунду)
    #                    3) Счетчик монет (от 0 до ...)
    #                    4) ...
    # еще один вопрос - будет ли наш персонаж атаковать? (можно убрать эту возможность) опять же по времени
