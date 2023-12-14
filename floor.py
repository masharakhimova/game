import pygame as pg

class Floor(pg.sprite.Sprite):
    '''
    отрисовка пола путем загрузки картинок
    '''
    def __init__(self, game):
        '''
        self.floor - загрузка картинки
        self.settings - начальные параметры уровня
        self.scr - экран
        '''
        super().__init__()
        pg.init()
        self.settings = game.settings
        self.scr_rect = game.scr.get_rect()
        self.scr = game.scr
        self.x = 0
        self.y = 0
        self.floor = pg.image.load('images/floor.png')
        self.floor = pg.transform.scale(self.floor, (self.scr_rect.width / 12, self.scr_rect.height / 6))
    def update(self):
        self.floor = pg.transform.scale(self.floor, (self.scr_rect.width / 12, self.scr_rect.height / 6))
        self.floor_draw = self.scr.blit(self.floor, (self.x, self.y))
