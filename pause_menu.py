import pygame
import pygame_gui


class PauseMenu:
    def __init__(self, window_size):
        self.manager = pygame_gui.UIManager(window_size)
        self.pause_surface = pygame.Surface(window_size)

    def give_manager(self):
        return self.manager, self.pause_surface

    def create(self, size):
        btn_width = 160
        btn_height = 80
        self.continue_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((size[0] // 2 - btn_width // 2, size[1] // 3),
                                      (btn_width, btn_height)),
            text="Continue",
            manager=self.manager
        )
        self.go_to_main_menu = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((size[0] // 2 - btn_width // 2, size[1] - size[1] // 2),
                                      (btn_width, btn_height)),
            text="Go to Main Menu",
            manager=self.manager
        )
        self.exit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((size[0] // 2 - btn_width // 2, size[1] - size[1] // 3),
                                      (btn_width, btn_height)),
            text="Exit the Game",
            manager=self.manager
        )
