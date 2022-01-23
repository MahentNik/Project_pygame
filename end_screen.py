import pygame
import pygame_gui
from terminate import terminate


class EndScreen:
    def __init__(self, image_end, screen, clock, fps):
        self.image = image_end
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.play_losed_music()

    def play_losed_music(self):
        pass

    def create_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONDOWN:
                    return False
            self.screen.blit(self.image, (0, 0))
            pygame.display.flip()
            self.clock.tick(self.fps)
