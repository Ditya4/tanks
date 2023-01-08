'''
so... we read a map file 24 for 24 size with next file structure
space for free, black space
33 _ascii code "!" for first image block
! - for first 5x5 image block 0, 0, 73, 80
34 _ascii code '"' for second image block
! - for first 5x5 image block 0, 73, 73, 80
lets create 2 fake rows and 2 fake columns for borders, where we will put some
unbreakable and unmovable objects(borders of map) zero and self.size + 1
indexes

'''
import pygame
import numpy as np
from os import path, getcwd


class Player:

    def __init__(self, top, left, direction):
        '''
        top, left - top, left border of the player _rect
        direction - direction in which the gun turned
        speed - constant speed of player moving
        stage - which tank type is our player visually
        tank_model - simple = 0, a bit better = 1, double bullet = 2,
        concrete smasher = 3
        ? cause we only move in direction, in which our payer turned, probably
        speed should be changed here, not in control.
        '''
        self.top = top
        self.left = left
        self.direction = direction
        self.tank_model = 0
        self.speed = 0
        self.stage = 0
        self.horizontal_speed = 0
        self.vertical_speed = 0

    def change_speed(self, horizontal, vertical):
        if horizontal and vertical:
            print("pressed bouth buttons")
            input()
        self.horizontal_speed += horizontal
        self.vertical_speed += vertical
        old_left = self.left
        self.left += self.horizontal_speed
        print("move horizontal with speed", self.horizontal_speed)
        if 1 != 1:
        # if pygame.sprite.spritecollideany(self, walls) is not None:
            self.left = old_left

        old_top = self.top
        self.top += self.vertical_speed
        if 1 != 1:
        # if pygame.sprite.spritecollideany(self, walls) is not None:
            self.top = old_top
        print("move vertical with speed", self.vertical_speed)


class Field:

    def __init__(self, map_name):
        '''
        map_name - is path to map_file ready to use in open function.
        we have 24 x 24 battle landscape
        '''
        self.borders = 2
        self.size = 24 + self.borders
        self.map_name = map_name
        self.landscape = np.zeros((self.size, self.size), np.int32).reshape(
                              self.size, self.size)
        ascii_for_border = 125
        for i in range(self.size):
            self.landscape[0][i] = self.landscape[i][0] = (
                self.landscape[i][self.size - 1]) = (
                    self.landscape[self.size - 1][i]) = ascii_for_border
        self.read_map()

    def read_map(self):
        '''
        cause of 2 fake rows and columns we make this ranges
        '''
        map_file = open(self.map_name)
        map_lines = map_file.readlines()
        for i in range(len(map_lines)):
            map_lines[i] = map_lines[i].rstrip("\n")
        # print(map_lines)
        for y in range(0, self.size - self.borders):
            for x in range(0, self.size - self.borders):
                # print(map_lines[y][x], end="")
                self.landscape[y + 1][x + 1] = ord(map_lines[y][x])
            # print()


if __name__ == "__main__":
    map_folder = "maps"
    map_file_name = "map_1.txt"
    map_full_name = (path.join(map_folder, map_file_name))

    field = Field(map_full_name)
    # print(field.landscape)

















