import pygame
from class_files.game import Game
from class_files.classes import Player
import time



class Interface():
    def print_text(screen, message, x, y, font_color=(0, 0, 0), font_type = "", font_size = 0):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        screen.blit(text, (x, y))


    class minimap():
        def room_minimap(map, room):
            # pygame.draw.rect(room, "Grey", (1075, 15, 200, 200))

            for i in range(10):
                for j in range(10):
                    if map[i][j] in range(1, 3):
                        pygame.draw.rect(room, "Black", (1075 + (j + 1) * 20, 15 + (i + 1) * 20, 17, 17))

        def player_minimap(map, room):
            for i in range(10):
                for j in range(10):
                    if map[i][j] == 2:
                        pygame.draw.rect(room, "Green", (1078 + (j + 1) * 20, 18 + (i + 1) * 20, 11, 11))

    class room():
        D = "img/rooms/d.jpeg"
        DL = "img/rooms/dl.jpeg"
        L = "img/rooms/l.jpeg"
        R = "img/rooms/r.jpeg"
        RD = "img/rooms/rd.jpeg"
        RDL = "img/rooms/rdl.jpeg"
        RL = "img/rooms/rl.jpeg"
        U = "img/rooms/u.jpeg"
        UD = "img/rooms/ud.jpeg"
        UDL = "img/rooms/udl.jpeg"
        UL = "img/rooms/ul.jpeg"
        UR = "img/rooms/ur.jpeg"
        URD = "img/rooms/urd.jpeg"
        URL = "img/rooms/url.jpeg"
        URDL = "img/rooms/urdl.jpeg"

        def room_changing(player, map, room_x, room_y, room): 

            if player.x < 226 and map[room_x][room_y - 1] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x][room_y - 1] = 2
                room_y -= 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 965
                player.y = 408
                Interface.minimap.player_minimap(map, room)


            if player.x > 1000 and map[room_x][room_y + 1] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x][room_y + 1] = 2
                room_y += 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 258
                player.y = 418
                Interface.minimap.player_minimap(map, room)

            if player.y < 195 and map[room_x - 1][room_y] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x - 1][room_y] = 2
                room_x -= 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 611
                player.y = 603
                Interface.minimap.player_minimap(map, room)


            if player.y > 640 and map[room_x + 1][room_y] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x + 1][room_y] = 2
                room_x += 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 604
                player.y = 224
                Interface.minimap.player_minimap(map, room)

            
            return room, room_x, room_y
        


    class menu():

        def main_menu(screen, running):
            FPS = 15
            direct_y = 1
            clock = pygame.time.Clock()

            menu = pygame.image.load("img/menu/main_menu.jpg")
            y = 540
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                
                clock.tick(FPS)
                screen.blit(menu, (0, 0))
                Interface.print_text(screen, "The Legend of ACSiE", 800, 70, "Brown", "fonts/FerdinandFont-Regular.ttf", 45)
                Interface.print_text(screen, "Tears of students", 860, 120, "Brown", "fonts/FerdinandFont-Regular.ttf", 35)


                Interface.print_text(screen, "Press SPACE to START", 430, y, "Grey", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 45) 
                y += direct_y

                if y > 545 or y < 535:
                    direct_y = -direct_y

                pygame.display.update()

                

                

    class game():
        def main_game(screen, room_x, room_y, running):
            player_texture = pygame.image.load("img/players/dimochka.png")

            player = Player(player_texture, None, None, None, 0.6, 0.4, None, 540, 300)
            player.hitbox = player_texture.get_rect(topleft = (player.x, player.y))

            map = Game.map.rand_map()
            room = pygame.image.load(Game.map.room_choose(map, room_x, room_y))

            while running:

                
                Interface.minimap.room_minimap(map, room)
                Interface.minimap.player_minimap(map, room)

                room, room_x, room_y = Interface.room.room_changing(player, map, room_x, room_y, room)

                screen.blit(room, (0, 0))

                screen.blit(player.texture, (player.x, player.y))
                Player.moving(player)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()

