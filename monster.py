import pygame as pg
from random import *

class Monster(pg.sprite.Sprite):
    def __init__(self, game):
        '''
        отрисовка противников. self.moster - случайный выбор одного из трех монстров
        self.x и self.y - случайная позиция противника
        self.damage - урон монстра
        self.write_health - отображение здоровья у монстра
        '''
        pg.init()
        super().__init__()
        self.scr = game.scr
        self.scr_rect = self.scr.get_rect()
        self.scr_rect = self.scr.get_rect()
        monster_1 = pg.image.load('images/monsters/1.gif')
        monster_2 = pg.image.load('images/monsters/2.gif')
        monster_3 = pg.image.load('images/monsters/3.gif')
        self.monster = choice([monster_1, monster_2, monster_3])
        self.monster = pg.transform.scale(self.monster, (self.scr_rect.width / 13, self.scr_rect.height / 7))
        self.x = choice(game.settings.ox)
        self.y = choice(game.settings.oy)
        self.monster_rect = self.monster.get_rect()
        self.damage = randint(5, 10)
        self.font = pg.font.SysFont(None, 20)
        self.health = 100

    def update(self):
        self.write_health = self.font.render(f'{self.health}%', True, (255, 0, 0))
        self.monster_rect = self.monster.get_rect()
        self.monster_rect.x = self.x
        self.monster_rect.y = self.y
        self.scr.blit(self.monster, self.monster_rect)
        self.scr.blit(self.write_health, (self.x, self.y))
