import pygame
import random

gravity = 0.25


class Items(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
    # класс предметов которые лежат на земле
    # их можно подобрать


class Coin(Items):
    def __init__(self, x, y, coin_im, *groups):
        super().__init__(*groups)
        self.image = coin_im
        self.rect = self.image.get_rect().move(x, y - 70)

        self.gravity = gravity

        num1 = range(-3, 3)
        num2 = range(-3, -1)

        self.vx = random.choice(num1)
        self.vy = random.choice(num2)

    def update(self, ground_group):
        if not collide(self, ground_group):
            self.vy += self.gravity
            self.rect.x += self.vx
            self.rect.y += self.vy
        else:
            self.vx, self.vy = 0, 0

    # класс монета


class Gun(Items):
    pass
    # класс оружия (если успеем)


class Rune(Items):
    pass
    # класс руны которая делает тебя невоспреимчивым к урону на 5 сек (кулдаун 25 сек)
    # или дает тебе возможность пройти через тайную текстуру class Secret


def collide(player, group, status=False):
    return pygame.sprite.spritecollide(player, group, status)
