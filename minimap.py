import pygame

def init_minimap(map, room):
    # pygame.draw.rect(room, "Grey", (1075, 15, 200, 200))

    for i in range(10):
        for j in range(10):
            if map[i][j] in range(1, 3):
                pygame.draw.rect(room, "Black", (1075 + (j + 1) * 20, 15 + (i + 1) * 20, 17, 17))

def minimap_player(map, room):
    for i in range(10):
        for j in range(10):
            if map[i][j] == 2:
                pygame.draw.rect(room, "Green", (1078 + (j + 1) * 20, 18 + (i + 1) * 20, 11, 11))