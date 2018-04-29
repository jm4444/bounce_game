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

class Board:
    def __init__(self, image_file):
        self.file_name = image_file
        self.background = game.image.load(graphics_path + self.file_name)
        self.size = width, height = get_image_size.get_image_size(graphics_path + self.file_name)
        self.screen = game.display.set_mode(self.size)

    def display(self):
        self.screen.blit(self.background, (0, 0))


class Button:
    def __init__(self, image_file, position):
        self.file_name = image_file + ".png"
        self.highlighted_name = image_file + " highlight.png"
        self.button = game.image.load(graphics_path + self.file_name)
        self.highlighted = game.image.load(graphics_path + self.highlighted_name)
        self.rectangle = self.button.get_rect()
        self.highlighted_rectangle = self.highlighted.get_rect()
        self.rectangle.left = 106
        self.highlighted_rectangle.left = 106
        if position == "top":
            self.rectangle.centery = 225
            self.highlighted_rectangle.centery = 225
        elif position == "bottom":
            self.rectangle.centery = 300
            self.highlighted_rectangle.centery = 300

    def display(self):
        board.screen.blit(self.button, self.rectangle)



#   ~   ~   ~   ~   FUNCTIONS   ~   ~   ~   ~   ~#

def update_display():
    board.display()
    single_player_button.display()
    two_player_button.display()



#   ~   ~   ~   ~   SETTING THE MENU   ~   ~   ~   ~   ~#

board = Board("menu.png")
single_player_button = Button("single player", "top")
two_player_button = Button("two player", "bottom")
update_display()


#   ~   ~   ~   ~   RUNNING THE GAME   ~   ~   ~   ~   ~#

while True:

    #//// Check for Specific Events //

    for event in game.event.get():
        if event.type == game.QUIT:      # allows the player to exit the game by clicking the exit 'X' on the window
            game.quit()
            raise SystemExit


    #// Variables for Running the Game
    fps_clock.tick(60)      # sets the frame rate at 60fps
    game.event.pump()
    update_display()
    game.display.update()
