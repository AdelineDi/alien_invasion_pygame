import sys
import pygame

def check_keydown_events(event, ship):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    """ Реагирует на отпускание клавищ """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left =False

def check_events(ship):
# Отслеживание событий клавиатуры и мыши.
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
            # if event.key == pygame.K_RIGHT:
            #     #Переместить корабль вправо.
            #     #ship.rect.centerx +=1
            #     ship.moving_right =True
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """ Обновляет изображения на экране и отображает новый экран """
    #При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_colour)
    ship.blitme()
    # Отображение последнего прорисованного окна
    pygame.display.flip()