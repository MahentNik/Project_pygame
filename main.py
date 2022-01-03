import os
import pygame
from hero import Hero
from air import Air
from ground import Ground

# основные переменные
WINDOW_SIZE = WIDTH, HEIGHT = 1600, 800
FPS = 60
JUMP_POWER = 10
HERO_SPEED = 6
GRAVITY = 0.35

tile_width = tile_height = 70
PLATFORM_COLOR = "#FF6262"
PRIMITIVE_LEVEL = [
    "---------------------",
    "-                   -",
    "-                   -",
    "-   @               -",
    "-            --     -",
    "-                   -",
    "-                   -",
    "-                   -",
    "-                   -",
    "-              --   -",
    "-                   -",
    "---------------------"]


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


# загрузка картинок
hero_im = load_image('p1_stand.png')
brick = load_image("brickWall.png")


def create_level(name_level):
    for y in range(len(name_level)):
        for x in range(len(name_level[y])):
            if name_level[y][x] == ' ':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
            elif name_level[y][x] == '-':
                Ground(x, y, tile_width, tile_height, brick, let_group, all_sprites)
            elif name_level[y][x] == '@':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                hero = Hero(x, y, tile_width, tile_height, hero_im, hero_group, all_sprites)
    return hero


def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    clock = pygame.time.Clock()
    hero = create_level(PRIMITIVE_LEVEL)
    is_left = is_right = False
    up = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    up = True
                if event.key == pygame.K_LEFT:
                    is_left = True
                elif event.key == pygame.K_RIGHT:
                    is_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    up = False
                if event.key == pygame.K_RIGHT:
                    is_right = False
                elif event.key == pygame.K_LEFT:
                    is_left = False
        hero.update(is_left, is_right, up)
        screen.fill("Black")
        air_group.draw(screen)
        hero_group.draw(screen)
        let_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
air_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
let_group = pygame.sprite.Group()  # стены
ladder_group = pygame.sprite.Group()
items_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

if __name__ == '__main__':
    main()
