"""

_  __  ___b o u n c e___  __  _
        a Pong knock off

by Justin Meredith.
project started March 16th, 2018.


"""



#   ~   ~   ~   ~   MODULES & SET UP   ~   ~   ~   ~   ~#

import sys, pygame as game, get_image_size as image, random
from functions import *
from menu_screen import game_mode

game.init()

graphics_path = "graphics/"
fps_clock = game.time.Clock()
winner = None



#   ~   ~   ~   ~   CLASSES   ~   ~   ~   ~   ~#

class Board:
    def __init__(self, image_file):
        self.file_name = image_file
        self.background = load_image(self.file_name)
        self.size = width, height = image.get_image_size(graphics_path + self.file_name)
        self.screen = game.display.set_mode(self.size)

    def display(self):
        self.screen.blit(self.background, (0, 0))


class Image:
    def __init__(self, image_file):
        self.file_name = image_file
        self.image = load_image(self.file_name)
        self.rectangle = self.image.get_rect()
        self.rectangle.centerx = board.size[0] / 2
        self.rectangle.centery = board.size[1] / 2

    def display(self):
        board.screen.blit(self.image, self.rectangle)


class Score:
    def __init__(self, side_of_screen):
        self.side_of_screen = side_of_screen
        self.score_count = 0
        self.change_score()

    def change_score(self):
        self.current_score = load_image(str(self.score_count) + ".png")
        self.rectangle = self.current_score.get_rect()
        self.display()

    def add_point(self):
        self.score_count += 1
        self.change_score()
        if self.score_count == 7:
            global winner
            if self.side_of_screen == "left":
                winner = "player one"
            elif self.side_of_screen == "right":
                winner = "player two"

    def display(self):
        screen_quarter = board.size[0] / 4
        self.rectangle.centery = 75
        if self.side_of_screen == "left":
            self.rectangle.centerx = screen_quarter
        elif self.side_of_screen == "right":
            self.rectangle.centerx = screen_quarter * 3
        board.screen.blit(self.current_score, self.rectangle)


class Paddle:
    def __init__(self, image_file, side_of_screen):
        self.file_name = image_file
        self.paddle = load_image(self.file_name)
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
        self.speed = 12

    def display(self):
        board.screen.blit(self.paddle, self.rectangle)

    def move(self, key_input):
        if key_input[self.up] and self.rectangle.top >= 0:
            self.rectangle.centery -= self.speed
        elif key_input[self.down] and self.rectangle.bottom <= board.size[1]:
            self.rectangle.centery += self.speed

    def reset_position(self):
        self.rectangle.centery = board.size[1] / 2


class ArtificialPaddle(Paddle):
    def __init__(self, image_file, side_of_screen):
        super().__init__(image_file, side_of_screen)
        self.speed = 10

    def move(self):
        if ball.start_moving == True:
            if ball.speed[0] > 0 and ball.rectangle.centerx > board.size[0] / 3 * 2:
                if self.rectangle.centery < ball.rectangle.centery and self.rectangle.bottom <= board.size[1]:      # moves the paddle down, towards the ball
                    self.rectangle.centery += self.speed
                elif self.rectangle.centery > ball.rectangle.centery and self.rectangle.top >= 0:      # moves the paddle up, towards the ball
                    self.rectangle.centery -= self.speed


class Ball:
    def __init__(self, image_file):
        self.file_name = image_file
        self.ball = load_image(self.file_name)
        self.rectangle = self.ball.get_rect()
        self.default_position()
        self.start_moving = False
        self.speed = [7.5, 11]
        self.randomize_speed()

    def display(self):
        board.screen.blit(self.ball, self.rectangle)

    def move(self):
        if self.start_moving == True:
            self.rectangle = self.rectangle.move(self.speed)
            if self.rectangle.right < 0:      # going off left of screen
                right_score.add_point()
                reset_positions(moving_objects, objects)
            elif self.rectangle.left > board.size[0]:      # going off right of screen
                left_score.add_point()
                reset_positions(moving_objects, objects)

            if self.rectangle.top < 0 or self.rectangle.bottom > board.size[1]:      # bouncing off top or bottom of screen
                self.speed[1] = -self.speed[1]

            if self.rectangle.colliderect(left_paddle.rectangle) and self.rectangle.left >= left_paddle.rectangle.centerx:      # bouncing off of the left paddle
                self.speed[0] = -self.speed[0]

            if self.rectangle.colliderect(right_paddle.rectangle) and self.rectangle.right <=right_paddle.rectangle.centerx:      # bouncing off of the right paddle
                self.speed[0] = -self.speed[0]

    def reset_position(self):
        self.rectangle.move([0, 0])
        ball.start_moving = False
        self.randomize_speed()
        self.default_position()

    def randomize_speed(self):
        randomizer = (-1)**random.randrange(2)      # generates a 1 or -1
        self.speed[0] *= randomizer
        self.speed[1] *= randomizer

    def default_position(self):
        self.rectangle.centerx = board.size[0] / 2
        self.rectangle.centery = board.size[1] / 2



#   ~   ~   ~   ~   SETTING THE BOARD   ~   ~   ~   ~   ~#

board = Board("background.png")
left_score = Score("left")
right_score = Score("right")
ball = Ball("ball.png")
left_paddle = Paddle("paddle.png", "left")
if game_mode == "single player":
    right_paddle = ArtificialPaddle("paddle.png", "right")
elif game_mode == "two player":
    right_paddle = Paddle("paddle.png", "right")
objects = [board, left_score, right_score, ball, left_paddle, right_paddle]
moving_objects = [ball, left_paddle, right_paddle]
update_display(objects)



#   ~   ~   ~   ~   RUNNING THE GAME   ~   ~   ~   ~   ~#

while True:

    #// Check for Specific Events
    for event in game.event.get():
        if event.type == game.QUIT:      # allows the player to exit the game by clicking the exit 'X' on the window
            game.quit()
            raise SystemExit


    #// Variables for Running the Game
    fps_clock.tick(40)      # sets the frame rate
    game.event.pump()
    key_input = game.key.get_pressed()
    update_display(objects)
    game.display.update()


    #// Moving the left paddle
    if key_input[left_paddle.up] or key_input[left_paddle.down]:
        left_paddle.move(key_input)
        ball.start_moving = True

    if game_mode == "single player":
        right_paddle.move()
    elif game_mode == "two player":
        if key_input[right_paddle.up] or key_input[right_paddle.down]:
            right_paddle.move(key_input)
            ball.start_moving = True

    ball.move()

    if winner != None:
        break



#   ~   ~   ~   ~   ENDING THE GAME   ~   ~   ~   ~   ~#

winner_image = Image(winner + " wins.png")
objects.append(winner_image)
update_display(objects)
game.display.update()

input()
