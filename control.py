import pygame
from time import time


class CheckEvents:

    def __init__(self):
        self.player = None
        self.field = None

    def check_events(self, event, player, field):
        self.player = player
        self.field = field
        self.event = event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.change_speed(-5, 0)
                self.player.direction = "left"
            elif event.key == pygame.K_RIGHT:
                self.player.direction = "right"
                self.player.change_speed(5, 0)
            elif event.key == pygame.K_UP:
                self.player.direction = "up"
                self.player.change_speed(0, -5)
            elif event.key == pygame.K_DOWN:
                self.player.direction = "down"
                self.player.change_speed(0, 5)

        if event.type == pygame.KEYUP:
            # self.player.change_speed(0, 0)

            if event.key == pygame.K_LEFT:
                self.player.change_speed(5, 0)
            elif event.key == pygame.K_RIGHT:
                self.player.change_speed(-5, 0)
            elif event.key == pygame.K_UP:
                self.player.change_speed(0, 5)
            elif event.key == pygame.K_DOWN:
                self.player.change_speed(0, -5)
            

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

    '''
    def check_events(self, keys, event, player, field):
        self.keys = keys
        self.player = player
        self.field = field
        self.event = event
        button_press_delta = 0.2
        left_button_pressed = 0
        right_button_pressed = 0
        up_button_pressed = 0
        down_button_pressed = 0




        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.change_speed(-5, 0)
                self.player.direction = "left"
        
            elif event.key == pygame.K_RIGHT:
                self.player.direction = "right"
                self.player.change_speed(5, 0)
            elif event.key == pygame.K_UP:
                self.player.direction = "up"
                self.player.change_speed(0, -5)
            elif event.key == pygame.K_DOWN:
                self.player.direction = "down"
                self.player.change_speed(0, 5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player.change_speed(5, 0)
            elif event.key == pygame.K_RIGHT:
                self.player.change_speed(-5, 0)
            elif event.key == pygame.K_UP:
                self.player.change_speed(0, 5)
            elif event.key == pygame.K_DOWN:
                self.player.change_speed(0, -5)

                
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
    '''
    def can_move(self):
        return True

    def move(self):
        if self.player.vertical_speed:
            self.player.top += self.player.vertical_speed
        if self.player.horizontal_speed:
            self.player.left += self.player.horizontal_speed