from os import path
import pygame
import model
import viewnew
import control


if __name__ == "__main__":
    pygame.init()
    map_folder = "maps"
    map_file_name = "map_1.txt"
    map_full_name = (path.join(map_folder, map_file_name))
    width = 1000
    height = 673
    texture_height = 28
    texture_width = 35
    player_start_left = 300
    player_start_top = 600
    player_direction = "up"
    fps = 60
    field = model.Field(map_full_name)
    player = model.Player(player_start_top, player_start_left,
                          player_direction)
    window = viewnew.Window(width, height,
                            texture_width, texture_height,
                            field, player)

    manage = control.CheckEvents()
    clock = pygame.time.Clock()

    # print(field.landscape)
    window.update()
    done = False
    while not done:
        # keys = pygame.key.get_pressed()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            manage.check_events(event, player, field, keys)
            # keys = pygame.key.get_pressed()
            # manage.check_events(keys, event, player, field)
        # print(player.vertical_speed, player.horizontal_speed)
        
        # print(keys)
        if any(keys):
            manage.check_pressed_keys(keys, player, field)

        # manage.check_events(keys, event, player, field)
        # keys = pygame.key.get_pressed()
        # manage.check_events(keys, event, player, field)
        window.update()
        clock.tick(fps)
