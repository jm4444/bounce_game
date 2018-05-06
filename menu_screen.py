"""

_  __  ___b o u n c e___  __  _
        a Pong knock off

by Justin Meredith.
project started March 16th, 2018.


"""



#   ~   ~   ~   ~   MODULES & SET UP   ~   ~   ~   ~   ~#

import pygame as game, get_image_size as image
from pygame.locals import *
from functions import load_image

game.init()

graphics_path = "graphics/"
fps_clock = game.time.Clock()
game_mode = None



#   ~   ~   ~   ~   CLASSES   ~   ~   ~   ~   ~#

class Board:
    def __init__(self, image_file):
        self.file_name = image_file
        self.background = load_image(self.file_name)
        self.size = width, height = image.get_image_size(graphics_path + self.file_name)
        self.screen = game.display.set_mode(self.size)

    def display(self):
        self.screen.blit(self.background, (0, 0))


class Button:
    def __init__(self, image_file, position):
        self.is_highlighted = False
        self.file_name = image_file + ".png"
        self.highlighted_name = image_file + " highlight.png"
        self.button = load_image(self.file_name)
        self.highlighted = load_image(self.highlighted_name)
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
        if self.is_highlighted == False:
            board.screen.blit(self.button, self.rectangle)
        elif self.is_highlighted == True:
            board.screen.blit(self.highlighted, self.highlighted_rectangle)



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



#   ~   ~   ~   ~   RUNNING THE MENU   ~   ~   ~   ~   ~#

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

    if single_player_button.rectangle.collidepoint(game.mouse.get_pos()) or single_player_button.highlighted_rectangle.collidepoint(game.mouse.get_pos()):
        single_player_button.is_highlighted = True
        for event in game.event.get():
            if event.type == MOUSEBUTTONDOWN:
                game_mode = "single player"
                break
    else:
        single_player_button.is_highlighted = False

    if two_player_button.rectangle.collidepoint(game.mouse.get_pos()) or two_player_button.highlighted_rectangle.collidepoint(game.mouse.get_pos()):
        two_player_button.is_highlighted = True
        for event in game.event.get():
            if event.type == MOUSEBUTTONDOWN:
                game_mode = "two player"
                break
    else:
        two_player_button.is_highlighted = False

    if game_mode != None:
        break



game.quit()
