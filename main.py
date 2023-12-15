import pygame as pg
from random import *
import sys

from floor import *
from walls import *
from settings import *
from player import *
from plus_damage import *
from plus_health import *
from plus_star import *
from monster import *
from lost_win import *

class Game:
    def __init__(self):
        pg.init()
        self.objects = []
        self.scr = pg.display.set_mode((900, 600))
        pg.display.set_caption('Pixel Dungeon')
        self.scr_rect = self.scr.get_rect()

        self.walls = pg.sprite.Group()
        self.floor = pg.sprite.Group()
        self.stars = pg.sprite.Group()
        self.hearts = pg.sprite.Group()
        self.swords = pg.sprite.Group()
        self.monsters = pg.sprite.Group()

        self.settings = Settings()
        self.player = Player(self)
        self.lost_win = LostWin(self)

        self.door = pg.image.load('images/door.png')
        self.door = pg.transform.scale(self.door, (self.scr_rect.width / 12, self.scr_rect.height / 6))

        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont(None, 30)

    def run(self):
        while True:
            self.check_events()
            self.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

    def update(self):
        if self.settings.lost_win == False:
            self.level = self.font.render(f'Level: {self.settings.level + 1}', True, (255, 255, 255))
            if self.settings.new_level:
                self.settings.new_level = False
                self.settings.level += 1
                if self.settings.level < 10:
                    self.settings.card = self.settings.cards[self.settings.level]
                    self.maze()
            self.walls.update()
            self.floor.update()
            self.door_show = self.scr.blit(self.door, (self.door_x, self.door_y))
            self.darken_screen(self.scr, 128)
            self.player.move()
            self.player.open_door()
            self.stars.update()
            self.swords.update()
            self.hearts.update()
            self.monsters.update()
            self.health()
            self.damage()
            self.kill_monster()
            self.monster()
            self.scr.blit(self.level, (60, 170))
            self.player.draw()
            flashlight_radius = 100
            self.draw_flashlight(self.scr, self.player.player_rect, flashlight_radius, 128)
        self.lost_win.win()
        self.lost_win.lost()
        self.clock.tick(self.settings.fps)
        pg.display.update()

    def maze(self):
        a = 0
        self.scr_rect = self.scr.get_rect()
        width = self.scr_rect.width / 12
        height = self.scr_rect.height / 6
        self.y = 0
        self.x = 0
        self.settings.ox.clear()
        self.settings.oy.clear()
        for star in self.stars.copy():
            self.stars.remove(star)
        for heart in self.hearts.copy():
            self.stars.remove(heart)
        for sword in self.swords.copy():
            self.stars.remove(sword)
        for monster in self.monsters.copy():
            self.stars.remove(monster)

        for wall in self.walls.copy():
            self.walls.remove(wall)
        for floor in self.floor.copy():
            self.floor.remove(floor)
        for i in self.settings.card:
            if i == '#':
                wall = Wall(self)
                self.walls.add(wall)
                wall.x = self.x
                wall.y = self.y
                self.x += width

            elif i == '.':
                floor = Floor(self)
                self.floor.add(floor)
                floor.x = self.x
                floor.y = self.y
                self.settings.ox.append(floor.x)
                self.settings.oy.append(floor.y)
                self.x += width

            elif i == '@':
                self.door_x = self.x
                self.door_y = self.y
                self.x += width
            a += 1
            if a >= 12:
                self.y += height
                self.x = 0
                a = 0
        self.y = 0
        self.x = 0

    def damage(self):
        if len(self.swords) < 5:
            sword = PlusDamage(self)
            self.swords.add(sword)
        for sword in self.swords.copy():

            if sword.damage_rect.colliderect(self.player.player_rect):
                self.settings.player_damage += randint(10, 20)
                self.swords.remove(sword)
    def health(self):
        if len(self.hearts) < 5:
            heart = PlusHealth(self)
            self.hearts.add(heart)
        for heart in self.hearts.copy():
            if heart.health_rect.colliderect(self.player.player_rect):
                for i in range(randint(5, 25)):
                    if self.settings.player_health == 100:
                        break
                    self.settings.player_health += 1
                self.hearts.remove(heart)

    def kill_monster(self):
        if len(self.stars) < 5:
            star = PlusStar(self)
            self.stars.add(star)
        for star in self.stars.copy():
            if star.star_rect.colliderect(self.player.player_rect):
                self.settings.stars += 1
                self.stars.remove(star)

    def monster(self):
        if len(self.monsters) < 2:
            monster = Monster(self)
            self.monsters.add(monster)
        for monster in self.monsters.copy():
            distance_x = abs(self.player.player_rect.x - monster.monster_rect.x)
            distance_y = abs(self.player.player_rect.y - monster.monster_rect.y)
            if distance_x < 15 or distance_y < 15 and not self.settings.player_retreat and not self.settings.player_approach:
                if self.settings.stars > 0:
                    self.settings.stars -= 1
                    monster.health = 0
                if monster.health <= 0:
                    self.monsters.remove(monster)
                self.settings.player_health -= monster.damage
                monster.health -= self.settings.player_damage
                pg.time.wait(300)

    def darken_screen(self, surface, alpha):
        dark_surface = pg.Surface((self.scr.get_width(), self.scr.get_height()), pg.SRCALPHA)
        dark_surface.fill((0, 0, 0, alpha))
        surface.blit(dark_surface, (0, 0))

    def draw_flashlight(self, surface, player_rect, light_radius, alpha):
        light_mask = pg.Surface((self.scr.get_width(), self.scr.get_height()))
        light_mask.fill((50, 50, 50))
        pg.draw.circle(light_mask, (255, 255, 255), player_rect.center, light_radius)
        surface.blit(light_mask, (0, 0), special_flags=pg.BLEND_MULT)


game = Game()
game.run()
