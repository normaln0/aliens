import pygame
import sys
import time
from bullet import Bullet
from alien import Alien
from settings import Settings

set = Settings()

def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            if event.key == pygame.K_LEFT:
                gun.mleft = False

def update_bullets(screen, stats, scores, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        scores.image_score()
        check_high_score(stats, scores)
        scores.image_guns()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)

    
def create_army(screen, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((800 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 150 - alien_height*2) / alien_height)

    for row_number in range(number_alien_y - set.level):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 1 * alien.rect.height * row_number
            aliens.add(alien)


def update_aliens(stats, screen, scores, gun, aliens, bullets):
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, scores, gun, aliens, bullets)
    aliens_check(stats, screen, scores, gun, aliens, bullets)


def gun_kill(stats, screen, scores, gun, aliens, bullets):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        scores.image_guns()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        gun.create_gun()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()


def aliens_check(stats, screen, scores, gun, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, scores, gun, aliens, bullets)
            break


def update_screen(bg_color, screen, stats, scores, gun, aliens, bullets):
        screen.fill(bg_color)
        scores.show_score()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        gun.outpoot()
        aliens.draw(screen)
        pygame.display.flip()


def check_high_score(stats, scores):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scores.image_high_score()
        with open('higscore.txt', 'w') as file:
            file.write(str(stats.high_score))
