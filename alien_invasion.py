import sys
import pygame
from settings import Settings
from ship import  Ship
import game_functions as gf

def run_game():
    """ Инициализирует игру """
    pygame.init()
    ai_settings = Settings()
    #screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings ,screen)
    #bg_colour = (216, 187, 237)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
run_game()