import pygame

HUD_SIZE = (HUD_WIDTH, HUD_HEIGHT) = (300, 150)

RELOAD_HIT = pygame.USEREVENT + 76  # перезарядка получения урона
COOLDOWN_DAMAGE = 1000
RELOAD_o2 = pygame.USEREVENT + 77  # перезарядка получения кислорода
COOLDOWN_O2 = 1000
RELOAD__o2 = pygame.USEREVENT + 78  # перезарядка отнимания кислорода
COOLDOWN__O2 = 2000
RELOAD__05 = pygame.USEREVENT + 111


class Hud(pygame.sprite.Sprite):
    def __init__(self, hero_hp, hero_oxygen, player, pos_x, pos_y, for_hud, numbers, *groups):
        super().__init__(*groups)

        self.hero_hp = hero_hp
        self.hero_oxygen = hero_oxygen

        self.hero = player

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.tile = 50

        self.coin_counter = 0
        self.coin_im = for_hud[4]

        self.HP = hero_hp
        self.HP_im = for_hud[2]
        self.halfHP_im = for_hud[1]
        self.no_hp_im = for_hud[0]
        self.visible_hp = True

        self.firs_damage = False

        self.O2 = hero_oxygen
        self.o2_im = for_hud[3]
        self.visible_o2 = False

        # цифры
        self.numbers = numbers

        self.firs_damage = True
        self.timer_hp = False
        self.timer_o2 = False
        self.timer__o2 = False
        self.timer__05 = False

        self.show_stats()

    def update(self, dead_block_group, water_group, enemy_group, coin_group, air_group, spikes_group,
               may_get_damaged, is_time_o2, is_time__o2, is_time__05):

        if collide(self.hero, dead_block_group):
            self.HP = 0

        self.visible_o2 = False

        if collide(self.hero, enemy_group) or collide(self.hero, spikes_group):
            if may_get_damaged or self.firs_damage:
                self.HP -= 1
                self.firs_damage = False
                if not self.timer_hp:
                    pygame.time.set_timer(RELOAD_HIT, 1000)
                    self.timer_hp = True
        else:
            pygame.time.set_timer(RELOAD_HIT, 0)
            self.timer_hp = False
            self.firs_damage = True

        if self.O2 == 0:
            if not self.timer__05:
                pygame.time.set_timer(RELOAD__05, 1000)
                self.timer__05 = True
            if is_time__05:
                self.HP -= 0.5
        else:
            pygame.time.set_timer(RELOAD__05, 0)
            self.timer__05 = False

        if collide(self.hero, coin_group, True):
            self.coin_counter += 1

        if collide(self.hero, water_group):
            self.visible_o2 = True
            if not self.timer__o2:
                pygame.time.set_timer(RELOAD__o2, COOLDOWN__O2)
                self.timer__o2 = True
            if collide(self.hero, air_group):
                if not self.timer_o2:
                    pygame.time.set_timer(RELOAD_o2, COOLDOWN_O2)
                    self.timer_o2 = True
                if is_time_o2:
                    pygame.time.set_timer(RELOAD__o2, 0)
                    self.timer__o2 = False
                    if self.O2 < self.hero_oxygen:
                        self.O2 += 1
            else:
                if is_time__o2:
                    pygame.time.set_timer(RELOAD_o2, 0)
                    self.timer_o2 = False
                    if self.O2 > 0:
                        self.O2 -= 1
        else:
            pygame.time.set_timer(RELOAD__o2, 0)
            self.timer__o2 = False
            if self.O2 < self.hero_oxygen:
                if not self.timer_o2:
                    pygame.time.set_timer(RELOAD_o2, COOLDOWN_O2)
                    self.timer_o2 = True
                if is_time_o2:
                    self.O2 += 1
            else:
                pygame.time.set_timer(RELOAD_o2, COOLDOWN_O2)
                self.timer_o2 = False

        self.show_stats()

    def show_hp(self, screen):
        pos_x = 0
        change_pos = 50
        hp = self.HP
        for i in range(self.hero_hp):
            if hp >= 1:
                hp -= 1
                screen.blit(self.HP_im, (pos_x, 0))
            elif hp <= 0:
                screen.blit(self.no_hp_im, (pos_x, 0))
            elif 0 < hp < 1:
                hp -= 0.5
                screen.blit(self.halfHP_im, (pos_x, 0))
            pos_x += change_pos

    def hero_status(self):
        if self.HP <= 0:
            self.hero.kill()
            return True
        else:
            return None

    def show_coins(self, screen):
        coins = str(self.coin_counter)

        pos_x = 0
        screen.blit(self.coin_im, (pos_x, 50))

        change_pos = 32
        pos_x += change_pos * 1.5
        photo_0, photo_1, photo_2, photo_3, photo_4, photo_5, photo_6, photo_7, photo_8, photo_9 = self.numbers

        for i in range(len(coins)):
            name_photo = eval("photo_" + coins[i])
            screen.blit(name_photo, (pos_x, 50))
            pos_x += change_pos

    def show_oxygen(self, screen):
        pos_x = 0
        change_pos = 50

        for _ in range(self.O2):
            screen.blit(self.o2_im, (pos_x, 90))
            pos_x += change_pos

    def show_stats(self):
        hud_screen = pygame.Surface((300, 140), pygame.SRCALPHA, 32)
        hud_screen.convert_alpha()

        self.show_hp(hud_screen)
        self.show_coins(hud_screen)
        if self.visible_o2:
            self.show_oxygen(hud_screen)

        self.image = hud_screen
        self.rect = self.image.get_rect()


def collide(player, group, status=False):
    return pygame.sprite.spritecollide(player, group, status)
