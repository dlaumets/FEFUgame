import pygame
import classes
from enterface import Enterface
from game import Game


WIDTH = 1280
HEIGHT = 768


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # flags = pygame.NOFRAME
pygame.display.set_caption("FEFUgame")
icon = pygame.image.load("img/icons/icon100.png")
pygame.display.set_icon(icon)


player_texture = pygame.image.load("img/players/dimochka.png")


player = classes.Player(player_texture, None, None, None, 0.6, 0.4, None, 540, 300)
player.hitbox = player_texture.get_rect(topleft = (player.x, player.y))





map = Game.map.rand_map()
room = pygame.image.load(Game.map.room_choose(map, Enterface.room.room_x, Enterface.room.room_y))


running = True
while running:
#   Enterface.Menu.menu()
#   if Enterface.Menu.menu():
    
    Enterface.minimap.room_minimap(map, room)
    Enterface.minimap.player_minimap(map, room)

    # Room changing
    if player.x < 226 and map[Enterface.room.room_x][Enterface.room.room_y - 1] in range(1, 3):
            map[Enterface.room.room_x][Enterface.room.room_y] = 1
            map[Enterface.room.room_x][Enterface.room.room_y - 1] = 2
            Enterface.room.room_y -= 1
            room = pygame.image.load(Game.map.room_choose(map, Enterface.room.room_x, Enterface.room.room_y))
            player.x = 965
            player.y = 408
            Enterface.minimap.player_minimap(map, room)


    if player.x > 1000 and map[Enterface.room.room_x][Enterface.room.room_y + 1] in range(1, 3):
            map[Enterface.room.room_x][Enterface.room.room_y] = 1
            map[Enterface.room.room_x][Enterface.room.room_y + 1] = 2
            Enterface.room.room_y += 1
            room = pygame.image.load(Game.map.room_choose(map, Enterface.room.room_x, Enterface.room.room_y))
            player.x = 258
            player.y = 418
            Enterface.minimap.player_minimap(map, room)

    if player.y < 195 and map[Enterface.room.room_x - 1][Enterface.room.room_y] in range(1, 3):
            map[Enterface.room.room_x][Enterface.room.room_y] = 1
            map[Enterface.room.room_x - 1][Enterface.room.room_y] = 2
            Enterface.room.room_x -= 1
            room = pygame.image.load(Game.map.room_choose(map, Enterface.room.room_x, Enterface.room.room_y))
            player.x = 611
            player.y = 603
            Enterface.minimap.player_minimap(map, room)


    if player.y > 640 and map[Enterface.room.room_x + 1][Enterface.room.room_y] in range(1, 3):
            map[Enterface.room.room_x][Enterface.room.room_y] = 1
            map[Enterface.room.room_x + 1][Enterface.room.room_y] = 2
            Enterface.room.room_x += 1
            room = pygame.image.load(Game.map.room_choose(map, Enterface.room.room_x, Enterface.room.room_y))
            player.x = 604
            player.y = 224
            Enterface.minimap.player_minimap(map, room)

    screen.blit(room, (0, 0))

    

    screen.blit(player.texture, (player.x, player.y))


    

    # Player moving
    classes.Player.moving(player)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
            