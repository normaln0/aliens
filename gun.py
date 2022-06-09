from turtle import screensize
import pygame
from pygame.sprite import Sprite
from settings import Settings

class Gun(Sprite):
    def __init__(self, screen):
        super(Gun, self).__init__()
        self.set = Settings()
        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (40, 70))

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx

        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.mright = False
        self.mleft = False

        self.speed = self.set.speed_gun

    def outpoot(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        elif self.mleft and self.rect.left > 0:
            self.center -= self.speed

        self.rect.centerx = self.center

    def create_gun(self):
        self.center = self.screen_rect.centerx