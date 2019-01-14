# This file contains all attributes and methods of the class Piece

# Piece represents the red or yellow circular pieces each player places in the
# game board. Piece acts like a rigid body which drops at a constant velocity
# and detect any collision with the bottom of the board or other Piece below.
# The collision detections is enabled only when an instance of Board is present,
# such as in the match scene.

import pygame

# global identifiers each representing a RGB colour
red = (255, 0, 0)
yellow = (255, 255, 0)

class Piece():
    def __init__(self, position, radius, colour):
        self.x = position[0] # x position
        self.y = position[1] # y position
        self._radius = radius # radius of the piece
        self.colour = colour # colour of the piece
        self.is_stationary = False


    '''
    Determine if it has collided with any other instances of pieces below. This
    method is enabled only when an instance of the class Board is available in
    the current state of the game.
    
    Arguments:
        other_piece (Piece): another instance of Piece
        board (Board or None): an instance of class Board. If nothing is passed,
                               it is set to None.
    
    Returns:
        True if an instance of Board is available and an instance of Piece is
        immediately below. Otherwise, False.
    '''
    def _collided(self, other_piece, board = None):
        return board != None and \
               other_piece.y > self.y and \
               other_piece.y - self.y <= board.unit_size and \
               other_piece.x == self.x


    '''
    Determine if it has reached the bottom of the instance of Board. This
    method is enabled only when an instance of the class Board is available in
    the current state of the game.
    
    Arguments:
        screen (Screen): an instance of pygame class Screen
        board (Board or None): an instance of class Board. If nothing is passed,
                               it is set to None.
    
    Returns:
        True if it has reach the bottom row of the instance of Board.
        Otherwise, False.
    '''
    def _is_at_bottom(self, screen, board = None):
        return board != None and \
               self.y >= screen.height - board.unit_size / 2


    '''
    Update its current state. If it has reached the bottom row of the instance
    of Board or has collided with another instance of Piece immediately below,
    then it is considered stationary. Otherwise, it is not stationary and its
    y position is incremented by 25 pixels.
    
    Arguments:
        screen (Screen): an instance of pygame class Screen
        pieces (list or None): all existing instances of Piece. If nothing is
                               passed, it is set to None.
        board (Board or None): an instance of class Board. If nothing is passed,
                               it is set to None.
    
    Returns:
        None
    '''
    def update(self, screen, pieces = None, board = None):
        has_collided = False
        self.is_stationary = True # stationary by default
        
        # increment y position only if it is not colliding with the bottom
        # of the board or any other instance of Piece below.
        if not self._is_at_bottom(screen, board):
            if pieces != None:
                for piece in pieces:
                    if self._collided(piece, board):
                        has_collided = True

            if not has_collided:
                self.y += 25
                self.is_stationary = False # not stationary if it's moving!


    '''
    Draw its current state on the screen.
    
    Arguments:
        screen (Screen): an instance of pygame class Screen
    
    Returns:
        None
    '''
    def draw(self, screen):
        pygame.draw.circle(screen.surface, self.colour,
                           (self.x, self.y), self._radius)
