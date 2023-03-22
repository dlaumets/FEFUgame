import pygame
from class_files.game import Game

class Interface():


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
                print(img)
                room = pygame.image.load(img)
                player.x = 965
                player.y = 408
                Interface.minimap.player_minimap(map, room)


            if player.x > 1000 and map[room_x][room_y + 1] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x][room_y + 1] = 2
                room_y += 1
                img = Game.map.room_choose(map, room_x, room_y)
                print(img)
                room = pygame.image.load(img)
                player.x = 258
                player.y = 418
                Interface.minimap.player_minimap(map, room)

            if player.y < 195 and map[room_x - 1][room_y] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x - 1][room_y] = 2
                room_x -= 1
                img = Game.map.room_choose(map, room_x, room_y)
                print(img)
                room = pygame.image.load(img)
                player.x = 611
                player.y = 603
                Interface.minimap.player_minimap(map, room)


            if player.y > 640 and map[room_x + 1][room_y] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x + 1][room_y] = 2
                room_x += 1
                img = Game.map.room_choose(map, room_x, room_y)
                print(img)
                room = pygame.image.load(img)

                player.x = 604
                player.y = 224
                Interface.minimap.player_minimap(map, room)

            
            return room, room_x, room_y