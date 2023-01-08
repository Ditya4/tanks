import pygame
from os import path


class Player(pygame.sprite.Sprite):

    def __init__(self, model_player, canvas, rect_size):
        super().__init__()
        '''
        self.model_player = model_player
        self.canvas = canvas
        self.rect_size = rect_size
        self.image = pygame.Surface([self.rect_size, self.rect_size])
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self)
        '''

    def update(self):
        pass
        '''
        x, y = pygame.mouse.get_pos()
        self.rect.y = y
        self.rect.x = x
        self.player_group.draw(self.canvas)
        '''


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
                                     self.window.texture_height]).convert()
        self.image.blit(texture, (0, 0), (texture_top_left[1],
                                          texture_top_left[0],
                                          self.window.texture_width,
                                          self.window.texture_height))
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()
        self.rect.top = y * self.window.texture_height
        self.rect.left = x * self.window.texture_width


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
        self.width = width
        self.height = height
        self.window = window
        self.canvas = window.canvas
        self.model_field = model_field
        self.texture_dict = {}
        self.fill_texture_dict()
        self.texture_group = pygame.sprite.Group()
        self.texture_image = self.get_texture_image()
        self.update()

    def get_texture_image(self):
        sprites_folder = "sprites"
        sprites_file_name = "battle city sprites upsized.png"
        sprites_full_name = (path.join(sprites_folder,
                                       sprites_file_name))
        texture = pygame.image.load(sprites_full_name).convert()
        return texture

    def fill_texture_dict(self):
        texture_data_list = [["brick", "!", 0, 550],
                             ["grass", ",", 58, 585],
                             ["water_1", "+", 58, 550], ]

        for texture_data in texture_data_list:
            self.texture_dict[texture_data[1]] = (texture_data[2],
                                                  texture_data[3])

    def update(self):
        self.texture_group.empty()
        for y in range(1, self.model_field.size):
            for x in range(1, self.model_field.size):
                if self.model_field.landscape[y][x] != 32:  # not space symbol
                    if chr(self.model_field.landscape[y][x]) in (
                            self.texture_dict):
                        print(y, x, self.model_field.landscape[y][x])

                        texture = Texture(
                            y - 1, x - 1,
                            self.texture_dict[chr(
                                self.model_field.landscape[y][x])],
                            self.texture_image, self.window)
                        self.texture_group.add(texture)
        self.texture_group.draw(self.canvas)


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
        self.statistic = Statistic(self.statistic_width,
                                   self.height,
                                   self.width - self.statistic_width,
                                   self.canvas)
        self.battlefield = Battlefield(self.width - self.statistic_width,
                                       self.height,
                                       self,
                                       self.model_field)
        self.player = Player(self.model_player, self.canvas, self.battlefield)


    def update(self):
        self.canvas.fill((0, 5, 150))
        self.statistic.update()
        self.battlefield.update()
        self.player.update()
        pygame.display.update()





















