import pygame


class Items(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, *groups):
        pass
    # класс предметов которые жат на земле
    # их можно подобрать


class Coin(Items):
    pass
    # класс монета


class Gun(Items):
    pass
    # класс оружия (если успеем)


class Rune(Items):
    pass
    # класс руны которая делает тебя невоспреимчивым к урону на 5 сек (кулдаун 25 сек)
    # или дает тебе возможность пройти через тайную текстуру class Secret
