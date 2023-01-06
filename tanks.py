from os import path
import pygame
import model
import viewnew















if __name__ == "__main__":
    pygame.init()
    map_folder = "maps"
    map_file_name = "map_1.txt"
    map_full_name = (path.join(map_folder, map_file_name))
    width = 1100
    height = 700
    fps = 1
    field = model.Field(map_full_name)
    window = viewnew.Window(width, height, field)
    clock = pygame.time.Clock()


    print(field.landscape)
    window.update()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # screen.fill(BLACK)
                done = True
        window.update()
        clock.tick(fps)


