import pygame

HUD_SIZE = (HUD_WIDTH, HUD_HEIGHT) = (300, 150)
HERO_HP = 3
HERO_OXYGEN = 6

RELOAD_HIT = pygame.USEREVENT + 76  # перезарядка получения урона
RELOAD_02 = pygame.USEREVENT + 77  # перезарядка получения кислорода
RELOAD__02 = pygame.USEREVENT + 78  # перезарядка отнимания кислорода


class Hud(pygame.sprite.Sprite):
    def __init__(self, player, pos_x, pos_y, no_hp_im, half_hp_im, hp_im, o2_im, coin_im, numbers, *groups):
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

        # цифры
        self.numbers = numbers

        self.show_stats()

    def collide(self, player, group, status=False):
        return pygame.sprite.spritecollide(player, group, status)

    def update(self, water_group, enemy_group, coin_group, air_group, may_get_damaged, is_time_o2, is_time__o2):

        self.visible_o2 = False

        if self.collide(self.hero, enemy_group):
            if may_get_damaged:
                self.HP -= 1
                pygame.time.set_timer(RELOAD_HIT, 1000)
        else:
            pygame.time.set_timer(RELOAD_HIT, 0)
        if self.collide(self.hero, coin_group, True):
            self.coin_counter += 1
        if self.collide(self.hero, water_group):
            self.visible_o2 = True
            if self.collide(self.hero, air_group):
                pygame.time.set_timer(RELOAD__02, 0)
                pygame.time.set_timer(RELOAD_02, 1000)
                if is_time_o2:
                    self.O2 += 1
            else:
                pygame.time.set_timer(RELOAD_02, 0)
                pygame.time.set_timer(RELOAD__02, 1000)
                if is_time__o2:
                    self.O2 -= 1

        self.show_stats()

    def show_stats(self):
        change_pos = 50
        hp = self.HP
        coins = self.coin_counter
        coins = str(coins).split()

        photo_0, photo_1, photo_2, photo_3, photo_4, photo_5, photo_6, photo_7, photo_8, photo_9 = self.numbers

        hud_screen = pygame.Surface((300, 150))

        pos_x = 0
        for i in range(HERO_HP):
            if hp >= 1:
                hp -= 1
                hud_screen.blit(self.HP_im, (pos_x, 0))
            elif hp <= 0:
                hud_screen.blit(self.no_hp_im, (pos_x, 0))
            elif 0 < hp < 1:
                hp -= 0.5
                hud_screen.blit(self.halfHP_im, (pos_x, 0))
            pos_x += change_pos

        if self.visible_o2:
            pos_x = 0
            for _ in range(self.O2):
                hud_screen.blit(self.o2_im, (pos_x, 50))
                pos_x += change_pos

        pos_x = 0
        hud_screen.blit(self.coin_im, (pos_x, 100))
        pos_x += change_pos * 1.5
        change_pos = 32
        for i in coins:
            name_photo = eval("photo_" + i)
            hud_screen.blit(name_photo, (pos_x, 106))
            pos_x += change_pos

        self.image = hud_screen
        self.rect = self.image.get_rect()
