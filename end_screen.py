import pygame
import pygame_gui
from terminate import terminate

SKIP_END_SCREEN = pygame.USEREVENT + 140

class EndScreen:
    def __init__(self, image_end, screen, clock, fps):
        self.image = image_end
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.play_music()
        self.time = False

    def play_music(self):
        pass

    def create_screen(self):
        pygame.time.set_timer(SKIP_END_SCREEN, 3000)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == SKIP_END_SCREEN:
                    pygame.time.set_timer(SKIP_END_SCREEN, 0)
                    self.time = True
                if self.time:
                    if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONDOWN:
                        return False
            self.screen.blit(self.image, (0, 0))
            pygame.display.flip()
            self.clock.tick(self.fps)
