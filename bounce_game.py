"""

_  __  ___b o u n c e___  __  _
        a Pong knock off

by Justin Meredith.
project started March 16th, 2018.

"""

import sys, pygame as pg, get_image_size
pg.init()

# the Board class is used to create the screen and background images
class Board:
    def __init__(self, image_file):
        self.file_name = image_file
        self.background = pg.image.load(graphics_path + self.file_name)
        self.size = width, height = get_image_size.get_image_size(graphics_path + self.file_name)
        self.screen = pg.display.set_mode(self.size)

    def display(self):
        self.screen.blit(self.background, (0, 0))
        pg.display.update()

# the Paddle class is used to create and control the paddles
class Paddle:
    def __init__(self, image_file, side_of_screen):
        self.file_name = image_file
        self.paddle = pg.image.load(graphics_path + self.file_name)
        self.rectangle = self.paddle.get_rect()
        self.rectangle.centery = board.size[1] / 2
        if side_of_screen == "left":
            self.rectangle.centerx = 30
        elif side_of_screen == "right":
            self.rectangle.centerx = board.size[0] - 30

    def display(self, board):
        board.screen.blit(self.paddle, self.rectangle)
        pg.display.update()


graphics_path = "graphics/"
board = Board("background.png")
board.display()
left_paddle = Paddle("paddle.png", "left")
right_paddle = Paddle("paddle.png", "right")
right_paddle.display(board)
left_paddle.display(board)

input("Press enter to close the game.")
