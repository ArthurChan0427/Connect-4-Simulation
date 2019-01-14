# This file contains all attributes and methods of the class Input_cursor

# Input_cursor process all user inputs during the match scene. In addition,
# it contains a decrementing internal timer that represents the amount of time
# left for the player to make their next move. Input_cursor displays its current
# x position, turn, and mode as an arrow and its timer as a horizontal bar.

import pygame

from Objects.Piece import Piece

# global identifiers each representing a RGB colour
red = (255, 0, 0)
yellow = (255, 255, 0)

class Input_cursor():
    def __init__(self, screen):
        self._x = int(screen.width / 2) # x position
        self._colour = red # colour of the pieces to be dropped/deleted
        self._mode = 'add' # 'add' or 'delete'
        self._timer_max = 800 # a total 800 frames available for each move 
        self._timer = self._timer_max # current state of timer
        self.player_turn = True # used in pve game only


    '''
    Draw its current state on the screen.
    
    Arguments:
        screen (Screen): an instance of pygame class Screen
        board (Board): an instance of pygame class Board
    
    Returns:
        None
    '''
    def draw(self, screen, board):
        # location of each vertices during its current state
        vertices = [(self._x, board.unit_size),
                    (self._x - board.unit_size / 4, 0.5 * board.unit_size),
                    (self._x, 0.65 * board.unit_size),
                    (self._x + board.unit_size / 4, 0.5 * board.unit_size)]

        # draw the cursor completely filled to indicate 'add' mode or
        # with a hollow interior to indicate 'delete' mode
        if self._mode == 'add':
            pygame.draw.polygon(screen.surface, self._colour, vertices)
        elif self._mode == 'delete':
            pygame.draw.polygon(screen.surface, self._colour, vertices, 2)
        
        # draw the current state of the timer at the top of the window
        pygame.draw.rect(screen.surface, self._colour, (0, 0, 
                         int(self._timer / self._timer_max * screen.width), 20))
    

    '''
    Decrement its timer by 1. When the timer reaches zero, it switches its
    colour and reset the timer for pvp game, or it ends the player's turn and
    reset the timer for pve game.
    
    Arguments:
        game_state (str): 'pve' or 'pvp', 
                          representing single or multi player game
    
    Returns:
        None
    '''
    def update_timer(self, game_state):
        self._timer -= 1        
        if self._timer <= 0:
            if game_state == 'pvp':
                self._change_turn()
            elif game_state == 'pve':
                self.player_turn = False
                self._timer = self._timer_max


    '''
    Handle the user inputs. The possible user inputs include left arrow key,
    right arrow key, enter key, space key, and escape key.
    
    Arguments:
        screen (Screen): an instance of pygame class Screen
        board (Board): an instance of class Board
        pieces (list): all existing instances of Piece
        game_state (str): 'pve' or 'pvp', 
                          representing single or multi player game
    
    Returns:
        None or 'menu'
    '''
    def handle_input(self, screen, board, pieces, game_state):
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == 276: # arrow key - left
                self._move(screen, board, 'left')
            elif event.key == 275: # arrow key - right
                self._move(screen, board, 'right')
            elif event.key == 13: # enter key
                if self._mode == 'add': 
                    self._add_piece(board, pieces, game_state)
                elif self._mode == 'delete':
                    self._delete_piece(screen, board, pieces, game_state)
            elif event.key == 32: # space key
                self._change_mode()
            elif event.key == 27: # ESC key
                return 'menu'
            

    '''
    Move its x position by one board unit to the left/right when the user
    presses the left/right arrow key.
    
    Arguments:
        screen (Screen): an instance of pygame class Screen
        board (Board): an instance of class Board
        direction (str): 'left' or 'right', depending on the input arrow key
    
    Returns:
        None
    '''
    def _move(self, screen, board, direction):
        if direction == 'left' and self._x > board.unit_size:
            self._x -= board.unit_size
        elif direction == 'right' and self._x < screen.width - board.unit_size:
            self._x += board.unit_size


    '''
    Instantiate a Piece of its current colour at it current x position, then
    switch the turn for pvp game or ends the player's turn for pve game. This
    method is executed when player presses the enter key.
    
    Arguments:
        board (Board): an instance of class Board
        pieces (list): all existing instances of Piece
        game_state (str): 'pve' or 'pvp', 
                          representing single or multi player game
    
    Returns:
        None
    '''
    def _add_piece(self, board, pieces, game_state):
        # The add piece procedure is executed only if the selected column is
        # not full.
        if not any((piece.y <= 1.5 * board.unit_size and piece.x == self._x or \
                    not piece.is_stationary) for piece in pieces):

            pieces.append(Piece((self._x, -50), board.c_radius, self._colour))
            if game_state == 'pvp':
                self._change_turn()
            elif game_state == 'pve':
                self.player_turn = False
                self._timer = self._timer_max


    '''
    Delete the instance of Piece located at the bottom of the selected coloumn,
    then switch the turn for pvp game or ends the player's turn for pve game.
    
    The selected instance of Piece must be of the same colour as the current
    state of the cursor; otherwise, this method does not execute the above
    operations.
    
    Arguments:
        screen (Screen): an instance of pygame class Screen
        board (Board): an instance of class Board
        pieces (list): all existing instances of Piece
        game_state (str): 'pve' or 'pvp', 
                          representing single or multi player game
    
    Returns:
        None
    '''
    def _delete_piece(self, screen, board, pieces, game_state):
        # The delete piece procedure is executed when all existing instances
        # of Piece are stationary.
        if all(piece.is_stationary for piece in pieces):
            
            # check each instances of Piece and remove only the correct one
            for piece in pieces:
                if piece.x == self._x and \
                   screen.height - piece.y < board.unit_size / 2 + 5 and \
                   self._colour == piece.colour:
    
                    pieces.remove(piece)

                    if game_state == 'pvp':
                        self._change_turn()
                    elif game_state == 'pve':
                        self.player_turn = False                    


    '''
    Reset its timer and switch its colour.
    
    Arguments:
        None
    
    Returns:
        None
    '''
    def _change_turn(self):
        self._timer = self._timer_max
        if self._colour == red:
            self._colour = yellow
        else:
            self._colour = red
            
    
    '''
    Switch its mode between 'delete' and 'add'.
    
    Arguments:
        None
    
    Returns:
        None
    '''
    def _change_mode(self):
        if self._mode == 'add':
            self._mode = 'delete'
        elif self._mode == 'delete':
            self._mode = 'add'
