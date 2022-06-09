import pygame
from bullet import Bullet
from gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from settings import Settings


def run_game():
    # Инициализирует игру
    set = Settings()

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Игра про космос")
    bg_color = set.bg_color

# Создание ракеты
    gun = Gun(screen)
# Создание группы пуль
    bullets = Group()
# Создание группы пришельцев
    aliens = Group()
# Создание армии
    controls.create_army(screen, aliens)
# Статистика
    stats = Stats()
# Счет
    scores = Scores(screen, stats)


# Запуск основного цикла игры.
    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update()
            controls.update_bullets(screen, stats, scores, aliens, bullets)
            controls.update_screen(bg_color, screen, stats, scores, gun, aliens, bullets)
            controls.update_aliens(stats, screen, scores, gun, aliens, bullets)


run_game()