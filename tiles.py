import pygame


# класс плитки
class Tile(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((tile_width, tile_height))
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


# класс воздуха
class Air(Tile):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, *groups):
        super().__init__(pos_x, pos_y, tile_width, tile_height, *groups)
        self.image.fill(pygame.Color(218, 187, 253))


# класс земли и стен
class Ground(Tile):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, image, *groups):
        super().__init__(pos_x, pos_y, tile_width, tile_height, *groups)
        self.image = image


# класс воды
class Water(Tile):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, image, *groups):
        super().__init__(pos_x, pos_y, tile_width, tile_height, *groups)
        self.image = image


# класс лестницы
class Ladder(Tile):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, image, *groups):
        super().__init__(pos_x, pos_y, tile_width, tile_height, *groups)
        self.image = image


# класс ящика с монетой
class CoinBox(Tile):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, image, *groups):
        super().__init__(pos_x, pos_y, tile_width, tile_height, *groups)
        self.image = image


# класс шипов
class Spike(Tile):

    def __init__(self, pos_x, pos_y, tile_width, tile_height, image, *groups):
        super().__init__(pos_x, pos_y, tile_width, tile_height, *groups)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y + 39)


# класс объектов на фоне
class ForeGround(Tile):
    def __init__(self, pos_x, pos_y, tile_width, tile_height, image, *groups):
        super().__init__(pos_x, pos_y, tile_width, tile_height, *groups)
        self.image = image


# класс фоновых объектов
class BackGround(Tile):
    def __init__(self, pos_x, pos_y, tile_width, tile_height, image, *groups):
        super().__init__(pos_x, pos_y, tile_width, tile_height, *groups)
        self.image = image


# конец уровня
class SpecialBlock(Tile):
    def __init__(self, pos_x, pos_y, tile_width, tile_height, image, *groups):
        super().__init__(pos_x, pos_y, tile_width, tile_height, *groups)
        self.image = image

