'''
so... we read a map file 26 for 26 size with next file structure
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


class Field:

    def __init__(self, map_name):
        '''
        map_name - is path to map_file ready to use in open function.
        we have 26 x 26 battle landscape
        '''
        borders = 2
        self.size = 26 + borders
        self.map_name = map_name
        self.landscape = np.zeros((self.size, self.size), np.int32).reshape(
                              self.size, self.size)
        for i in range(self.size):
            self.landscape[0][i] = self.landscape[i][0] = (
                self.landscape[i][self.size - 1]) = (
                    self.landscape[self.size - 1][i]) = 125
        self.read_map()

    def read_map(self):
        '''
        cause of 2 fake rows and columns we make this ranges
        '''
        map_file = open(self.map_name)
        map_lines = map_file.readlines()
        for i in range(len(map_lines)):
            map_lines[i] = map_lines[i].rstrip("\n")
        print(map_lines)
        for y in range(0, self.size - 2):
            for x in range(0, self.size - 2):
                print(map_lines[y][x], end="")
                self.landscape[y + 1][x + 1] = ord(map_lines[y][x])
            print()


if __name__ == "__main__":
    map_folder = "maps"
    map_file_name = "map_1.txt"
    map_full_name = (path.join(map_folder, map_file_name))

    field = Field(map_full_name)
    print(field.landscape)

















