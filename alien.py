import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):

    def __init__(self, screen):
        super(Alien, self).__init__()
        self.set = Settings()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (60, 50))

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.set.speed_alien
        self.rect.y = self.y