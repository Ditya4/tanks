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
import numpy as np
from os import path


class Bullet:

    def __init__(self, direction, left, top):
        self.direction = direction
        self.left = left
        self.top = top
        self.speed = self.calculate_speed()
        self.textures = self.textures_coords()
        # first calling update method for move top_left to the direction,
        # where the end of barrel is.
        self.update()

    def calculate_speed(self):
        speeds = {"left": (-7, 0),
                  "right": (7, 0),
                  "up": (0, -7),
                  "down": (0, 7), }
        return speeds[self.direction]

    def textures_coords(self):
        images_dict = {"left": [172, 705],
                       "right": [172, 740],
                       "up": [172, 678],
                       "down": [172, 724], }
        return images_dict

    def update(self):
        self.left += self.speed[0]
        self.top += self.speed[1]


class TankModel:
    '''
    we create a _dict with next format
    ["left"] = {(55, 70), (90,70)}
    coordinates will be different for each model of tank
    also need to make a call method with direction as argument to
    return certain value of this _dict
    '''

    def __init__(self, model_index):
        self.model_index = model_index
        self.imges_dict = {}
        self.fill_images_dict()

    def fill_images_dict(self):

        if self.model_index == 0:
            self.images_dict = {"left": [[0, 68], [0, 102]],
                                "right": [[0, 204], [0, 238]],
                                "up": [[0, 0], [0, 34]],
                                "down": [[0, 136], [0, 170]], }

        elif self.model_index == 1:
            self.images_dict = {"left": [[28, 68], [28, 102]],
                                "right": [[28, 204], [28, 238]],
                                "up": [[28, 0], [28, 34]],
                                "down": [[28, 136], [28, 170]], }

    def __call__(self, direction):
        return self.images_dict[direction]


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
        TankModel will be _dict of lists of pairs top and left
        for moving images

        new one for every different tank_model_index.
        !!!
        i don't need direction, cause direction will be sended as
        parameter to the _dict to get image
        with keys of self.direction("left", "right") i
        '''
        self.top = top
        self.left = left
        self.direction = direction
        self.tank_model_index = 1
        self.tank_model = TankModel(self.tank_model_index)
        self.speed = 0
        self.stage = 0
        self.horizontal_speed = 0
        self.vertical_speed = 0

    def change_speed(self, horizontal_speed, vertical_speed):
        self.horizontal_speed += horizontal_speed
        self.vertical_speed += vertical_speed
        '''
        # if horizontal and vertical:
        if self.horizontal_speed and vertical:

            print("pressed bouth buttons")
            return
            # input()
        self.horizontal_speed += horizontal
        self.vertical_speed += vertical
        old_left = self.left
        self.left += self.horizontal_speed
        # print("move horizontal with speed", self.horizontal_speed)
        #  if pygame.sprite.spritecollideany(self, walls) is not None:
        if 1 != 1:
            self.left = old_left

        old_top = self.top
        self.top += self.vertical_speed
        # if pygame.sprite.spritecollideany(self, walls) is not None:
        if 1 != 1:
            self.top = old_top
        # print("move vertical with speed", self.vertical_speed)
        '''


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

















