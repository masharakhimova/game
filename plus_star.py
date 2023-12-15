import pygame as pg
from random import *


class PlusStar(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.scr = game.scr
        self.scr_rect = self.scr.get_rect()
        self.walls = game.walls
        self.star = pg.image.load('images/kill_monster.gif')
        self.star = pg.transform.scale(self.star, (self.scr_rect.width / 13, self.scr_rect.height / 7))
        self.star_rect = self.star.get_rect()
        self.x = choice(game.settings.ox)
        self.y = choice(game.settings.oy)

    def update(self):
        self.star_rect = self.star.get_rect()
        self.star_rect.x = self.x
        self.star_rect.y = self.y
        self.scr.blit(self.star, self.star_rect)