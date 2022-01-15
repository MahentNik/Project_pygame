import pygame

HUD_SIZE = (HUD_WIDTH, HUD_HEIGHT) = (300, 150)
HERO_HP = 3
HERO_OXYGEN = 6

RELOAD_HIT = pygame.USEREVENT + 76  # перезарядка получения урона
COOLDOWN_DAMAGE = 1000
RELOAD_o2 = pygame.USEREVENT + 77  # перезарядка получения кислорода
COOLDOWN_O2 = 1000
RELOAD__o2 = pygame.USEREVENT + 78  # перезарядка отнимания кислорода
COOLDOWN__O2 = 2000


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

        self.firs_damage = False

        self.O2 = HERO_OXYGEN
        self.o2_im = o2_im
        self.visible_o2 = False

        # цифры
        self.numbers = numbers

        self.timer_o2 = False
        self.timer__o2 = False
        self.timer_hp = False

        self.show_stats()

    def collide(self, player, group, status=False):
        return pygame.sprite.spritecollide(player, group, status)

    def update(self, water_group, enemy_group, coin_group, air_group, may_get_damaged, first_damage,
               is_time_o2, is_time__o2):

        self.visible_o2 = False

        if self.collide(self.hero, enemy_group):
            if may_get_damaged or first_damage:
                self.HP -= 1
                self.firs_damage = False
                if not self.timer_hp:
                    pygame.time.set_timer(RELOAD_HIT, COOLDOWN_DAMAGE)
                    self.timer_hp = True
        else:
            self.timer_hp = False
            pygame.time.set_timer(RELOAD_HIT, 0)
            self.first_damage = True
            #  если сбрасывается соприкосновение с врагом, то нужно передать что первый дамаг должен восстановился)
            self.reload_first_damage()

        if self.O2 == 0:
            self.hero.kill()
            # если кислород кончится, то будет или смерть, или будкт отниматься по полхп

        if self.collide(self.hero, coin_group, True):
            self.coin_counter += 1

        if self.collide(self.hero, water_group):
            self.visible_o2 = True
            if not self.timer__o2:
                pygame.time.set_timer(RELOAD__o2, COOLDOWN__O2)
                self.timer__o2 = True
            if self.collide(self.hero, air_group):
                if not self.timer_o2:
                    pygame.time.set_timer(RELOAD_o2, COOLDOWN_O2)
                    self.timer_o2 = True
                if is_time_o2:
                    pygame.time.set_timer(RELOAD__o2, 0)
                    self.timer__o2 = False
                    if self.O2 < HERO_OXYGEN:
                        self.O2 += 1
            else:
                if is_time__o2:
                    pygame.time.set_timer(RELOAD_o2, 0)
                    self.timer_o2 = False
                    if self.O2 > 0:
                        self.O2 -= 1
        else:
            pygame.time.set_timer(RELOAD__o2, 0)
            pygame.time.set_timer(RELOAD_o2, 0)
            self.timer__o2 = False
            self.timer_o2 = False

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

    def reload_first_damage(self):
        return self.first_damage
