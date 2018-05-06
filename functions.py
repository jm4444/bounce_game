"""

_  __  ___b o u n c e___  __  _
        a Pong knock off

by Justin Meredith.
project started March 16th, 2018.


"""



#   ~   ~   ~   ~   MODULES & SET UP   ~   ~   ~   ~   ~#

import pygame as game

graphics_path = "graphics/"



#   ~   ~   ~   ~   FUNCTIONS   ~   ~   ~   ~   ~#

def update_display(objects):
    for object in objects:
        object.display()

def reset_positions(moving_objects, objects):
    for object in moving_objects:
        object.reset_position()
    update_display(objects)
    game.display.update()
    hold_game()


def hold_game():
    game.time.delay(1500)

def load_image(file_name):
    return game.image.load(graphics_path + file_name)
