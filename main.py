import os
import pygame
from player import Hero
from air import Air
from ground import Ground
from water import Water
from ladder import Ladder
from camera import Camera
from hud import Hud

# основные переменные
WINDOW_SIZE = WIDTH, HEIGHT = 1600, 800
FPS = 60
RELOAD_HIT = pygame.USEREVENT + 76  # перезарядка получения урона
RELOAD_o2 = pygame.USEREVENT + 77  # перезарядка получения кислорода
RELOAD__o2 = pygame.USEREVENT + 78  # перезарядка отнимания кислорода

tile_width = tile_height = 70
PRIMITIVE_LEVEL = [
    "--------------------------",
    "-          w             -",
    "-          w             -",
    "-   @      w             -",
    "-          w ------l--   -",
    "-          w       l     -",
    "-          w       l     -",
    "-          w       l     -",
    "-          w       l     -",
    "-          w   --- l     -",
    "-w        www      l     -",
    "-                   -ww- -",
    "------ww-------------ww---",
    "-wwwww-  -wwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwww---wwwwwwwwwwww-",
    "-wwwwwwwww- -wwwwwwwwwwww- ",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "--------------------------",

]


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


def create_level(name_level, hero_im, brick, air_im=None, water_im=None,
                 ladder_im=None):  # потом следует изменить отправление текстур (если будет несколько уровней)
    for y in range(len(name_level)):
        for x in range(len(name_level[y])):
            if name_level[y][x] == ' ':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
            elif name_level[y][x] == '-':
                Ground(x, y, tile_width, tile_height, brick, let_group, all_sprites)
            elif name_level[y][x] == '@':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                hero = Hero(x, y, tile_width, tile_height, hero_im, hero_group, all_sprites)
            elif name_level[y][x] == 'w':
                Water(x, y, tile_width, tile_height, water_group, all_sprites)
            elif name_level[y][x] == 'l':
                Ladder(x, y, tile_width, tile_height, ladder_group, all_sprites)
    return hero, x, y


def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    # загрузка картинок
    hero_im = load_image('p1_stand.png')
    brick = load_image("brickWall.png")
    no_hp_im = load_image("no_hp.png", -1)
    half_hp_im = load_image("half_hp.png", -1)
    hp_im = load_image("hp.png", -1)
    o2_im = load_image("o2.png")
    coin_im = load_image("coin.png", -1)
    numbers = load_image("hud_0.png"), load_image("hud_1.png"), load_image("hud_2.png"), load_image(
        "hud_3.png"), load_image("hud_4.png"), load_image("hud_5.png"), load_image("hud_6.png"), load_image(
        "hud_7.png"), load_image("hud_8.png"), load_image("hud_9.png")

    clock = pygame.time.Clock()
    hero, level_x, level_y = create_level(PRIMITIVE_LEVEL, hero_im, brick)
    camera = Camera((level_x, level_y), WIDTH, HEIGHT)
    hud = Hud(hero, 0, 0, no_hp_im, half_hp_im, hp_im, o2_im, coin_im, numbers, hud_group, all_sprites)

    is_left = is_right = False
    up = False
    wat_up = False
    wat_down = False

    running = True
    while running:
        may_get_damaged = True  # перезарядка получения урона
        first_damage = True

        timer_off_hp = False
        timer_off_o2 = False
        timer_off__o2 = False

        is_time_o2 = False  # перезарядка получения кислорода
        is_time__o2 = False  # перезарядка отнимания кислорода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    up = True
                if event.key == pygame.K_UP:
                    wat_up = True
                elif event.key == pygame.K_DOWN:
                    wat_down = True
                if event.key == pygame.K_LEFT:
                    is_left = True
                elif event.key == pygame.K_RIGHT:
                    is_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    up = False
                if event.key == pygame.K_UP:
                    wat_up = False
                elif event.key == pygame.K_DOWN:
                    wat_down = False
                if event.key == pygame.K_RIGHT:
                    is_right = False
                elif event.key == pygame.K_LEFT:
                    is_left = False
            if event.type == RELOAD_HIT:
                may_get_damaged = True
                first_damage = False
            if event.type == RELOAD_o2:
                is_time_o2 = True
            if event.type == RELOAD__o2:
                is_time__o2 = True
        camera.update(hero)

        for sprite in all_sprites:
            camera.apply(sprite)

        hero.update(is_left, is_right, up, wat_up, wat_down, let_group, water_group, ladder_group, enemy_group,
                    coin_group, air_group
                    )
        hud.update(water_group, enemy_group, coin_group, air_group, may_get_damaged, first_damage,
                   is_time_o2, is_time__o2)
        screen.fill("Black")
        ladder_group.draw(screen)
        water_group.draw(screen)
        air_group.draw(screen)
        hero_group.draw(screen)
        let_group.draw(screen)
        hud_group.draw(screen)
        if hud.reload_first_damage():
            first_damage = True

        pygame.display.flip()
        clock.tick(FPS)


pygame.quit()

coin_box_group = pygame.sprite.Group()  # если монеты будут просто спасниться на земле то эта группа не нужна
# это является и препятствием и отдельной группой
coin_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
air_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
let_group = pygame.sprite.Group()  # стены
ladder_group = pygame.sprite.Group()
items_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
hud_group = pygame.sprite.Group()

if __name__ == '__main__':
    main()
