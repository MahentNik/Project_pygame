import os
import pygame
import pytmx
from load_image import load_image
from snail import Snail
from fish import Fish
from player import Hero
from camera import Camera
from hud import Hud
from items import Rune
from spike import Spike
from tiles import *
from special_block import SpecialBlock
from pause_menu import PauseMenu
from menu_cycle import menu_cycle
from pause_cycle import pause_cycle
from end_screen import EndScreen

# основные переменные
WINDOW_SIZE = WIDTH, HEIGHT = 1300, 800
FPS = 60
RELOAD_HIT = pygame.USEREVENT + 76  # перезарядка получения урона
RELOAD_o2 = pygame.USEREVENT + 77  # перезарядка получения кислорода
RELOAD__o2 = pygame.USEREVENT + 78  # перезарядка отнимания кислорода
REPEAT_MUSIC = pygame.USEREVENT + 1
RUNE_MOVES = pygame.USEREVENT + 99
RELOAD__05 = pygame.USEREVENT + 111

difficult = {"Easy": (6, 6),
             "Medium": (4, 6),
             "Hard": (2, 5)
             }

dir_levels = ["first_level.tmx", "second_level.tmx"]

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
    "--k-k-k-   w   -k- l     S",
    "-                  l     S",
    "-  r           s    -ww- -",
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
    fullname = os.path.join('levels', name_level)
    level = pytmx.load_pygame(f'{fullname}')
    for y in range(level.height):
        for x in range(level.width):
            im_1layer = level.get_tile_image(x, y, 0)
            im_2layer = level.get_tile_image(x, y, 1)
            id1 = level.tiledgidmap[level.get_tile_gid(x, y, 0)]
            id2 = level.tiledgidmap[level.get_tile_gid(x, y, 1)]
            if id1 == 159:
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                hero = Hero(x, y, tile_width, tile_height, images[0], images[7], special_block_group, coin_group,
                            coin_box_group,
                            all_sprites, hero_group, all_sprites)
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
            elif level[y][x] == '-':
                Ground(x, y, tile_width, tile_height, images[1], let_group, ground_group, all_sprites)
            elif level[y][x] == '@':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                hero = Hero(x, y, tile_width, tile_height, images[0], images[7], special_block_group, coin_group,
                            coin_box_group,
                            all_sprites, hero_group, all_sprites)
            elif level[y][x] == 'w':
                Water(x, y, tile_width, tile_height, images[5], water_group, all_sprites)
            elif level[y][x] == 'l':
                Ladder(x, y, tile_width, tile_height, images[4], ladder_group, all_sprites)
            elif level[y][x] == "k":
                CoinBox(x, y, tile_width, tile_height, images[6], let_group, coin_box_group, air_group, all_sprites)
            elif level[y][x] == 's':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                Snail(x, y, tile_width, tile_height, images[2], enemy_group, all_sprites)
            elif level[y][x] == 'f':
                Water(x, y, tile_width, tile_height, images[5], water_group, all_sprites)
                Fish(x, y, tile_width, tile_height, images[3], enemy_group, all_sprites)
            elif level[y][x] == 'd':
                Spike(x, y, tile_width, tile_height, images[8], spikes_group, all_sprites)
            elif level[y][x] == "r":
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                Rune(x, y, tile_width, tile_height, images[-2], rune_group, all_sprites)
            elif level[y][x] == "S":
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                SpecialBlock(x, y, tile_width, tile_height, images[-1], let_group, special_block_group, all_sprites)
    return hero, x, y


def get_images():
    end_game_im = load_image("end_screen.png")
    hero_im = load_image('p1_stand.png', -1)
    brick = load_image('brickWall.png', -1)
    snail_image = load_image('snailWalk1.png', -1)
    fish_image = load_image('fishSwim1.png', -1)
    ladder_image = load_image('ladder_mid.png', -2)
    water_image = load_image('liquidWater.png')
    coin_box = load_image("boxCoin.png", -1)
    coin_im = load_image("coinGold1.png", -1)
    spike_im = load_image('spikes.png', -1)
    rune_im = load_image("rune.png", -1)
    special = load_image("special.png", -1)
    images = [hero_im, brick, snail_image, fish_image, ladder_image, water_image, coin_box, coin_im, spike_im, rune_im,
              special]
    for_hud = [load_image("no_hp.png", -1), load_image("half_hp.png", -1), load_image("hp.png", -1),
               load_image("o2.png"), coin_im]
    numbers = load_image("hud_0.png", -1), load_image("hud_1.png", -1), load_image("hud_2.png", -1), load_image(
        "hud_3.png", -1), load_image("hud_4.png", -1), load_image("hud_5.png", -1), load_image("hud_6.png", -1), \
              load_image("hud_7.png", -1), load_image("hud_8.png", -1), load_image("hud_9.png", -1)
    return end_game_im, images, for_hud, numbers


def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    clock = pygame.time.Clock()

    # музыка
    pygame.mixer.music.load('data/song.ogg')
    pygame.mixer.music.play()
    pygame.time.set_timer(REPEAT_MUSIC, 60000)

    # загрузка меню
    dif = menu_cycle(clock, FPS, WINDOW_SIZE, screen)

    # загрузка картинок
    end_game_im, images, for_hud, numbers = get_images()

    hero, level_x, level_y = create_level(dir_levels[0], images)
    hud = Hud(*difficult[dif], hero, 0, 0, for_hud, numbers, hud_group, all_sprites)
    camera = Camera((level_x, level_y), WIDTH, HEIGHT)

    is_left = is_right = False
    up = False
    wat_up = False
    wat_down = False
    is_paused = False
    running = True

    # timers
    pygame.time.set_timer(RUNE_MOVES, 140)
    while running:

        may_get_damaged = False  # перезарядка получения урона
        is_time_o2 = False  # перезарядка получения кислорода
        is_time__o2 = False  # перезарядка отнимания кислорода
        is_time__05 = False
        rune_event = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == REPEAT_MUSIC:
                pygame.mixer.music.play()
            if event.type == RELOAD__05:
                is_time__05 = True
            if event.type == RUNE_MOVES:
                rune_event = True
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
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    is_paused = not is_paused
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

        if not is_paused:
            camera.update(hero)

            for sprite in all_sprites:
                camera.apply(sprite)

            hero.update(is_left, is_right, up, wat_up, wat_down, let_group, water_group, ladder_group, enemy_group,
                        coin_group, air_group, coin_box_group, rune_group)
            hud.update(water_group, enemy_group, coin_group, air_group, spikes_group, may_get_damaged,
                       is_time_o2, is_time__o2, is_time__05)
            hero_status = hud.hero_status()

            if rune_event:
                rune_group.update()

            enemy_group.update()
            coin_group.update(ground_group)
        else:
            pause_cycle(clock, FPS, WINDOW_SIZE, screen)
            is_paused = False
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
        rune_group.draw(screen)
        special_block_group.draw(screen)
        hud_group.draw(screen)

        if hero_status:
            pygame.mixer.music.pause()
            end_game_screen = EndScreen(end_game_im, screen, clock, FPS)
            end_game_screen.create_screen()
            running = False
            for i in all_sprites:
                i.kill()
            main()
        pygame.display.flip()
        clock.tick(FPS)


special_block_group = pygame.sprite.Group()
rune_group = pygame.sprite.Group()
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
