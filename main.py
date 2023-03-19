import pygame
from room_gen import rand_map, room_choose

WIDTH = 1280
HEIGHT = 768


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # flags = pygame.NOFRAME
pygame.display.set_caption("FEFUgame")
icon = pygame.image.load("img/icons/icon100.png")
pygame.display.set_icon(icon)


player = pygame.image.load("img/players/dimochka.png")


player1_x = 540
player1_y = 300

player_hitbox = player.get_rect(topleft = (player1_x, player1_y))


player_speed = 0.5
player_speed_diag = 0.4

room_x = 4
room_y = 4
map = rand_map()
room = pygame.image.load(room_choose(map, room_x, room_y))


running = True
while running:

    screen.fill("Grey")

    # Room changing
    if player1_x < 226 and map[room_x][room_y - 1] == 1:
            room_y -= 1
            room = pygame.image.load(room_choose(map, room_x, room_y))
            player1_x = 965
            player1_y = 408
    if player1_x > 1000 and map[room_x][room_y + 1] == 1:
            room_y += 1
            room = pygame.image.load(room_choose(map, room_x, room_y))
            player1_x = 258
            player1_y = 418
    if player1_y < 195 and map[room_x - 1][room_y] == 1:
            room_x -= 1
            room = pygame.image.load(room_choose(map, room_x, room_y))
            player1_x = 611
            player1_y = 603
    if player1_y > 640 and map[room_x + 1][room_y] == 1:
            room_x += 1
            room = pygame.image.load(room_choose(map, room_x, room_y))
            player1_x = 604
            player1_y = 224

    screen.blit(room, (0, 0))

    


    screen.blit(player, (player1_x, player1_y))

    

    # Player moving
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and keys[pygame.K_a]:
        if (player1_x > 246 or (player1_y > 378 and player1_y + player_hitbox.height < 510)) and (player1_y > 222 or (player1_x > 574 and player1_x + player_hitbox.width < 708)):
            player1_x -= player_speed_diag
            player1_y -= player_speed_diag
    elif keys[pygame.K_a] and keys[pygame.K_s]:
        if (player1_x > 246 or (player1_y > 378 and player1_y + player_hitbox.height < 510)) and (player1_y < 614 or (player1_x > 574 and player1_x + player_hitbox.width < 708)):
            player1_x -= player_speed_diag
            player1_y += player_speed_diag
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        if (player1_y < 614 or (player1_x > 574 and player1_x + player_hitbox.width < 708)) and (player1_x < 970 or (player1_y > 378 and player1_y + player_hitbox.height < 510)):
            player1_x += player_speed_diag
            player1_y += player_speed_diag
    elif keys[pygame.K_d] and keys[pygame.K_w]:
        if (player1_x < 970 or (player1_y > 378 and player1_y + player_hitbox.height < 510)) and (player1_y > 222 or (player1_x > 574 and player1_x + player_hitbox.width < 708)):
            player1_x += player_speed_diag
            player1_y -= player_speed_diag

    elif keys[pygame.K_a]:
        if player1_x > 246 or (player1_y > 378 and player1_y + player_hitbox.height < 510):
            player1_x -= player_speed
    elif keys[pygame.K_d]:
        if player1_x < 970 or (player1_y > 378 and player1_y + player_hitbox.height < 510):
            player1_x += player_speed
    elif keys[pygame.K_s]:
        if player1_y < 614 or (player1_x > 574 and player1_x + player_hitbox.width < 708):
            player1_y += player_speed
    elif keys[pygame.K_w]:
        if player1_y > 222 or (player1_x > 574 and player1_x + player_hitbox.width < 708):
            player1_y -= player_speed


    # print(player1_x, player1_y)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
            