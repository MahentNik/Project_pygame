import pygame
import pygame_gui


class PauseMenu:
    def __init__(self, window_size):
        self.manager = pygame_gui.UIManager(window_size)
        self.pause_surface = pygame.Surface(window_size)

    def give_manager(self):
        return self.manager, self.pause_surface

    def create(self, size):
        start_btn_width = 160
        start_btn_height = 80
        self.continue_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((size[0] // 2 - start_btn_width // 2, size[1] // 3),
                                      (start_btn_width, start_btn_height)),
            text="Continue",
            manager=self.manager
        )
        exit_btn_width = 160
        exit_btn_height = 80
        self.exit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((size[0] // 2 - start_btn_width // 2, size[1] - size[1] // 2),
                                      (exit_btn_width, exit_btn_height)),
            text="Exit the Game",
            manager=self.manager
        )
