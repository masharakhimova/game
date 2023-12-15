import pygame as pg
from random import *

class PlusDamage(pg.sprite.Sprite):
    def __init__(self, game):
        '''
        инициализация картинки оружия и случайное ее размещение на поле
        '''
        pg.init()
        super().__init__()
        self.scr = game.scr
        self.scr_rect = self.scr.get_rect()
        self.walls = game.walls
        self.damage = pg.image.load('images/damage.gif')
        self.damage = pg.transform.scale(self.damage, (self.scr_rect.width / 13, self.scr_rect.height / 7))
        self.damage_rect = self.damage.get_rect()
        self.x = choice(game.settings.ox)
        self.y = choice(game.settings.oy)

    def update(self):
        #появление оружия на экране
        self.damage_rect.x = self.x
        self.damage_rect.y = self.y
        self.scr.blit(self.damage, self.damage_rect)
