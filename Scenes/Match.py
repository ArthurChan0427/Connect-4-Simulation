# This file contains the procedures which run the match scene when
# the variable "game_state" is set to 'pvp' or 'pve'

import pygame

from Objects.Screen import Screen
from Objects.Board import Board
from Objects.Input_cursor import Input_cursor
from Objects.Piece import Piece
from Objects.Computer import Computer

# global identifier representing the rgb of black
black = (0,0,0)

'''
run all necessary operations associated with the match scene.

Arguments:
    game_state (str): current game state, either 'pvp' or 'pve'
    screen (Screen): an instance of pygame class Screen

Returns:
    winner (str): the winner of the match, either 'red' or 'yellow'
    'menu' or 'game over'
'''
def run_match(game_state, screen):
    # instantiate Board and Input_cursor, as well as Computer if
    # game_state == pve. An empty list called "pieces" is also declared
    # the current scope to hold any instance of Piece created in the midst
    # of the match.
    board, cursor, pieces, computer = match_init(screen, game_state)

    # loop till a winner has been announced or the player wish to exit the game
    # promptly with the ESC key.
    while True:
        # draw the match scene in the current state, then update the state
        draw_match(screen, board, cursor, pieces)
        winner = update_match(screen, board, cursor, pieces, computer, game_state)
        
        # switch to 'menu' scene if player used ESC key, or 
        # switch to 'game over' scene if a winner is announced
        # Otherwise, keep looping at a maximum fps of 50.
        if winner == 'menu':
            return 'menu', winner
        elif winner == 'red' or winner == 'yellow':
            return 'game over', winner
        pygame.time.wait(20)


'''
Instantiate all objects required in the match including the game board, the
input cursor, an empty list to hold all pieces, as well the AI class represented
by the class Computer if the game is single-player.

Arguments:
    screen (Screen): an instance of pygame class Screen
    game_state (str): current game state, either 'pvp' or 'pve'

Returns:
    board (Board): an instance of class Board
    cursor (Input_cursor): an instance of class Input_cursor
    pieces (list): an empty list to hold all instances of Piece in the match
    computer (Computer): an instance of class Computer for 'pve' game only.
                         otherwise, returns None.
'''
def match_init(screen, game_state):
    # instantiate a playing grid with 6 rows, 7 columns,
    # and circular holes with radius of 40 pixels
    board = Board(screen, 6, 7, 40)
    
    # instantiate an input cursor
    cursor = Input_cursor(screen)
    
    # an array that holds all the instance of piece currently present
    pieces = []    

    # instantiate a computer for pve game only
    computer = None
    if game_state == 'pve':
        computer = Computer()

    return board, cursor, pieces, computer


'''
Draw all objects, including the game board, the current state of input cursor,
and the current state all existing instances of Piece onto the pygame screen.

Arguments:
    screen (Screen): an instance of pygame class Screen
    board (Board): an instance of class Board
    cursor (Input_cursor): an instance of class Input_cursor
    pieces (list): all existing instances of Piece

Returns:
    None
'''
def draw_match(screen, board, cursor, pieces):
    # refresh the scene
    pygame.draw.rect(screen.surface, black, (0, 0, screen.width, screen.height))
    
    # draw the instance of Board
    board.draw_rect(screen)
    board.draw_holes(screen)
    
    # draw any existing instance of Piece in their current state
    for piece in pieces:
        piece.draw(screen)
    
    # draw the instance of Input_cursor
    cursor.draw(screen, board)


'''
Update the current state of the match, including the state of all existing
objects and user inputs.

Arguments:
    screen (Screen): an instance of pygame class Screen
    board (Board): an instance of class Board
    cursor (Input_cursor): an instance of class Input_cursor
    pieces (list): all existing instances of Piece
    computer (Computer): an instance of class Computer. None for pve game.
    game_state (str): 'pve' or 'pvp', representing single or multi player game

Returns:
    winner (str): winner of the match. None if no winner has been announced yet.
'''
def update_match(screen, board, cursor, pieces, computer, game_state):
    # process the user input using the method of Input_cursor. For pve game,
    # the instance of Computer will instantiate a Piece after every player's
    # turn has ended.
    if game_state == 'pvp' or cursor.player_turn:
        cursor.update_timer(game_state)
        back_to_menu = cursor.handle_input(screen, board, pieces, game_state)
        if back_to_menu: return 'menu'
    elif game_state == 'pve':
        if all(piece.is_stationary for piece in pieces):
            computer.drop_piece(board, pieces)
            cursor.player_turn = True

    # update the state of any existing instances of Piece
    for piece in pieces:
        piece.update(screen, pieces, board)

    # The instance of Board acts also act as a referee of the match which
    # checks if a winner is present in the current state of the match.
    # If no winner is present, it is assigned None.
    winner = board.check_winner(pieces)

    pygame.display.update()

    return winner
