import pygame

def init_minimap(map, room_x, room_y, room):
    # pygame.draw.rect(room, "Grey", (1075, 15, 200, 200))

    for i in range(10):
        for j in range(10):
            if map[i][j] == 1:
                pygame.draw.rect(room, "Black", (1075 + (j + 1) * 20, 15 + (i + 1) * 20, 17, 17))