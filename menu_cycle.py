import pygame
import pygame_gui
from terminate import terminate
from menu import Menu

REPEAT_MUSIC = pygame.USEREVENT + 1


def menu_cycle(clock, fps, window_size, screen):
    menu = Menu(window_size)
    manager, menu_screen = menu.give_manager()
    menu.create(window_size)
    while True:
        time_delta = clock.tick(fps) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == REPEAT_MUSIC:
                pygame.mixer.music.play()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    menu.game_difficult = event.text
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == menu.start_btn:
                        return menu.game_difficult
                    elif event.ui_element == menu.exit_btn:
                        terminate()
            manager.process_events(event)
        screen.fill((218, 187, 253))
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()
