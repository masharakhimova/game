import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна игры
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Рогалик")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Определение размеров и положений объектов
player_size = 40
player_pos = [random.randint(50, width-50), random.randint(50, height-50)]
enemy_size = 50
enemy_pos = [random.randint(50, width-50), random.randint(50, height-50)]
treasure_size = 20
treasure_pos = [random.randint(50, width-50), random.randint(50, height-50)]

# Определение переменной здоровья
player_health = 100
enemy_health = 50

# Определение скорости игрока
player_speed = 10

# Определение переменной для проверки коллизий
collision = False

# Основной игровой цикл
game_over = False
while not game_over:
    # Для каждого события в игре
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        # Управление игроком с клавиатуры
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_speed
            elif event.key == pygame.K_UP:
                player_pos[1] -= player_speed
            elif event.key == pygame.K_DOWN:
                player_pos[1] += player_speed

    # Обновление экрана
    screen.fill(BLACK)

    # Отображение игрока
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))

    # Отображение врага
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # Отображение сундука
    pygame.draw.rect(screen, GREEN, (treasure_pos[0], treasure_pos[1], treasure_size, treasure_size))

    # Отображение здоровья игрока и врага
    font = pygame.font.Font(None, 24)
    player_health_text = font.render("Здоровье: " + str(player_health), True, WHITE)
    enemy_health_text = font.render("Здоровье врага: " + str(enemy_health), True, WHITE)
    screen.blit(player_health_text, (10, 10))
    screen.blit(enemy_health_text, (10, 40))

    # Проверка столкновений игрока с врагом
    if player_pos[0] > enemy_pos[0] - player_size and player_pos[0] < enemy_pos[0] + enemy_size:
        if player_pos[1] > enemy_pos[1] - player_size and player_pos[1] < enemy_pos[1] + enemy_size:
            if enemy_health < player_health:
                enemy_health -= 10
            else:
                player_health -= 10
    
    # Проверка коллизий игрока с сундуком
    if player_pos[0] > treasure_pos[0] - player_size and player_pos[0] < treasure_pos[0] + treasure_size:
        if player_pos[1] > treasure_pos[1] - player_size and player_pos[1] < treasure_pos[1] + treasure_size:
            # Действие по сбору сокровища
            print("Сундук найден!")

    # Обновление экрана
    pygame.display.update()

# Закрытие Pygame
pygame.quit()
