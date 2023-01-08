import pygame


class CheckEvents:

    def __init__(self):
        pass

    def check_events(self, event, player, field):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_speed(-5, 0)
            if event.key == pygame.K_RIGHT:
                player.change_speed(5, 0)
            if event.key == pygame.K_UP:
                player.change_speed(0, -5)
            if event.key == pygame.K_DOWN:
                player.change_speed(0, 5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_speed(5, 0)
            if event.key == pygame.K_RIGHT:
                player.change_speed(-5, 0)
            if event.key == pygame.K_UP:
                player.change_speed(0, 5)
            if event.key == pygame.K_DOWN:
                player.change_speed(0, -5)
