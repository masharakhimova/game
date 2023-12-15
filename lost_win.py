import pygame as pg

class LostWin():
    '''
    отображение экрана в случае победы или поражения
    '''
    def __init__(self, game):
        '''
        self.lost_write и self.win_write - отображение надписей в случае
        соответственно победы или поражения
        '''
        pg.init()
        self.scr = game.scr
        self.font = pg.font.SysFont(None, 60)
        self.win_write = self.font.render('Вы победили!', True, (0, 255, 0))
        self.lost_write = self.font.render('Вы проиграли', True, (255, 0, 0))
        self.settings = game.settings

    def win(self):
        #победа в случае прохождения 10 уровня
        if self.settings.level == 10:
            self.settings.lost_win = True
            self.scr.fill((0, 0, 255))
            self.scr.blit(self.win_write, (0, 0))

    def lost(self):
        #поражение в случае потери всего здоровья
        if self.settings.player_health <= 0:
            self.settings.lost_win = True
            self.scr.fill((0, 0, 255))
            self.scr.blit(self.lost_write, (0, 0))
