import pygame
import pygame_gui


class Menu:
    def __init__(self, window_size):
        self.manager = pygame_gui.UIManager(window_size)
        self.menu_surface = pygame.Surface(window_size)
        self.game_difficult = "Easy"

    def give_manager(self):
        return self.manager, self.menu_surface

    def create(self, size):
        start_btn_width = 160
        start_btn_height = 80
        self.start_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((size[0] // 2 - start_btn_width // 2, size[1] // 3),
                                      (start_btn_width, start_btn_height)),
            text="Play",
            manager=self.manager
        )
        exit_btn_width = 160
        exit_btn_height = 80
        self.exit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((size[0] // 2 - start_btn_width // 2, size[1] - size[1] // 3),
                                      (exit_btn_width, exit_btn_height)),
            text="Exit the Game",
            manager=self.manager
        )
        self.difficult = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
            options_list=["Easy", "Medium", "Hard"], starting_option="Easy",
            relative_rect=pygame.Rect((size[0] // 2 - start_btn_width // 2, size[1] - size[1] // 2),
                                      (exit_btn_width, exit_btn_height)),
            manager=self.manager,
        )
