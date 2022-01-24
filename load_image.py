import os
import pygame


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
        if color_key == -2:
            color_key = image.get_at((35, 0))
        if color_key == -3:
            color_key = image.get_at((0, 50))
        if color_key == -4:
            color_key = image.get_at((65, 65))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image
