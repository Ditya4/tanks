import pygame
import numpy as np
from os import path


class BattleField:
    sprites_folder = "sprites"
    sprites_file_name = "battle city sprites.png"
    sprites_full_name = (path.join(sprites_folder, sprites_file_name))

    def __init__(self, size, canvas):
        self.size = size
        self.canvas = canvas
        self.sprites = pygame.image.load(self.sprites_full_name)


class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = pygame.display.set_mode((width, height))
        self.battle_field_height = self.height
        self.battle_field_width = self.width - 100
        self.battle_field_square_size = min(
            self.battle_field_height, self.battle_field_height)
        self.battle_field = BattleField(self.battle_field_square_size,
                                        self.canvas)


if __name__ == "__main__":
    width = 800
    height = 700
    window = Window(width, height)

