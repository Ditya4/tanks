import pygame
from time import time


class CheckEvents:

    def __init__(self):
        self.player = None
        self.field = None

    def check_events(self, event, player, field, keys):
        '''
        we need keys here to check at the moment of pygame.KEYUP is there
        some pressed keys, if so we need to change speed for that key.
        '''
        self.player = player
        self.field = field
        self.event = event
        self.keys = keys
        if event.type == pygame.KEYDOWN:
            # if (self.player.vertical_speed != 0 and
            #         self.player.horizontal_speed != 0):

            if self.player.vertical_speed == 0:
                if event.key == pygame.K_LEFT:
                    self.player.change_speed(-5, 0)
                    self.player.direction = "left"
                if event.key == pygame.K_RIGHT:
                    self.player.direction = "right"
                    self.player.change_speed(5, 0)

            if self.player.horizontal_speed == 0:
                if event.key == pygame.K_UP:
                    self.player.direction = "up"
                    self.player.change_speed(0, -5)
                if event.key == pygame.K_DOWN:
                    self.player.direction = "down"
                    self.player.change_speed(0, 5)

        if event.type == pygame.KEYUP:
            # self.player.change_speed(0, 0)

            if event.key == pygame.K_LEFT:
                if self.player.horizontal_speed == -5:
                    self.player.change_speed(5, 0)
                    print("keys[pygame.K_LEFT] is", keys[pygame.K_LEFT],
                          "len(keys) =",
                          len(list(filter(lambda x: x is True, keys))))
                    if (self.key_down(keys, "left") != (0, 0) and
                            len(list(filter(lambda x: x is True, keys))) == 2):
                        # print(self.key_down(keys))
                        self.player.change_speed(*self.key_down(keys, "left"))

            if event.key == pygame.K_RIGHT:
                if self.player.horizontal_speed == 5:
                    self.player.change_speed(-5, 0)
                    print(self.key_down(keys, "right"))
                    if (self.key_down(keys, "right") != (0, 0) and
                            len(list(filter(lambda x: x is True, keys))) == 2):
                        self.player.change_speed(
                            *self.key_down(keys, "right"))

            if event.key == pygame.K_UP:
                if self.player.vertical_speed == -5:
                    self.player.change_speed(0, 5)
                    print(self.key_down(keys, "up"))
                    if (self.key_down(keys, "up") != (0, 0) and
                            len(list(filter(lambda x: x is True, keys))) == 2):
                        self.player.change_speed(*self.key_down(keys, "up"))
                    '''
                    if any(self.keys):
                        self.player.change_speed(self.key_down(keys))
                    '''
            if event.key == pygame.K_DOWN:
                if self.player.vertical_speed == 5:
                    self.player.change_speed(0, -5)
                    print(self.key_down(keys, "down"))
                    if (self.key_down(keys, "down") != (0, 0) and
                            len(list(filter(lambda x: x is True, keys))) == 2):
                        # print(self.key_down(keys))
                        self.player.change_speed(*self.key_down(keys, "down"))

    def key_down(self, keys, upped_key):
        '''
        this method is calling during KEYUP any arrow
        '''

        if self.keys[pygame.K_LEFT] and upped_key != "left":
            self.player.direction = "left"
            return -5, 0
        elif keys[pygame.K_RIGHT] and upped_key != "right":
            self.player.direction = "right"
            return 5, 0
        elif keys[pygame.K_UP] and upped_key != "up":
            self.player.direction = "up"
            return 0, -5
        elif keys[pygame.K_DOWN] and upped_key != "down":
            self.player.direction = "down"
            return 0, 5
        else:
            return 0, 0

    def check_pressed_keys(self, keys, player, field):
        self.keys = keys
        self.player = player
        self.field = field
        button_press_delta = 0.2
        left_button_pressed = 0
        right_button_pressed = 0
        up_button_pressed = 0
        down_button_pressed = 0

        if self.keys[pygame.K_LEFT]:
            if not left_button_pressed:
                if self.can_move():
                    self.move()
                left_button_pressed = 1
                left_button_pressed_time_start = time()
            if left_button_pressed:
                left_button_pressed_time = (
                    time() - left_button_pressed_time_start)
                if left_button_pressed_time > button_press_delta:
                    if self.can_move():
                        self.move()
                    left_button_pressed_time_start = time()

        elif keys[pygame.K_RIGHT]:
            if not right_button_pressed:
                if self.can_move():
                    self.move()
                right_button_pressed = 1
                right_button_pressed_time_start = time()
            if right_button_pressed:
                right_button_pressed_time = (
                    time() - right_button_pressed_time_start)
                if right_button_pressed_time > button_press_delta:
                    if self.can_move():
                        self.move()
                    right_button_pressed_time_start = time()

        elif keys[pygame.K_UP]:
            if not up_button_pressed:
                if self.can_move():
                    self.move()
                up_button_pressed = 1
                up_button_pressed_time_start = time()
            if up_button_pressed:
                up_button_pressed_time = (
                    time() - up_button_pressed_time_start)
                if up_button_pressed_time > button_press_delta:
                    if self.can_move():
                        self.move()
                    up_button_pressed_time_start = time()

        elif keys[pygame.K_DOWN]:
            if not down_button_pressed:
                if self.can_move():
                    self.move()
                down_button_pressed = 1
                down_button_pressed_time_start = time()
            if down_button_pressed:
                down_button_pressed_time = (
                    time() - down_button_pressed_time_start)
                if down_button_pressed_time > button_press_delta * 3:
                    if self.can_move():
                        self.move()
                    down_button_pressed_time_start = time()

    def can_move(self):
        return True

    def move(self):
        if self.player.vertical_speed:
            self.player.top += self.player.vertical_speed
        if self.player.horizontal_speed:
            self.player.left += self.player.horizontal_speed
