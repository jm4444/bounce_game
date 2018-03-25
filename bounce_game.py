"""

~  ~  ~  ~  .:Bounce:.  ~  ~  ~  ~
             a pong knock off

by Justin Meredith.
project started March 16th, 2018.

"""

import sys, pygame, get_image_size
pygame.init()

# the Board class is used to create the screen and background images
class Board:
    def __init__(self, image_file):
        self.file_name = image_file
        self.background = pygame.image.load(graphics_path + self.file_name)
        self.size = width, height = get_image_size.get_image_size(graphics_path + self.file_name)
        self.screen = pygame.display.set_mode(self.size)

    def display(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()


graphics_path = "graphics/"
board = Board("background.png")
board.display()

input("Press any key to close the program.")
