import pygame
from load_image import load_image
from snail import Snail
from player import Hero
from air import Air
from ground import Ground
from water import Water
from ladder import Ladder
from camera import Camera
from fish import Fish

# основные переменные
WINDOW_SIZE = WIDTH, HEIGHT = 1600, 800
FPS = 60

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
    "-          w   --  l     -",
    "-w        www      l     -",
    "-                s  -ww- -",
    "---------------------ww---",
    "-wwwww-  -wwwwwwwwwwwwwww-",
    "-fwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwwfwwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwww---wwwwwwwwwwww-",
    "-wwwwwwwww- -wwwwwwwwwwww- ",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "-wwwwwwwwwwwwwwwwwwwwwwww-",
    "--------------------------",

]


def create_level(name_level, images, air_im=None, water_im=None,
                 ladder_im=None):  # потом следует изменить отправление текстур (если будет несколько уровней)
    for y in range(len(name_level)):
        for x in range(len(name_level[y])):
            if name_level[y][x] == ' ':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
            elif name_level[y][x] == '-':
                Ground(x, y, tile_width, tile_height, images[1], let_group, all_sprites)
            elif name_level[y][x] == '@':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                hero = Hero(x, y, tile_width, tile_height, images[0], hero_group, all_sprites)
            elif name_level[y][x] == 'w':
                Water(x, y, tile_width, tile_height, images[5], water_group, all_sprites)
            elif name_level[y][x] == 'l':
                Ladder(x, y, tile_width, tile_height, images[4], ladder_group, all_sprites)
            elif name_level[y][x] == 's':
                Air(x, y, tile_width, tile_height, air_group, all_sprites)
                Snail(x, y, tile_width, tile_height, images[2], enemy_group, all_sprites)
            elif name_level[y][x] == 'f':
                Water(x, y, tile_width, tile_height, images[5], water_group, all_sprites)
                Fish(x, y, tile_width, tile_height, images[3], enemy_group, all_sprites)
    return hero, x, y


def main():
    pygame.init()

    pygame.display.set_caption('game')
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.mouse.set_visible(False)

    # музыка
    pygame.mixer.music.load('data/song.ogg')
    pygame.mixer.music.play()

    # загрузка картинок
    hero_im = load_image('p1_stand.png', -1)
    brick = load_image('brickWall.png', -1)
    snail_image = load_image('snailWalk1.png', -1)
    fish_image = load_image('fishSwim1.png', -1)
    ladder_image = load_image('ladder_mid.png', -2)
    water_image = load_image('liquidWater.png')
    images = [hero_im, brick, snail_image, fish_image, ladder_image, water_image]

    clock = pygame.time.Clock()
    hero, level_x, level_y = create_level(PRIMITIVE_LEVEL, images)
    camera = Camera((level_x, level_y), WIDTH, HEIGHT)
    is_left = is_right = False
    up = False
    wat_up = False
    wat_down = False

    running = True
    while running:
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
        camera.update(hero)

        for sprite in all_sprites:
            camera.apply(sprite)

        hero.update(is_left, is_right, up, wat_up, wat_down, let_group, water_group, ladder_group, enemy_group,
                    coin_group, air_group)
        enemy_group.update()

        screen.fill(pygame.Color(218, 187, 253))
        ladder_group.draw(screen)
        water_group.draw(screen)
        air_group.draw(screen)
        hero_group.draw(screen)
        let_group.draw(screen)
        enemy_group.draw(screen)

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

if __name__ == '__main__':
    main()
