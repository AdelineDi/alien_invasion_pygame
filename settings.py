class Settings():
    """ Класс для всех настроек игры """
    def __init__(self):
        """ Инициализирует настройки игры """
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        #self.bg_colour = (216, 187, 237)
        self.bg_colour = (230, 230, 230)
        self.ship_speed_factor = 1.5