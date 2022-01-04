import pygame


class Water(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tile_width, tile_height, *groups):
        super().__init__(groups)
        self.image = pygame.Surface((tile_width, tile_height))
        self.image.fill("Blue")
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
    # это класс воды (есть рыбы - есть вода, значит персонаж может попасть в воду)
    # у воды есть свои особенности:
    # В ней персонаж будет медленней,
    # Также персонаж может как погружаться на дно так и всплывать,
    # И когда он погружен в воду у него тратится показатель воздуха.
