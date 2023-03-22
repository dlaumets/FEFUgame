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
lenin = pygame.image.load("img/enemy/lenin..png")


player = classes.Player(player_texture, None, None, None, 0.6, 0.4, None, 540, 300)
player.hitbox = player_texture.get_rect(topleft = (player.x, player.y))


room_x = 4
room_y = 4


map = Game.map.rand_map()
room = pygame.image.load(Game.map.room_choose(map, 4, 4))


running = True
while running:

    
    Enterface.minimap.room_minimap(map, room)
    Enterface.minimap.player_minimap(map, room)


    room, room_x, room_y = Enterface.room.room_changing(player, map, room_x, room_y, room)

    screen.blit(room, (0, 0))

    print(player.x, player.y)

    screen.blit(player.texture, (player.x, player.y))


    classes.Player.moving(player)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
            