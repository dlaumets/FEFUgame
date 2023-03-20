import pygame
from room_gen import rand_map, room_choose
from minimap import init_minimap, minimap_player
from hero import Hero


WIDTH = 1280
HEIGHT = 768


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # flags = pygame.NOFRAME
pygame.display.set_caption("FEFUgame")
icon = pygame.image.load("img/icons/icon100.png")
pygame.display.set_icon(icon)


player_texture = pygame.image.load("img/players/dimochka.png")


player = Hero(player_texture, None, None, None, 0.6, 0.4, None, 540, 300)
player.hitbox = player_texture.get_rect(topleft = (player.x, player.y))






room_x = 4
room_y = 4
map = rand_map()
room = pygame.image.load(room_choose(map, room_x, room_y))


running = True
while running:

    
    init_minimap(map, room)
    minimap_player(map, room)

    # Room changing
    if player.x < 226 and map[room_x][room_y - 1] in range(1, 3):
            map[room_x][room_y] = 1
            map[room_x][room_y - 1] = 2
            room_y -= 1
            room = pygame.image.load(room_choose(map, room_x, room_y))
            player.x = 965
            player.y = 408
            minimap_player(map, room)


    if player.x > 1000 and map[room_x][room_y + 1] in range(1, 3):
            map[room_x][room_y] = 1
            map[room_x][room_y + 1] = 2
            room_y += 1
            room = pygame.image.load(room_choose(map, room_x, room_y))
            player.x = 258
            player.y = 418
            minimap_player(map, room)

    if player.y < 195 and map[room_x - 1][room_y] in range(1, 3):
            map[room_x][room_y] = 1
            map[room_x - 1][room_y] = 2
            room_x -= 1
            room = pygame.image.load(room_choose(map, room_x, room_y))
            player.x = 611
            player.y = 603
            minimap_player(map, room)

    if player.y > 640 and map[room_x + 1][room_y] in range(1, 3):
            map[room_x][room_y] = 1
            map[room_x + 1][room_y] = 2
            room_x += 1
            room = pygame.image.load(room_choose(map, room_x, room_y))
            player.x = 604
            player.y = 224
            minimap_player(map, room)

    screen.blit(room, (0, 0))

    

    screen.blit(player.texture, (player.x, player.y))


    

    # Player moving
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and keys[pygame.K_a]:
        if (player.x > 246 or (player.y > 378 and player.y + player.hitbox.height < 510)) and (player.y > 222 or (player.x > 574 and player.x + player.hitbox.width < 708)):
            player.x -= player.diagonal_speed
            player.y -= player.diagonal_speed
    elif keys[pygame.K_a] and keys[pygame.K_s]:
        if (player.x > 246 or (player.y > 378 and player.y + player.hitbox.height < 510)) and (player.y < 614 or (player.x > 574 and player.x + player.hitbox.width < 708)):
            player.x -= player.diagonal_speed
            player.y += player.diagonal_speed
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        if (player.y < 614 or (player.x > 574 and player.x + player.hitbox.width < 708)) and (player.x < 970 or (player.y > 378 and player.y + player.hitbox.height < 510)):
            player.x += player.diagonal_speed
            player.y += player.diagonal_speed
    elif keys[pygame.K_d] and keys[pygame.K_w]:
        if (player.x < 970 or (player.y > 378 and player.y + player.hitbox.height < 510)) and (player.y > 222 or (player.x > 574 and player.x + player.hitbox.width < 708)):
            player.x += player.diagonal_speed
            player.y -= player.diagonal_speed

    elif keys[pygame.K_a]:
        if player.x > 246 or (player.y > 378 and player.y + player.hitbox.height < 510):
            player.x -= player.speed
    elif keys[pygame.K_d]:
        if player.x < 970 or (player.y > 378 and player.y + player.hitbox.height < 510):
            player.x += player.speed
    elif keys[pygame.K_s]:
        if player.y < 614 or (player.x > 574 and player.x + player.hitbox.width < 708):
            player.y += player.speed
    elif keys[pygame.K_w]:
        if player.y > 222 or (player.x > 574 and player.x + player.hitbox.width < 708):
            player.y -= player.speed


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
            