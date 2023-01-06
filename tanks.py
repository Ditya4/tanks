from os import path
import pygame
import model
import viewnew















if __name__ == "__main__":
    pygame.init()
    map_folder = "maps"
    map_file_name = "map_1.txt"
    map_full_name = (path.join(map_folder, map_file_name))
    width = 1000
    height = 673
    player_start_left = 300
    player_start_top = 600
    player_direction = "up"
    fps = 1
    field = model.Field(map_full_name)
    window = viewnew.Window(width, height, field)
    player = model.Player(player_start_top, player_start_left,
                          player_direction)
    clock = pygame.time.Clock()

    print(field.landscape)
    window.update()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        window.update()
        clock.tick(fps)


