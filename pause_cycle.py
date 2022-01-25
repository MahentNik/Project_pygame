import pygame
import pygame_gui
from pause_menu import PauseMenu
from terminate import terminate
from confirm import create_confirm

REPEAT_MUSIC = pygame.USEREVENT + 1


def pause_cycle(clock, fps, window_size, screen):
    pause_menu = PauseMenu(window_size)
    manager, pause_screen = pause_menu.give_manager()
    pause_menu.create(window_size)
    running = True
    while running:
        time_delta = clock.tick(fps) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                create_confirm(manager, window_size)
            if event.type == REPEAT_MUSIC:
                pygame.mixer.music.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                    terminate()
                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    pause_menu.game_difficult = event.text
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == pause_menu.continue_btn:
                        return False
                    elif event.ui_element == pause_menu.go_to_main_menu:
                        return True
                    elif event.ui_element == pause_menu.exit_btn:
                        create_confirm(manager, window_size)
            manager.process_events(event)
        screen.fill((218, 187, 253))
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()
