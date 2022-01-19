import os
import pygame
from load_image import load_image
from snail import Snail
from fish import Fish
from player import Hero
from camera import Camera
from hud import Hud
from items import Coin
from spike import Spike
from tiles import *

# основные переменные
WINDOW_SIZE = WIDTH, HEIGHT = 1600, 800
FPS = 60

RELOAD_HIT = pygame.USEREVENT + 76  # перезарядка получения урона
RELOAD_o2 = pygame.USEREVENT + 77  # перезарядка получения кислорода
RELOAD__o2 = pygame.USEREVENT + 78  # перезарядка отнимания кислорода
REPEAT_MUSIC = pygame.USEREVENT + 1
FRAME_CHANGE = pygame.USEREVENT + 2

tile_width = tile_height = 70
PRIMITIVE_LEVEL = [
    "------------------   -----",
    "-          w      kkk    -",
    "-          w      kkk    -",
    "-   @      w    s        -",
    "-      kkk w -----lll-   -",
    "-          w       l     -",
    "-          w       l     -",
    "-      --- w       l    k-",
    "- dd       w       l    k-",
    "--k-k-k-   w   -k- l     -",
    "-                  l     -",
    "-              s    -ww- -",
    "---------------------ww---",
    "-wwwww-  -wwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwfwwwwwwwww-",
    "-wwwwfwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwww---wwwwwwwwwwww-",
    "-wwwwwwwww- -wwwwwfwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwwfwwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "--------------------------",
]


def create_level(name_level, images):
    for y in range(len(name_level)):
        for x in range(len(name_level[y])):
            if name_level[y][x] == ' ':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
            elif name_level[y][x] == '-':
                Ground(x, y, tile_width, tile_height, images[1], let_group, ground_group, all_sprites)
            elif name_level[y][x] == '@':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                hero = Hero(x, y, tile_width, tile_height, images[0], images[7], coin_group, coin_box_group,
                            all_sprites, hero_group, all_sprites)
            elif name_level[y][x] == 'w':
                Water(x, y, tile_width, tile_height, images[5], water_group, all_sprites)
            elif name_level[y][x] == 'l':
                Ladder(x, y, tile_width, tile_height, images[4], ladder_group, all_sprites)
            elif name_level[y][x] == "k":
                CoinBox(x, y, tile_width, tile_height, images[6], let_group, coin_box_group, air_group, all_sprites)
            elif name_level[y][x] == 's':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                Snail(x, y, tile_width, tile_height, images[2], enemy_group, all_sprites)
            elif name_level[y][x] == 'f':
                Water(x, y, tile_width, tile_height, images[5], water_group, all_sprites)
                Fish(x, y, tile_width, tile_height, images[3], enemy_group, all_sprites)
            elif name_level[y][x] == 'd':
                Spike(x, y, tile_width, tile_height, images[8], spikes_group, all_sprites)
    return hero, x, y


def get_images():
    jump_im = load_image('p1_jump.png', -1)
    walk_im = load_image('p1_walk11.png', -1)
    stand_im = load_image('p1_stand.png', -1)
    brick = load_image('brickWall.png', -1)
    snail_image = load_image('snailWalk1.png', -1)
    fish_image = load_image('fishSwim1.png', -1)
    ladder_image = load_image('ladder_mid.png', -2)
    water_image = load_image('liquidWater.png')
    coin_box = load_image("boxCoin.png", -1)
    coin_im = load_image("coinGold1.png", -1)
    spike_im = load_image('spikes.png', -1)
    hero_images = [stand_im, jump_im, walk_im]
    images = [hero_images, brick, snail_image, fish_image, ladder_image, water_image, coin_box, coin_im, spike_im]
    for_hud = [load_image("no_hp.png", -1), load_image("half_hp.png", -1), load_image("hp.png", -1),
               load_image("o2.png"), coin_im]
    numbers = load_image("hud_0.png", -1), load_image("hud_1.png", -1), load_image("hud_2.png", -1), load_image(
        "hud_3.png", -1), load_image("hud_4.png", -1), load_image("hud_5.png", -1), load_image("hud_6.png", -1), \
        load_image("hud_7.png", -1), load_image("hud_8.png", -1), load_image("hud_9.png", -1)
    return images, for_hud, numbers


def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    # музыка
    pygame.mixer.music.load('data/song.ogg')
    # pygame.mixer.music.play()

    # загрузка картинок
    images, for_hud, numbers = get_images()

    clock = pygame.time.Clock()
    hero, level_x, level_y = create_level(PRIMITIVE_LEVEL, images)
    hud = Hud(hero, 0, 0, for_hud, numbers, hud_group, all_sprites)
    camera = Camera((level_x, level_y), WIDTH, HEIGHT)
    is_left = is_right = False
    up = False
    wat_up = False
    wat_down = False

    running = True
    while running:
        may_get_damaged = False  # перезарядка получения урона
        is_time_o2 = False  # перезарядка получения кислорода
        is_time__o2 = False  # перезарядка отнимания кислорода

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == REPEAT_MUSIC:
                pass
                pygame.mixer.music.play()
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
            if event.type == RELOAD_o2:
                is_time_o2 = True
            if event.type == RELOAD__o2:
                is_time__o2 = True
        camera.update(hero)

        for sprite in all_sprites:
            camera.apply(sprite)

        hero.update(is_left, is_right, up, wat_up, wat_down, let_group, water_group, ladder_group, enemy_group,
                    coin_group, air_group, coin_box_group, spikes_group, may_get_damaged)
        hud.update(water_group, enemy_group, coin_group, air_group, spikes_group, may_get_damaged,
                   is_time_o2, is_time__o2)

        enemy_group.update()
        coin_group.update(ground_group)
        screen.fill((218, 187, 253))
        ladder_group.draw(screen)
        water_group.draw(screen)
        spikes_group.draw(screen)
        air_group.draw(screen)
        hero_group.draw(screen)
        ground_group.draw(screen)
        coin_box_group.draw(screen)
        coin_group.draw(screen)
        enemy_group.draw(screen)
        hud_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


coin_box_group = pygame.sprite.Group()  # если монеты будут просто спавниться на земле то эта группа не нужна
# это является и препятствием и отдельной группой
ground_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
air_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
let_group = pygame.sprite.Group()  # стены
ladder_group = pygame.sprite.Group()
spikes_group = pygame.sprite.Group()
items_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
hud_group = pygame.sprite.Group()

if __name__ == '__main__':
    main()
