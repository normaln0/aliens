import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):

    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.set = Settings()
        self.screen = screen
        self.gun = gun
        self.rect = pygame.Rect(0, 0, 5, 12)
        self.color = 139, 195, 74
        self.speed = self.set.speed_bullet
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect) 