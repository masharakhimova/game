from time import *
import pygame as pg
from random import choice, randint

class Player:
    def __init__(self, game):
        pg.init()
        self.scr = game.scr
        self.game = game
        self.scr_rect = self.scr.get_rect()
        self.player = pg.image.load('images/player.gif')
        self.player = pg.transform.scale(self.player, (int(self.scr_rect.width / 16), int(self.scr_rect.height / 7)))
        self.stars = pg.image.load('images/kill_monster.gif')
        self.stars = pg.transform.scale(self.stars, (int(self.scr_rect.width / 20), int(self.scr_rect.height / 20)))
        self.sword = pg.image.load('images/damage.gif')
        self.sword = pg.transform.scale(self.sword, (int(self.scr_rect.width / 20), int(self.scr_rect.height / 20)))
        self.heart = pg.image.load('images/health.gif')
        self.heart = pg.transform.scale(self.heart, (int(self.scr_rect.width / 20), int(self.scr_rect.height / 20)))
        self.monster1 = pg.image.load('images/monsters/1.gif')
        self.monster1 = pg.transform.scale(self.monster1, (int(self.scr_rect.width / 20), int(self.scr_rect.height / 20)))
        self.monster2 = pg.image.load('images/monsters/2.gif')
        self.monster2 = pg.transform.scale(self.monster2, (int(self.scr_rect.width / 20), int(self.scr_rect.height / 20)))
        self.monster3 = pg.image.load('images/monsters/1.gif')
        self.monster3 = pg.transform.scale(self.monster1, (int(self.scr_rect.width / 20), int(self.scr_rect.height / 20)))

        self.font = pg.font.SysFont(None, 30)
        self.player_rect = self.player.get_rect()
        self.walls = self.game.walls
        self.settings = game.settings
        self.player_rect.center = self.scr_rect.center

        self.x = self.player_rect.x
        self.y = self.player_rect.y



    def move(self):
        self.scr_rect = self.scr.get_rect()
        self.player = pg.transform.scale(self.player, (int(self.scr_rect.width / 16), int(self.scr_rect.height / 7)))
        self.scr_rect = self.scr.get_rect()
        self.walls = self.game.walls
        self.floors = self.game.floor

        self.key = pg.key.get_pressed()

        dx = 0
        dy = 0

        if self.key[pg.K_UP]:
            dy = -self.settings.player_speed
            self.settings.player_approach = True
        elif self.key[pg.K_DOWN]:
            dy = self.settings.player_speed
            self.settings.player_approach = True
        else:
            self.settings.player_approach = False
        if self.key[pg.K_RIGHT]:
            self.settings.player_retreat = True
            dx = self.settings.player_speed
        elif self.key[pg.K_LEFT]:
            self.settings.player_retreat = True
            dx = -self.settings.player_speed
        else:
            self.settings.player_retreat = False

        new_rect = self.player_rect.move(dx, dy)

        # Проверка на выход за пределы экрана
        if new_rect.left < 0:
            new_rect.left = 0
        if new_rect.right > self.scr_rect.right:
            new_rect.right = self.scr_rect.right
        if new_rect.top < 0:
            new_rect.top = 0
        if new_rect.bottom > self.scr_rect.bottom:
            new_rect.bottom = self.scr_rect.bottom

        for wall in self.walls:
            if new_rect.colliderect(wall.wall_draw):
                return

        self.player_rect = new_rect
    def open_door(self):
        if self.player_rect.colliderect(self.game.door_show):
            self.settings.new_level = True

    def draw(self):
        self.scr.blit(self.player, self.player_rect)
        self.scr.blit(self.sword, (10, 10))
        self.scr.blit(self.heart, (10, 60))
        self.scr.blit(self.stars, (10, 110))

        damage_text = self.font.render(f"Damage: {self.settings.player_damage}", True, (255, 255, 255))
        health_text = self.font.render(f"Health: {self.settings.player_health}%", True, (255, 255, 255))
        monster_health_text = self.font.render(f"Stars: {self.settings.stars}", True, (255, 255, 255))
        self.scr.blit(damage_text, (60, 20))
        self.scr.blit(health_text, (60, 70))
        self.scr.blit(monster_health_text, (60, 120))

