import sys
import pygame
from bullet import Bullet
import pygame.mixer

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Создание новой пули и включение ее в группу bullets
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        #Звук выстрела
        pygame.mixer.Sound('sounds/413057__lilmati__retro-laser-shot-01.wav').play()

def check_keyup_events(event,ship):
    """ Реагирует на отпускание клавищ """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left =False

def check_events(ai_settings, screen, ship, bullets):
# Отслеживание событий клавиатуры и мыши.
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
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

def update_screen(ai_settings, screen, ship, bullets):
    """ Обновляет изображения на экране и отображает новый экран """
    #При каждом проходе цикла перерисовывается экран
    #Все пули выводятся позади изображений корабля и прищельцев
    screen.fill(ai_settings.bg_colour)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Отображение последнего прорисованного окна
    pygame.display.flip()