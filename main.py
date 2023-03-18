import pygame
from room_gen import rand_map

WIDTH = 1280
HEIGHT = 768


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # flags = pygame.NOFRAME
pygame.display.set_caption("FEFUgame")
icon = pygame.image.load("img/icons/icon100.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("img/rooms/urdl.jpeg")
player = pygame.image.load("img/players/dimochka.png")


player1_x = 540
player1_y = 300

player_hitbox = player.get_rect(topleft = (player1_x, player1_y))


player_speed = 0.5
player_speed_diag = 0.4


running = True
while running:

    screen.fill("Grey")
    screen.blit(bg, (0, 0))

    l1 = pygame.draw.line(bg, "Red", [256, 192], [574, 192])



    screen.blit(player, (player1_x, player1_y))

    


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and keys[pygame.K_a]:
        player1_x -= player_speed_diag
        player1_y -= player_speed_diag
    elif keys[pygame.K_a] and keys[pygame.K_s]:
        player1_x -= player_speed_diag
        player1_y += player_speed_diag
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        player1_x += player_speed_diag
        player1_y += player_speed_diag
    elif keys[pygame.K_d] and keys[pygame.K_w]:
        player1_x += player_speed_diag
        player1_y -= player_speed_diag

    elif keys[pygame.K_a]:
        if player1_x > 246:
            player1_x -= player_speed
    elif keys[pygame.K_d]:
        if player1_x < 970:
            player1_x += player_speed
    elif keys[pygame.K_s]:
        if player1_y < 614:
            player1_y += player_speed
    elif keys[pygame.K_w]:
        if player1_y > 192:
            player1_y -= player_speed



    print(player1_x, player1_y)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
            