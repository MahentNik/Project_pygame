import pygame_gui
import pygame


def create_confirm(manager, window_size):
    confirm_height = 200
    confirm_width = 300
    exit_info = pygame_gui.windows.UIConfirmationDialog(
        rect=pygame.Rect(
            (window_size[0] // 2 - confirm_width // 2, window_size[1] // 2 - confirm_height // 2),
            (confirm_width, confirm_height)),
        manager=manager,
        window_title="Confirm Exit",
        action_long_desc="Do you really want to leave the game?",
        action_short_name="Yes",
        blocking=True
    )
