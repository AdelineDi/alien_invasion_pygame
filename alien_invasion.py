import pygame
from settings import Settings
from ship import  Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    """ Инициализирует игру """
    pygame.init()
    ai_settings = Settings()
    #screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings ,screen)
    #Создание группы для хранения пуль
    bullets = Group()
    #bg_colour = (216, 187, 237)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()