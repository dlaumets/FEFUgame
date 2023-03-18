import pygame
from room_gen import rand_map
# from map_hitbox import map_lines

pygame.init()
screen = pygame.display.set_mode((1280, 768)) # flags = pygame.NOFRAME
pygame.display.set_caption("FEFUgame")
icon = pygame.image.load("img/icons/icon100.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("img/rooms/urdl.jpeg")
player = pygame.image.load("img/players/dimochka.png")
# vanechka = pygame.image.load("img/players/vanechka.png")


player1_x = 540
player1_y = 300

player_hitbox = player.get_rect(topleft = (player1_x, player1_y))

# player2_x = 340
# player2_y = 100

player_speed = 0.5
player_speed_diag = 0.4


running = True
while running:

    screen.fill("Grey")
    screen.blit(bg, (0, 0))

    lines = [pygame.draw.rect(bg, "RED", (230, 160, 346, 32)),
        pygame.draw.rect(bg, "RED", (707, 160, 346, 32)),
        pygame.draw.rect(bg, "RED", (230, 670, 346, 32)),
        pygame.draw.rect(bg, "RED", (707, 670, 346, 32)),
        pygame.draw.rect(bg, "RED", (230, 160, 32, 220)),
        pygame.draw.rect(bg, "RED", (1028, 160, 32, 220)),
        pygame.draw.rect(bg, "RED", (230, 510, 32, 190)),
        pygame.draw.rect(bg, "RED", (1028, 510, 32, 190))]

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
        player1_x -= player_speed 
    elif keys[pygame.K_d]:
        player1_x += player_speed
    elif keys[pygame.K_s]:
        player1_y += player_speed
    elif keys[pygame.K_w]:
        player1_y -= player_speed




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
            