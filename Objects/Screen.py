# This file contains all attributes and methods of the class Screen

# Screen represents the pygame window itself. The initializing value for width
# and height represents the width and height of the game window in pixels. The
# attribute "surface" is used in all pygame.draw methods used in the rest of
# the game.

import pygame

class Screen(): 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = 0
        self._display()

    
    '''
    Display itself as a pygame window with a dimension, width and height,
    as initialized.
    
    Arguments:
        None
    
    Returns:
        None
    '''    
    def _display(self):
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect 4")
