"""

_  __  ___b o u n c e___  __  _
        a Pong knock off

by Justin Meredith.
project started March 16th, 2018.


"""



#   ~   ~   ~   ~   MODULES & SET UP   ~   ~   ~   ~   ~#

import sys, pygame as game, get_image_size, random

game.init()

graphics_path = "graphics/"
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
            self.up = game.K_w
            self.down = game.K_s
        elif side_of_screen == "right":
            self.rectangle.centerx = board.size[0] - 30
            self.up = game.K_UP
            self.down = game.K_DOWN
        self.rectangle.centery = board.size[1] / 2
        self.speed = 9

    def display(self):
        board.screen.blit(self.paddle, self.rectangle)
        game.display.update(self.rectangle)

    def move(self, key_input):
        if key_input[self.up] and self.rectangle.top >= 0:
            self.rectangle.centery -= self.speed
        elif key_input[self.down] and self.rectangle.bottom <= board.size[1]:
            self.rectangle.centery += self.speed

    def reset_position(self):
        self.rectangle.centery = board.size[1] / 2


# the Ball class is used to create and control the ball
class Ball:
    def __init__(self, image_file):
        self.file_name = image_file
        self.ball = game.image.load(graphics_path + self.file_name)
        self.rectangle = self.ball.get_rect()
        self.rectangle.centerx = board.size[0] / 2
        self.rectangle.centery = board.size[1] / 2
        self.start_moving = False
        self.speed = [7, 7]
        self.randomize_speed()

    def display(self):
        board.screen.blit(self.ball, self.rectangle)
        game.display.update(self.rectangle)

    def move(self):
        if self.start_moving == True:
            self.rectangle = self.rectangle.move(self.speed)
            if self.rectangle.right < 0 or self.rectangle.left > board.size[0]:      # bouncing off left or right of screen
                reset_positions(ball, left_paddle, right_paddle)

            if self.rectangle.top < 0 or self.rectangle.bottom > board.size[1]:      # bouncing off top or bottom of screen
                self.speed[1] = -self.speed[1]

            if self.rectangle.colliderect(left_paddle.rectangle):      # bouncing off of the left paddle
                self.speed[0] = -self.speed[0]

            if self.rectangle.colliderect(right_paddle.rectangle):      # bouncing off of the right paddle
                self.speed[0] = -self.speed[0]

    def reset_position(self):
        self.rectangle.move([0, 0])
        ball.start_moving = False
        self.randomize_speed()
        self.rectangle.centerx = board.size[0] / 2
        self.rectangle.centery = board.size[1] / 2

    def randomize_speed(self):
        randomizer = (-1)**random.randrange(2)      # generates a 1 or -1
        self.speed[0] *= randomizer
        self.speed[1] *= randomizer



#   ~   ~   ~   ~   FUNCTIONS   ~   ~   ~   ~   ~#

def update_display(board, ball, left_paddle, right_paddle):
    board.display()
    ball.display()
    left_paddle.display()
    right_paddle.display()

def reset_positions(ball, left_paddle, right_paddle):
    ball.reset_position()
    left_paddle.reset_position()
    right_paddle.reset_position()



#   ~   ~   ~   ~   SETTING THE BOARD   ~   ~   ~   ~   ~#

board = Board("background.png")
ball = Ball("ball.png")
left_paddle = Paddle("paddle.png", "left")
right_paddle = Paddle("paddle.png", "right")
update_display(board, ball, left_paddle, right_paddle)



#   ~   ~   ~   ~   RUNNING THE GAME   ~   ~   ~   ~   ~#

while True:

    #//// Check for Specific Events //

    for event in game.event.get():
        if event.type == game.QUIT:      # allows the player to exit the game by clicking the exit 'X' on the window
            game.quit()
            raise SystemExit


    #//// Variables for Running the Game //

    fps_clock.tick(44)      # sets the frame rate at 30fps
    game.event.pump()
    key_input = game.key.get_pressed()
    update_display(board, ball, left_paddle, right_paddle)


    #//// Moving Objects //

    #// Moving the left paddle /
    if key_input[left_paddle.up] or key_input[left_paddle.down]:
        left_paddle.move(key_input)
        ball.start_moving = True

    #// Moving the right paddle /
    if key_input[right_paddle.up] or key_input[right_paddle.down]:
        right_paddle.move(key_input)
        ball.start_moving = True

    ball.move()
