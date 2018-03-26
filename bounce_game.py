"""

_  __  ___b o u n c e___  __  _
        a Pong knock off

by Justin Meredith.
project started March 16th, 2018.

"""



#   ~   ~   ~   ~   MODULES & SET UP   ~   ~   ~   ~   ~#

import sys, pygame as game, get_image_size

game.init()

graphics_path = "graphics/"
player_input = game.key.get_pressed()
fps_clock = game.time.Clock()



#   ~   ~   ~   ~   CLASSES   ~   ~   ~   ~   ~#

# the Board class is used to create the screen and background images
class Board:
    def __init__(self, image_file):
        self.file_name = image_file
        self.background = game.image.load(graphics_path + self.file_name)
        self.size = width, height = get_image_size.get_image_size(graphics_path + self.file_name)
        self.screen = game.display.set_mode(self.size)

    def display(self):
        self.screen.blit(self.background, (0, 0))
        game.display.update()


# the Paddle class is used to create and control the paddles
class Paddle:
    def __init__(self, image_file, side_of_screen):
        self.file_name = image_file
        self.paddle = game.image.load(graphics_path + self.file_name)
        self.rectangle = self.paddle.get_rect()
        if side_of_screen == "left":
            self.rectangle.centerx = 30
        elif side_of_screen == "right":
            self.rectangle.centerx = board.size[0] - 30
        self.rectangle.centery = board.size[1] / 2


    def display(self):
        board.screen.blit(self.paddle, self.rectangle)
        game.display.update()

# the Ball class is used to create and control the ball
class Ball:
    def __init__(self, image_file):
        self.file_name = image_file
        self.ball = game.image.load(graphics_path + self.file_name)
        self.rectangle = self.ball.get_rect()
        self.rectangle.centerx = board.size[0] / 2
        self.rectangle.centery = board.size[1] / 2

    def display(self):
        board.screen.blit(self.ball, self.rectangle)
        game.display.update()



#   ~   ~   ~   ~   SETTING THE BOARD   ~   ~   ~   ~   ~#

board = Board("background.png")
ball = Ball("ball.png")
left_paddle = Paddle("paddle.png", "left")
right_paddle = Paddle("paddle.png", "right")
board.display()
ball.display()
right_paddle.display()
left_paddle.display()



#   ~   ~   ~   ~   RUNNING THE GAME   ~   ~   ~   ~   ~#

while True:
    fps_clock.tick(30)      # sets the frame rate at 30fps
    game.event.pump()

    for event in game.event.get():

        if event.type == game.QUIT:      # allows the player to exit the game by clicking the exit 'X' on the window
            print("See ya later!")
            game.quit()
            raise SystemExit

        elif event.type == game.KEYDOWN:      # testing to understand how to accept keyboard input from user
            if event.key == game.K_LEFT:
                print("Left")
