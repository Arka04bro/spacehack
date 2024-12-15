import pygame
import random
import math
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("C:/Users/Arkats/Downloads/34i_dj2019_spacexdragonart_live.jpg")  # Путь к иконке
pygame.display.set_icon(icon)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
background = pygame.image.load("C:/Users/Arkats/Downloads/beautiful-space-background-vector.jpg")  # Путь к файлу фона
player_img = pygame.image.load("C:/Users/Arkats/Downloads/34i_dj2019_spacexdragonart_live.jpg")
player_x = SCREEN_WIDTH / 2 - 32
player_y = SCREEN_HEIGHT - 100
player_x_change = 0
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('C:/Users/Arkats/Downloads/34i_dj2019_spacexdragonart_live.jpg'))  # Путь к изображению врага
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 64))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(2)
    enemy_y_change.append(40)

laser_img = pygame.image.load("C:/Users/Arkats/Downloads/360_F_484676675_JlKtR3qt4MjxpGDfFbBNgMKDgbH8sECY.jpg")  # Путь к изображению лазера
laser_x = 0
laser_y = player_y
laser_y_change = 10
laser_state = "ready"

# Счет
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

pygame.mixer.music.load("C:/Users/Arkats/Downloads/motivational-background-corporate-city-273359.mp3")  # Фоновые звуки
pygame.mixer.music.play(-1)
bullet_sound = pygame.mixer.Sound("C:/Users/Arkats/Downloads/attack-laser-128280.mp3")
explosion_sound = pygame.mixer.Sound("C:/Users/Arkats/Downloads/attack-laser-128280.mp3")
def show_score(x, y):
    score = font.render(f"Score : {score_value}", True, WHITE)
    screen.blit(score, (x, y))
def player(x, y):
    screen.blit(player_img, (x, y))
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))
def fire_laser(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laser_img, (x + 16, y + 10))


def is_collision(enemy_x, enemy_y, laser_x, laser_y):
    distance = math.sqrt(math.pow(enemy_x - laser_x, 2) + math.pow(enemy_y - laser_y, 2))
    return distance < 27

running = True
while running:

    screen.fill(BLACK)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Движение игрока
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if laser_state == "ready":
                    laser_x = player_x
                    fire_laser(laser_x, laser_y)
                    bullet_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= SCREEN_WIDTH - 64:
        player_x = SCREEN_WIDTH - 64
    for i in range(num_of_enemies):
        if enemy_y[i] > SCREEN_HEIGHT - 120:
            for j in range(num_of_enemies):
                enemy_y[j] = SCREEN_HEIGHT + 1
            running = False

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 2
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= SCREEN_WIDTH - 64:
            enemy_x_change[i] = -2
            enemy_y[i] += enemy_y_change[i]
        collision = is_collision(enemy_x[i], enemy_y[i], laser_x, laser_y)
        if collision:
            explosion_sound.play()
            laser_y = player_y
            laser_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemy_y[i] = random.randint(50, 150)
        enemy(enemy_x[i], enemy_y[i], i)
    if laser_state == "fire":
        fire_laser(laser_x, laser_y)
        laser_y -= laser_y_change
    if laser_y <= 0:
        laser_y = player_y
        laser_state = "ready"
    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()
pygame.quit()
