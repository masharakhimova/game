import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = 0x000000
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 1300
HEIGHT = 700

class Hero:
    def __init__(self, screen, x, y):
        self.live = 1
        self.x = x
        self.y = y
        self.screen = screen
        rect = pygame.Rect((50 * self.x, self.y * 50, 50, 50))
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        surf = pygame.image.load('hero.jpg').convert()
        surf = pygame.transform.scale(surf, (50, 50))
        self.screen.blit(surf, (50 * self.x, 50 * self.y))
        
    def move_up(self, level_map):
        if level_map[self.y - 1][self.x] == '.' or level_map[self.y - 1][self.x] == '@' or level_map[self.y - 1][self.x] == '!':
            surf = pygame.image.load('floor.png')
            surf = pygame.transform.scale(surf, (50, 50))
            self.screen.blit(surf, (50 * self.x, 50 * self.y))
            self.y -= 1
            rect = pygame.Rect((50 * self.x, self.y * 50, 50, 50))
            pygame.draw.rect(self.screen, (255, 255, 255), rect)
            surf = pygame.image.load('hero.jpg').convert()
            surf = pygame.transform.scale(surf, (50, 50))
            self.screen.blit(surf, (50 * self.x, 50 * self.y))

    def move_down(self, level_map):
        if level_map[self.y + 1][self.x] == '.' or level_map[self.y + 1][self.x] == '@' or level_map[self.y + 1][self.x] == '!':
            surf = pygame.image.load('floor.png')
            surf = pygame.transform.scale(surf, (50, 50))
            self.screen.blit(surf, (50 * self.x, 50 * self.y))
            self.y += 1
            rect = pygame.Rect((50 * self.x, self.y * 50, 50, 50))
            pygame.draw.rect(self.screen, (255, 255, 255), rect)
            surf = pygame.image.load('hero.jpg').convert()
            surf = pygame.transform.scale(surf, (50, 50))
            self.screen.blit(surf, (50 * self.x, 50 * self.y))

    def move_left(self, level_map):
        if level_map[self.y][self.x - 1] == '.' or level_map[self.y][self.x - 1] == '@' or level_map[self.y][self.x - 1] == '!':
            surf = pygame.image.load('floor.png')
            surf = pygame.transform.scale(surf, (50, 50))
            self.screen.blit(surf, (50 * self.x, 50 * self.y))
            self.x -= 1
            rect = pygame.Rect((50 * self.x, self.y * 50, 50, 50))
            pygame.draw.rect(self.screen, (255, 255, 255), rect)
            surf = pygame.image.load('hero.jpg').convert()
            surf = pygame.transform.scale(surf, (50, 50))
            self.screen.blit(surf, (50 * self.x, 50 * self.y))

    def move_right(self, level_map):
        if level_map[self.y][self.x + 1] == '.' or level_map[self.y][self.x + 1] == '@' or level_map[self.y][self.x + 1] == '!':
            surf = pygame.image.load('floor.png')
            surf = pygame.transform.scale(surf, (50, 50))
            self.screen.blit(surf, (50 * self.x, 50 * self.y))
            self.x += 1
            rect = pygame.Rect((50 * self.x, self.y * 50, 50, 50))
            pygame.draw.rect(self.screen, (255, 255, 255), rect)
            surf = pygame.image.load('hero.jpg').convert()
            surf = pygame.transform.scale(surf, (50, 50))
            self.screen.blit(surf, (50 * self.x, 50 * self.y))
            

def load_level(name):
    with open(name, 'r') as map_file:
        level_map = []
        for line in map_file:
            line = line.strip()
            level_map.append(line)
    return level_map

def draw_level(screen, level_map):
    new_player, x, y = None, None, None
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == '.':
                surf = pygame.image.load('floor.png')
                surf = pygame.transform.scale(surf, (50, 50))
                screen.blit(surf, (50 * x, 50 * y))
            elif level_map[y][x] == '#':
                surf = pygame.image.load('stone.png')
                surf = pygame.transform.scale(surf, (50, 50))
                screen.blit(surf, (50 * x, 50 * y))
            elif level_map[y][x] == '@':
                surf = pygame.image.load('floor.png')
                surf = pygame.transform.scale(surf, (50, 50))
                screen.blit(surf, (50 * x, 50 * y))
                new_player = Hero(screen, x, y)
            elif level_map[y][x] == '!':
                surf = pygame.image.load('door.png')
                surf = pygame.transform.scale(surf, (50, 50))
                screen.blit(surf, (50 * x, 50 * y))
    return new_player, x, y

def start(flag, finished, level):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    level_map = load_level(level)
    player, level_x, level_y = draw_level(screen, level_map)
    while finished:
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = False
                flag = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.move_up(level_map)
                    if level_map[player.y][player.x] == '!':
                        finished = False
                        return True
                if event.key == pygame.K_s:
                    player.move_down(level_map)
                    if level_map[player.y][player.x] == '!':
                        finished = False
                        return True
                if event.key == pygame.K_d:
                    player.move_right(level_map)
                    if level_map[player.y][player.x] == '!':
                        finished = False
                        return True
                if event.key == pygame.K_a:
                    player.move_left(level_map)
                    if level_map[player.y][player.x] == '!':
                        finished = False
                        return True

flag = True
finished = True
levels = ['level_1.txt', 'level_2.txt']
del_level = []
while flag:
    if len(levels) == 0:
        break
    level = levels[0]
    del_level.append(level)
    del levels[0]
    if not start(flag, finished, level):
        break
pygame.quit()
