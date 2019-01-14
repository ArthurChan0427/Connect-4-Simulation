# This file contains the procedures which run the instruction scene when
# the variable "game_scene" is set to 'instruction'

import pygame

# global identifiers each representing a RGB colour
blue = (0,0,255)
black = (0,0,0)
yellow = (255, 255, 0)
white = (255, 255, 255)

'''
run all necessary operations associated with the Instruction scene.

Arguments:
    screen (Screen): an instance of pygame class Screen

Returns:
    'menu'
'''
def run_instruction(screen):
    # set the general font style and size, as well as the y position of the
    # first line of text
    font = 'Comic Sans Ms'
    text_size = 30
    y_line = 50
    
    # refresh the scene
    pygame.draw.rect(screen.surface, black, (0, 0, screen.width, screen.height))
    
    # draw each line of text from top to bottom using the style and size as
    # specified above, unless otherwise noted. Each value assigned to y-line
    # represents the y position of the next line of text.
    
    # bigger size, bolded
    y_line = draw_text(screen,
                       'Welcome to Connect 4 Ultra!',
                       font, 50, blue, 75, y_line, True)

    # double spaced, bolded
    y_line = draw_text(screen, 
                       'Rules and Objectives:',
                       font, text_size, white, 215, y_line + text_size, True)
    y_line = draw_text(screen, 
                       'In a 7 x 6 grid, the red player and the yellow player',
                       font, text_size, white, 100, y_line)
    y_line = draw_text(screen, 
                       'shall take turn dropping/deleting a piece of their respective color.',font, text_size, white, 25, y_line)
    y_line = draw_text(screen, 
                       'There is a time limit in each turn, so think fast!',
                       font, text_size, white, 120, y_line)    
    y_line = draw_text(screen, 
                       'The player that achieves a sequence of 4 pieces aligned',
                       font, text_size, white, 70, y_line)
    y_line = draw_text(screen, 
                       'vertically/horizontally/diagonally wins the game!',
                       font, text_size, white, 110, y_line)

    # double spaced, bolded
    y_line = draw_text(screen,
                       'Controls:',
                       font, text_size, white, 290, y_line + text_size, True)
    y_line = draw_text(screen,
                       'Use left and right arrow key to select a column',
                       font, text_size, white, 120, y_line)
    y_line = draw_text(screen,
                       'Use space key to switch between piece addition and piece deletion',
                       font, text_size, white, 20, y_line)
    y_line = draw_text(screen,
                       'Use enter key to drop the piece or delete a piece',
                       font, text_size, white, 115, y_line)
    y_line = draw_text(screen,
                       'Use escape key to promptly exit a game',
                       font, text_size, white, 155, y_line)    
    
    # bigger size, double spaced, bolded
    y_line = draw_text(screen, 
                       'Return to main menu',
                       font, 50, yellow, 140, y_line + text_size, True)

    pygame.display.update()

    # since no background animation is present, the maximum fps is set to 10
    # to decrease cpu usage while in this scene. When the player presses
    # the enter key, the scene goes back to 'menu'.    
    while True:
        if return_to_menu(): return 'menu'      
        pygame.time.wait(100)


'''
draw a single line of customized text on the pygame screen. In addition,
return a integer representing the y-position of the next line of text.

Arguments:
    screen (Screen): an instance of pygame class Screen
    text (str): text to be displayed
    style (str): font style
    size (int): font size
    color (tuple): font color as a rgb combination
    x (int): x-position of the top left corner of the text relative to the
             x-position of the top left corner of the window
    y (int): y-position of the top left corner of the text relative to the
             y-position of the top left corner of the window
    bold (bool): bold the text if set to True. It is defaulted as False.
    italic (bool): italasize the text if set to True. It is defaulted as False.

Returns:
    y + size (int): possible y-position of the next line of text
'''
def draw_text(screen, text, style, size, color, x, y,
              bold = False, italic = False):

    text_font = pygame.font.SysFont(style, size, bold, italic)
    text_image = text_font.render(text, False, color)
    screen.surface.blit(text_image, (x, y))
    return y + size # y position of the next line of text


'''
Tells the run_Intruction function to exit itself and have the game return to the
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
