# import os
# from tiles import Grass
import sys
import pygame
from load_image import load_image
from player import Player

pygame.init()
pygame.key.set_repeat(200)

FPS = 50
WIDTH = 800
HEIGHT = 800
STEP = 50
tile_width = tile_height = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
boxes_group = pygame.sprite.Group()

player_image = load_image('p1_walk11.png')
rect = tile_height, tile_width
pos = 0, 0
groups_for_player = all_sprites, player_group
player = Player(pos, player_image, groups_for_player, rect)


def terminate():
    pygame.quit()
    sys.exit()


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= STEP
            if event.key == pygame.K_RIGHT:
                player.rect.x += STEP
            if event.key == pygame.K_UP:
                player.rect.y -= STEP
            if event.key == pygame.K_DOWN:
                player.rect.y += STEP

    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

    clock.tick(FPS)
terminate()

