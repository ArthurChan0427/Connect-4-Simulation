##########################################
######### RUN THIS FILE FOR DEMO #########
##########################################

import pygame

from Scenes.Match import run_match
from Scenes.Menu import run_menu
from Scenes.Instruction import run_instruction
from Scenes.Game_over import run_game_over

from Objects.Screen import Screen

'''
Initialize all necessary items to start the program, then enter the game loop.

Arguments -
    None
Returns -
    None
'''
def main():
    # initilize pygame and set initial game scene to 'menu'
    pygame.init()
    game_state = 'menu'
    screen = Screen(700, 700) # instantiate a  700 x 700 pygame window

    # then enter the main game loop
    game_loop(game_state, screen)


'''
Run the appropriate scenes as specified by the variable game_state.

Arguments:
    game_state (str): initial scene
    screen (Screen): an instance of pygame class Screen

Returns:
    None
'''
def game_loop(game_state, screen):
    while True:
        if game_state == 'menu': # menu scene
            game_state = run_menu(screen)
        elif game_state == 'instruction': # instruction scene
            game_state = run_instruction(screen)
        elif game_state == 'pvp' or game_state == 'pve': # match scene
            game_state, winner = run_match(game_state, screen)
        elif game_state == 'game over': # game over scene
            game_state = run_game_over(screen, winner)
        elif game_state == 'exit': # exit procedures
            pygame.quit()
            break


if __name__ == "__main__":
    main()
