import pygame
import sys

width = 800
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Главное меню')
clock = pygame.time.Clock()
FPS = 60
x = True

def start_screen():
    '''
    отрисовка начальной заставки
    '''
    global x
    background = pygame.image.load('images/mainmenu.png')
    background = pygame.transform.scale(background, (width, height))
    screen.blit(background, (0, 0))
    #инициализация шрифтов для текста
    pygame.font.init()
    font = pygame.font.Font(None, 40)
    string = font.render('Нажмите любую клавишу', 1, pygame.Color('white'))
    screen.blit(string, (170, 200))
    string = font.render('для начала игры', 1, pygame.Color('white'))
    screen.blit(string, (250, 260))
    finished = True

    while finished:
        #реагирование на клаиатуру для начала игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = False
                finished = False
            elif event.type == pygame.KEYDOWN:
                x = True
                finished = False
        pygame.display.flip()
        clock.tick(FPS)
        

start_screen() 
