# This file contains the procedures which run the menu scene when
# the variable "game_state" is set to 'menu'

import pygame
from random import randint, seed

from Objects.Piece import Piece

# global identifiers each representing a RGB colour
black = (0,0,0)
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

'''
run all necessary operations associated with the menu scene.

Arguments:
    screen (Screen): an instance of pygame class Screen

Returns:
    'pve', 'pvp', 'instruction', or 'exit'
'''
def run_menu(screen):
    # shuffle the seed for random number generator
    seed(randint(0, 10000))

    # initilize an empty array to hold any existing instances of Piece as the
    # loop runs below
    pieces = []

    # the highlighted features are represented by a single integer from 0 to 3.
    highlighted = 0

    # loop till a feature is selected
    while True:
        # refresh the scene
        pygame.draw.rect(screen.surface, black, 
                         (0, 0, screen.width, screen.height))
        
        # background animation - 
        # drop a red or yellow piece on a random frequency
        # delete any piece that falls below the viewing window
        update_animation(screen, pieces)

        # draw interactive features
        highlighted, selected = feature_interaction(screen, highlighted)

        # change to the user's selected game state, which exit the loop
        if selected:
            if highlighted == 0:
                return 'pve'
            elif highlighted == 1:
                return 'pvp'
            elif highlighted == 2:
                return 'instruction'
            elif highlighted == 3:
                return 'exit'

        pygame.display.update()
        
        # The maximum fps is set to 50 fps to allow for adequately smooth
        # animations to be displayed
        pygame.time.wait(20)


'''
update the current state of the background animation, and draw the updated
state onto the screen.

Arguments:
    screen (Screen): an instance of pygame class Screen
    pieces (list): all existing instances of Piece

Returns:
    None
'''
def update_animation(screen, pieces):
    # instantiate a Piece at a random frequency and x postion, and
    # delete any instance of Piece which has fell below the visible window
    drop_piece(screen, pieces)
    delete_piece(screen, pieces)

    # draw any existing instance of Piece at their current state, then
    # update its state
    for piece in pieces:
        piece.draw(screen)
        piece.update(screen)


'''
instanstiate a Piece of either red or yellow colour located
at a random x position within the screen, at a fixed 10% frequency.

Arguments:
    screen (Screen): an instance of pygame class Screen
    pieces (list): all existing instances of Piece

Returns:
    None
'''
def drop_piece(screen, pieces):
    drop_chance = 10 # 0 to 100% chance to drop a piece
    drop_roll = randint(1, 100)
    if drop_roll <= drop_chance:
        
        x = randint(0, screen.width) # x position of dropped piece
        y = -50 # the piece is dropped above the view window
        r = 40 # radius of the dropped piece
        
        red_chance = 50 # 0 to 100% chance for the dropped piece to be red
        red_roll = randint(1, 100)
        
        if red_roll <= red_chance:
            pieces.append(Piece((x, y), r, red))
        else:
            pieces.append(Piece((x, y), r, yellow))


'''
Delete any instances of Piece that have dropped below the visible screen.

Arguments:
    screen (Screen): an instance of pygame class Screen
    pieces (list): all existing instances of Piece

Returns:
    None
'''
def delete_piece(screen, pieces):
    for piece in pieces:
        if piece.y >= screen.height + 100:
            pieces.remove(piece)


'''
Draw all texts onto the screen based on the current state of the variable
"highlighted". In addition, return a boolean value which indicates if the
user has selected any feature.

Arguments:
    screen (Screen): an instance of pygame class Screen
    highlighted (int): an integer (1 to 4) representing the currently 
                       highlighted feature

Returns:
    highlighted (int): an integer (1 to 4) representing the next 
                       highlighted feature
    selected (bool): set to True if the user has selected a feature
'''
def feature_interaction(screen, highlighted):
    font = 'Comic Sans Ms'

    # draw title
    draw_text(screen, 'Connect 4', font, 120, yellow, (110, 150), True)

    # draw sub_title
    draw_text(screen, 'Ultra Edition', font, 70, red, (195, 225))
    
    # draw menu instruction
    draw_text(screen, 'up/down arrow: navigate', font, 30, white, (10, 670))
    draw_text(screen, 'enter: select', font, 30, white, (565, 670))
    
    # draw interactive features that change to game scene when selected
    highlighted, selected = handle_input(highlighted)
    if highlighted == 0:
        draw_text(screen, 'Single player', font, 50, yellow, (235, 350))
    else:
        draw_text(screen, 'Single player', font, 50, white, (235, 350))
    if highlighted == 1: 
        draw_text(screen, 'Multiplayer', font, 50, red, (255, 400))
    else:
        draw_text(screen, 'Multiplayer', font, 50, white, (255, 400))
    if highlighted == 2: 
        draw_text(screen, 'Instruction', font, 50, yellow, (255, 450))
    else:
        draw_text(screen, 'Instruction', font, 50, white, (255, 450))
    if highlighted == 3:
        draw_text(screen, 'Exit', font, 50, red, (310, 500))
    else:
        draw_text(screen, 'Exit', font, 50, white, (310, 500))

    return highlighted, selected


'''
draw a single line of customized text on the pygame screen.

Arguments:
    screen (Screen): an instance of pygame class Screen
    text (str): text to be displayed
    style (str): font style
    size (int): font size
    color (tuple): font color as a rgb combination
    position (tuple): location of the top left corner of the text relative to
                      the top left corner of the window
    bold (bool): bold the text if set to True. It is defaulted as False.
    italic (bool): italasize the text if set to True. It is defaulted as False.

Returns:
    None
'''
def draw_text(screen, text, style, size, color, position,
              bold = False, italic = False):

    text_font = pygame.font.SysFont(style, size, bold, italic)
    text_image = text_font.render(text, False, color)
    screen.surface.blit(text_image, position)


'''
Handle the user inputs as required. The possible inputs include up arrow key,
down arrow key, and enter key.

Arguments:
    highlighted (int): an integer (1 to 4) representing the currently 
                       highlighted feature

Returns:
    highlighted (int): an integer (1 to 4) representing the next 
                       highlighted feature
    selected (bool): set to True if the user has pressed the enter key.
                     Otherwise, False.
'''
def handle_input(highlighted):
    selected = False
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        if event.key == 273: # arrow key - up
            highlighted = navigate_upward(highlighted)
        elif event.key == 274: # arrow key - down
            highlighted = navigate_downward(highlighted)
        elif event.key == 13: # enter key
            selected = True
    
    return highlighted, selected


'''
Move the highlight to the feature above if possible.

Arguments:
    highlighted (int): an integer (1 to 4) representing the currently 
                       highlighted feature

Returns:
    highlighted (int): an integer (1 to 4) representing the next 
                       highlighted feature
'''
def navigate_upward(highlighted):
    if highlighted > 0:
        highlighted -= 1
    return highlighted


'''
Move the highlight to the feature below if possible.

Arguments:
    highlighted (int): an integer (1 to 4) representing the currently 
                       highlighted feature

Returns:
    highlighted (int): an integer (1 to 4) representing the next 
                       highlighted feature
'''
def navigate_downward(highlighted):
    if highlighted < 3:
        highlighted += 1
    return highlighted
