import pygame
import random
 
# Inicialização do Pygame
pygame.init()
 
# Configurações da janela do jogo
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")
 
# Cores
black = (0, 0, 0)
white = (255, 255, 255)
 
# Carregamento das imagens dos sprites
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("alien.png")
bullet_img = pygame.image.load("bullet.png")
barrier_img = pygame.image.load("barrier.png")
 
# Configurações do jogador
player_width = 64
player_height = 64
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_x_change = 0
 
# Configurações dos inimigos
enemy_width = 64
enemy_height = 64
enemy_x = random.randint(0, window_width - enemy_width)
enemy_y = 50
enemy_x_change = 3
enemy_y_change = 40
 
# Configurações dos projéteis
bullet_width = 32
bullet_height = 32
bullet_x = 0
bullet_y = player_y
bullet_y_change = 10
bullet_state = "ready"
 
# Configurações das barreiras de defesa
num_barriers = 4
barrier_width = 64
barrier_height = 48
barrier_y = window_height - player_height - barrier_height - 20
barrier_x_spacing = (window_width - num_barriers * barrier_width) // (num_barriers + 1)
barrier_list = []
for i in range(num_barriers):
    barrier_x = (i + 1) * barrier_x_spacing + i * barrier_width
    barrier_list.append([barrier_x, barrier_y])
 
def player(x, y):
    window.blit(player_img, (x, y))
 
def enemy(x, y):
    window.blit(enemy_img, (x, y))
 
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bullet_img, (x + player_width // 2 - bullet_width // 2, y))
 
def is_collision(obj1_x, obj1_y, obj1_width, obj1_height, obj2_x, obj2_y, obj2_width, obj2_height):
    if obj2_x + obj2_width >= obj1_x >= obj2_x and obj2_y + obj2_height >= obj1_y >= obj2_y:
        return True
    if obj2_x + obj2_width >= obj1_x + obj1_width >= obj2_x and obj2_y + obj2_height >= obj1_y >= obj2_y:
        return True
    if obj2_x + obj2_width >= obj1_x >= obj2_x and obj2_y + obj2_height >= obj1_y + obj1_height >= obj2_y:
        return True
    if obj2_x + obj2_width >= obj1_x + obj1_width >= obj2_x and obj2_y + obj2_height >= obj1_y + obj1_height >= obj2_y:
        return True
    return False
 
def show_message(text):
    font = pygame.font.Font("freesansbold.ttf", 32)
    message = font.render(text, True, white)
    window.blit(message, (window_width // 2 - message.get_width() // 2, window_height // 2 - message.get_height() // 2))
 
# Loop principal do jogo
running = True
game_over = False
while running:
    window.fill(black)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        # Controle do jogador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 5
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
 
    # Movimento do jogador
    player_x += player_x_change
    if player_x < 0:
        player_x = 0
    elif player_x > window_width - player_width:
        player_x = window_width - player_width
 
    # Movimento dos inimigos
    enemy_x += enemy_x_change
    if enemy_x < 0 or enemy_x > window_width - enemy_width:
        enemy_x_change = -enemy_x_change
        enemy_y += enemy_y_change
 
    # Movimento do projétil
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
 
    # Verifica colisão do projétil com o inimigo
    if is_collision(enemy_x, enemy_y, enemy_width, enemy_height, bullet_x, bullet_y, bullet_width, bullet_height):
        bullet_y = player_y
        bullet_state = "ready"
        enemy_x = random.randint(0, window_width - enemy_width)
        enemy_y = 50
 
    # Verifica colisão do jogador com os inimigos
    if is_collision(enemy_x, enemy_y, enemy_width, enemy_height, player_x, player_y, player_width, player_height):
        game_over = True
 
    # Verifica colisão do projétil com as barreiras de defesa
    for i in range(num_barriers):
        barrier_x, barrier_y = barrier_list[i]
        if is_collision(barrier_x, barrier_y, barrier_width, barrier_height, bullet_x, bullet_y, bullet_width, bullet_height):
            bullet_y = player_y
            bullet_state = "ready"
            barrier_list[i] = [-100, -100]  # Remove a barreira da lista
 
    # Desenho dos elementos na tela
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    for barrier in barrier_list:
        window.blit(barrier_img, barrier)
 
    # Verifica se o jogo acabou
    if game_over:
        show_message("Game Over")
        break
 
    pygame.display.update()
 
# Encerra o Pygame
pygame.quit()
 