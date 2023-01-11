import pygame
from os import path
from random import choice


class Player(pygame.sprite.Sprite):

    def __init__(self, model_player, window):
        '''
        For start we'll take any texture tank picture but later it's going to
        change, during moving and player direction.
        '''
        self.player_texture_left = 0
        self.player_texture_top = 0

        super().__init__()

        self.model_player = model_player
        self.window = window
        self.canvas = self.window.canvas
        self.width = self.window.texture_width
        self.height = self.window.texture_height

        self.player_group = pygame.sprite.Group()
        self.update()

        '''
        self.texture_group = pygame.sprite.Group()
        self.texture_image = window.texture_image
        self.update()
        '''

        '''
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self)
        '''

    def update(self):
        '''
        first if-else make a change image of player in dependence of
        player direction and moving visualization
        '''
        # print(self.model_player.tank_model(self.model_player.direction))
        if (self.model_player.vertical_speed or
                self.model_player.horizontal_speed):
            random_image = choice([0, 1])
            self.player_texture_left = self.model_player.tank_model(
                self.model_player.direction)[random_image][1]
            self.player_texture_top = self.model_player.tank_model(
                self.model_player.direction)[random_image][0]
        else:
            self.player_texture_left = (
                self.model_player.tank_model(
                    self.model_player.direction)[0][1])
            self.player_texture_top = (
                self.model_player.tank_model(
                    self.model_player.direction)[0][0])

        self.player_group = pygame.sprite.Group()
        self.image = pygame.Surface([self.width, self.height])

        self.player_texture = Texture(
            self.model_player.top, self.model_player.left,
            (self.player_texture_top, self.player_texture_left),
            self.window.texture_image, self.window)
        self.player_group.add(self.player_texture)
        self.rect = self.image.get_rect()
        # x, y = pygame.mouse.get_pos()
        # self.model_player.top = y
        # self.model_player.left = x
        self.rect.top = self.model_player.top + 4
        self.rect.left = self.model_player.left + 4
        self.rect.height = self.window.texture_height - 4
        self.rect.width = self.window.texture_width - 4
        self.player_group.draw(self.canvas)

        # self.player_group.draw(self.canvas)


class Texture(pygame.sprite.Sprite):

    def __init__(self, y, x, texture_top_left, texture, window):
        '''
        y, x where we need to draw a texture
        texture_top_left - (top, left) where we need to take texture from
        texture_image - image with all textures

        '''
        super().__init__()
        self.window = window
        self.image = pygame.Surface([self.window.texture_width,
                                     self.window.texture_height])  # .convert()
        self.image.blit(texture, (0, 0), (texture_top_left[1],
                                          texture_top_left[0],
                                          self.window.texture_width,
                                          self.window.texture_height))
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


class Statistic:

    def __init__(self, width, height, left, canvas):
        '''
        this class for score, tanks remaining, life remaining
        '''
        pass

    def update(self):
        pass


class Battlefield:

    def __init__(self, width, height, window, model_field):
        '''
        not_passable_texture_group(brick, concrete, borders)
        '''
        self.width = width
        self.height = height
        self.window = window
        self.canvas = window.canvas
        self.model_field = model_field
        self.texture_dict = {}
        self.fill_texture_dict()
        self.first_call_for_read_borders = True

        # self.texture_group = pygame.sprite.Group()  # erase

        self.texture_group_under_player = pygame.sprite.Group()
        self.texture_group_over_player = pygame.sprite.Group()

        self.borders_texture_group = pygame.sprite.Group()
        self.not_passable_texture_group = pygame.sprite.Group()

        self.texture_image = window.texture_image
        self.update()

    # def get_texture_image(self):
        '''
        sprites_folder = "sprites"
        sprites_file_name = "battle city sprites upsized.png"
        sprites_full_name = (path.join(sprites_folder,
                                       sprites_file_name))
        texture = pygame.image.load(sprites_full_name).convert()
        return texture
        '''
        # pass

    def fill_texture_dict(self):
        '''
        data format:
        1. just some name
        2. _ascii symbol in file
        3. top border of texture
        4. left border of texture
        5. could player move over this texture(True/False)
        6. does this texture should be drawn under tank(ice, water) or
           over tank(trees)(True - under/False - over)
        '''
        texture_data_list = [["brick", "!", 0, 550, False, True],
                             ["grass", ",", 58, 585, True, False],
                             ["water_1", "+", 58, 550, True, True], ]

        for texture_data in texture_data_list:
            self.texture_dict[texture_data[1]] = (texture_data[2],
                                                  texture_data[3],
                                                  texture_data[4],
                                                  texture_data[5], )

    def update(self):
        self.not_passable_texture_group.empty()
        self.texture_group_under_player.empty()
        self.texture_group_over_player.empty()

        # self.texture_group.empty()  # erase
        for y in range(self.model_field.size):
            for x in range(self.model_field.size):
                # next condition not space symbol and border symbol
                if self.model_field.landscape[y][x] not in (32, 125):
                    if chr(self.model_field.landscape[y][x]) in (
                            self.texture_dict):
                        # print(y, x, self.model_field.landscape[y][x])

                        texture = Texture(
                            (y - 1) * self.window.texture_height,
                            (x - 1) * self.window.texture_width,
                            self.texture_dict[chr(
                                self.model_field.landscape[y][x])][:2],
                            self.texture_image, self.window)

                        if self.texture_dict[chr(
                                self.model_field.landscape[y][x])][3]:
                            self.texture_group_under_player.add(texture)
                        else:
                            self.texture_group_over_player.add(texture)

                        if not self.texture_dict[chr(
                                    self.model_field.landscape[y][x])][2]:
                            self.not_passable_texture_group.add(texture)
                if (self.first_call_for_read_borders and
                        self.model_field.landscape[y][x] == 125):
                    texture = Texture(
                            (y - 1) * self.window.texture_height,
                            (x - 1) * self.window.texture_width,
                            [0, 0],
                            self.texture_image, self.window)
                    self.borders_texture_group.add(texture)
        self.first_call_for_read_borders = False

                        # self.texture_group.add(texture)  # erase
        # self.texture_group.draw(self.canvas)  # erase

    def draw_under(self):
        self.texture_group_under_player.draw(self.canvas)

    def draw_over(self):
        self.texture_group_over_player.draw(self.canvas)

    def can_move_horizontal(self, model_player):
        player = self.window.player
        old_left = player.rect.left
        player.rect.left += model_player.horizontal_speed
        if (pygame.sprite.spritecollideany(
                player, self.not_passable_texture_group) is not None or
                pygame.sprite.spritecollideany(
                player, self.borders_texture_group) is not None):
            player.rect.left = old_left
            return False
        return True
        # print("move horizontal with speed", self.horizontal_speed)
        #  if pygame.sprite.spritecollideany(self, walls) is not None:
        # if 1 != 1:
        #     self.left = old_left

    def can_move_vertical(self, model_player):
        player = self.window.player
        old_top = player.rect.top
        player.rect.top += model_player.vertical_speed
        if (pygame.sprite.spritecollideany(
                player, self.not_passable_texture_group) is not None or
                pygame.sprite.spritecollideany(
                player, self.borders_texture_group) is not None):
            player.rect.top = old_top
            return False
        return True


class Window:

    def __init__(self, width, height,
                 texture_width, texture_height,
                 model_field, model_player):

        '''
        height and width are standard texture size

        800x750 battle_field
        100x750 statistic
        '''
        self.width = width
        self.height = height
        self.texture_width = texture_width
        self.texture_height = texture_height
        self.model_field = model_field
        self.model_player = model_player
        self.statistic_width = self.width - 800
        self.canvas = pygame.display.set_mode((self.width, self.height))
        self.texture_image = self.get_texture_image()
        self.statistic = Statistic(self.statistic_width,
                                   self.height,
                                   self.width - self.statistic_width,
                                   self.canvas)
        self.battlefield = Battlefield(self.width - self.statistic_width,
                                       self.height,
                                       self,
                                       self.model_field)
        self.player = Player(self.model_player, self)

    def get_texture_image(self):
        sprites_folder = "sprites"
        sprites_file_name = "battle city sprites upsized.png"
        sprites_full_name = (path.join(sprites_folder,
                                       sprites_file_name))
        texture = pygame.image.load(sprites_full_name).convert()
        return texture

    def update(self):
        self.canvas.fill((0, 0, 0))
        self.statistic.update()
        self.battlefield.update()
        self.battlefield.draw_under()
        self.player.update()
        self.battlefield.draw_over()
        pygame.display.update()























