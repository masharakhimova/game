import pygame as pg

class Wall(pg.sprite.Sprite):
    '''
    отрисовка стен
    '''
    def __init__(self, game):
        '''
        self.settings - параметры
        self.scr - экран
        self.wall - загрузка картинки стен
        '''
        super().__init__()
        self.x = 0
        self.y = 0
        pg.init()
        self.settings = game.settings
        self.scr = game.scr
        self.scr_rect = game.scr.get_rect()
        self.wall = pg.image.load('images/walls.png')
        self.wall = pg.transform.scale(self.wall, (self.scr_rect.width / 12, self.scr_rect.height / 6))

    def update(self):
        '''
        обновление стен для новых уровней
        '''
        self.wall = pg.transform.scale(self.wall, (self.scr_rect.width / 12, self.scr_rect.height / 6))
        self.wall_draw = self.scr.blit(self.wall, (self.x, self.y))
