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



#   ~   ~   ~   ~   FUNCTIONS   ~   ~   ~   ~   ~#

def update_display():
    board.display()



#   ~   ~   ~   ~   SETTING THE MENU   ~   ~   ~   ~   ~#

board = Board("menu.png")
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
