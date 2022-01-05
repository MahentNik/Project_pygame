import pygame

HUD_SIZE = (HUD_WIDTH, HUD_HEIGHT) = (300, 150)
HERO_HP = 3
HERO_OXYGEN = 6


class Hud(pygame.sprite.Sprite):
    def __init__(self, player, pos_x, pos_y, no_hp_im, half_hp_im, hp_im, o2_im, coin_im, *groups):
        super().__init__(groups)

        self.hero = player

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.tile = 50

        self.coin_counter = 0
        self.coin_im = coin_im

        self.HP = HERO_HP
        self.HP_im = hp_im
        self.halfHP_im = half_hp_im
        self.no_hp_im = no_hp_im
        self.visible_hp = True

        self.O2 = HERO_OXYGEN
        self.o2_im = o2_im
        self.visible_o2 = False
        self.reload_o2 = False

        self.show_stats()

    def collide(self, player, group, status=False):
        return pygame.sprite.spritecollide(player, group, status)

    def update(self, water_group, enemy_group, coin_group, air_group, is_time=False):

        self.visible_o2 = False
        self.reload_o2 = False

        if self.collide(self.hero, enemy_group):
            self.HP -= 1
        if self.collide(self.hero, coin_group, True):
            self.coin_counter += 1
        if self.collide(self.hero, water_group):
            self.visible_o2 = True
            if self.collide(self.hero, air_group):
                self.reload_o2 = True
                if is_time:
                    self.O2 += 1
            else:
                if is_time:
                    self.O2 -= 1

        self.show_stats()

    def show_stats(self):
        hud_screen = pygame.Surface((300, 150))

        hp_screen = self.HP_im

        o2_screen = self.o2_im

        font = pygame.font.Font(None, 50)
        coins = font.render(str(self.coin_counter), True, (100, 255, 100))
        coin_screen = self.coin_im
        coin_screen.blit(coins, [70, 50, 0, 0])

        # потом все эти холсты надо поместить в один
        hud_screen.blit(hp_screen, [0, 0, 0, 0])
        hud_screen.blit(coin_screen, [0, 50, 0, 0])
        if self.visible_o2:
            hud_screen.blit(o2_screen, [0, 100, 0, 0])
            # hud_screen.blit(o2_screen, (0, 100))
        # статы будут создаваться отдельными холстами и накладываться на основной в верхнем левом углу
        self.image = hud_screen
        self.rect = self.image.get_rect()
