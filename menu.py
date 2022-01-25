import pygame
import pygame_gui


class Menu:
    def __init__(self, window_size):
        self.manager = pygame_gui.UIManager(window_size)
        self.menu_surface = pygame.Surface(window_size)
        self.game_difficult = "Easy"
        self.game_lvl = "1_lvl"
        self.diff = ["Easy", "Medium", "Hard"]
        self.levels = ["1_lvl", '2_lvl']
        self.help_info = ''

    def give_manager(self):
        return self.manager, self.menu_surface

    def create(self, size):
        start_btn_width = 160
        start_btn_height = 80
        self.help_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (size[0] // 2 - start_btn_width // 2, size[1] - size[1] // 2.5 - start_btn_height // 2),
                (start_btn_width, start_btn_height)),
            text="Help",
            manager=self.manager)
        self.start_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((size[0] // 2 - start_btn_width // 2, size[1] // 4),
                                      (start_btn_width, start_btn_height)),
            text="Play",
            manager=self.manager
        )
        self.level = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
            options_list=self.levels, starting_option="1_lvl",
            relative_rect=pygame.Rect((size[0] // 2 - start_btn_width // 2, size[1] // 2 - start_btn_height),
                                      (start_btn_width, start_btn_height)),
            manager=self.manager,
        )
        exit_btn_width = 160
        exit_btn_height = 80
        self.exit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((size[0] // 2 - start_btn_width // 2, size[1] - (2 * start_btn_height)),
                                      (exit_btn_width, exit_btn_height)),
            text="Exit the Game",
            manager=self.manager
        )
        self.difficult = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
            options_list=self.diff, starting_option="Easy",
            relative_rect=pygame.Rect((size[0] // 2 - start_btn_width // 2, size[1] - size[1] // 3),
                                      (exit_btn_width, exit_btn_height)),
            manager=self.manager,
        )

    def create_confirm(self, manager, window_size):
        confirm_height = 300
        confirm_width = 500
        text = "Эта игра - платформер; " \
               "Управлениее производится посредством клавиатуры: " \
               "За движение в воде и на поверхности отвечают стрелочки, " \
               "За прыжок отвечает пробел; " \
               "Также присутствует возможность поставить игру на паузу - нажав кнопку P(З) или Esc." \
               " Присутствует функция автоудерживания кнопки," \
               "для ее активации зажмите нужную кнопку из перечня кнопок, " \
               "затем нажмите Esc или P (вы войдете в режим паузы), здесь вам необходимо отжать выбранную кнопку " \
               "и снова нажать на Esc или P (вы выйдете из режима паузы). " \
               "Теперь ваш персонаж движется в выбранном направлении, " \
               "чтобы отключить эту функцию заново нажмите на кнопку которую вы выбирали вначале) " \
               "P.S Далее идут подсказки по прохождению первого уровня ели вы хотите разобраться сами," \
               " то ниже не листайте." \
               "--------------------------------------------------------------------------------------" \
               "--------------------------------------------------------------------------------------" \
               "--------------------------------------------------------------------------------------" \
               "--------------------------------------------------------------------------------------" \
               "--------------------------------------------------------------------------------------" \
               "------------------------------------------------------------------------- " \
               "Чтобы пройти уровень вам нужно забраться по воде в самом начале карты, " \
               "затем проползти по лестницам в небе и спрыгнуть на табличку {exit}"

        self.help_info = pygame_gui.windows.UIConfirmationDialog(
            rect=pygame.Rect(
                (window_size[0] // 2 - confirm_width // 2, window_size[1] // 2 - confirm_height // 2),
                (confirm_width, confirm_height)),
            manager=manager,
            window_title="Информация",
            action_long_desc=text,
            action_short_name="OK",
            blocking=True
        )
