# This file contains the procedures which run the game_over scene when
# the variable "game_state" is set to 'game over'

import pygame

from Objects.Piece import Piece

# global identifiers each representing a RGB colour
black = (0,0,0)
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

'''
run all necessary operations associated with the game over scene,
and display the winner of the match.

Arguments:
    screen (Screen): an instance of pygame class Screen
    winner (str): the winner of the match ('red', 'yellow')

Returns:
    'menu'
'''
def run_game_over(screen, winner):
    # wait for 2 seconds before displaying the game over scenes to allow the
    # player to observe the location of the sequence. While waiting, the event
    # queue is cleared every 100 ms to ensure no input event such as the enter
    # key is present which can Sterminate the game over scene immediately.
    for i in range(20):
        pygame.event.clear()
        pygame.time.wait(100)  
    
    # refresh the scene
    pygame.draw.rect(screen.surface, black, (0, 0, screen.width, screen.height))
    
    # draw a single piece of the winner's colour
    if winner == 'red':
        piece = Piece((180, 250), 40, red)
    else:
        piece = Piece((180, 250), 40, yellow)
    piece.draw(screen)
    
    # draw texts and prompt for enter key
    font = 'Comic Sans Ms'
    text_size = 50
    draw_text(screen, 'has won the game!', font, text_size, white, (250, 235))
    draw_text(screen, 'Return to main menu', font, text_size, yellow, (140, 400), True)
    
    pygame.display.update()
    
    # since no background animation is present, the maximum fps is set to 10
    # to decrease cpu usage while in this scene. When the player presses
    # the enter key, the scene goes back to 'menu'.
    while True:
        if return_to_menu(): return 'menu'
        pygame.time.wait(100)
    

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
Tells the run_game_over function to exit itself and have the game return to the
main menu, when the user hits the enter key.

Arguments:
    None

Returns:
    back_to_menu (bool): output signal representing whether to go back to main
                         menu. It is set to true when the enter key is pressed.
                         Otherwise, False.
'''
def return_to_menu():
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == 13: # enter key
        back_to_menu = True
    else:
        back_to_menu = False
    
    return back_to_menu
