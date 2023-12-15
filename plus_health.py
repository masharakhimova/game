import pygame as pg
from random import *


class PlusHealth(pg.sprite.Sprite):
    def __init__(self, game):
        pg.init()
        super().__init__()
        self.scr = game.scr
        self.scr_rect = self.scr.get_rect()
        self.walls = game.walls
        self.health = pg.image.load('images/health.gif')
        self.health = pg.transform.scale(self.health, (self.scr_rect.width / 13, self.scr_rect.height / 7))
        self.health_rect = self.health.get_rect()
        self.x = choice(game.settings.ox)
        self.y = choice(game.settings.oy)

    def update(self):
        self.health_rect = self.health.get_rect()
        self.health_rect.x = self.x
        self.health_rect.y = self.y
        self.scr.blit(self.health, self.health_rect)