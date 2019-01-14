# This file contains all attributes and methods of the class Board

# Board represents the casing which holds the pieces that the players have
# placed. It is on the screen as a blue rectangular casing with 7 x 6 black
# circles representing the holes. Beside acting as a holder of pieces, it also
# acts as a referee of a match and will announce a winner when one and only one
# colour has achieved a sequence of 4 connected pieces.

import pygame

# global identifiers each representing a RGB colour
blue = (0,0,255)
black = (0,0,0)
red = (255, 0, 0)
yellow = (255, 255, 0)

class Board():
    def __init__(self, screen, row, column, c_radius):
        self._row = row # the number of rows
        self._column = column # the number of columns
        self.c_radius = c_radius # the radius of each hole
        self.unit_size = int(screen.width / 7) # the spacing between the
                                               # the center of each hole


    '''
    Draw the single blue rectangle representing
    the casing of the board on the screen.
    
    Arguments:
        screen (Screen): an instance of pygame class Screen
    
    Returns:
        None
    '''    
    def draw_rect(self, screen):
        pygame.draw.rect(screen.surface, blue, (0, self.unit_size, screen.width,
                                                screen.height - self.unit_size))


    '''
    Draw 42 black circles in a uniformly distributed 6 x 7 grid representing
    the holes of the game board.
    
    Arguments:
        screen (Screen): an instance of pygame class Screen
    
    Returns:
        None
    '''    
    def draw_holes(self, screen):
        for c in range(self._column):
            for r in range(self._row):
                c_pos = {'x': int(self.unit_size * (c + 0.5)),
                         'y': int(self.unit_size * (r + 1.5))}
                pygame.draw.circle(screen.surface, black, 
                                   (c_pos['x'], c_pos['y']), self.c_radius)
    

    '''
    Determine if a winner is present from the list "pieces" which contains the
    all instances of Piece in their current state.
    
    The winner, either 'red' or 'yellow', is declared when one of them achieves
    a sequence of 4 pieces connected in either vertical, horizontal, negative
    diagonal, or positive diagonal orientation.
    
    If both colours achieve a sequence of 4 in the current state, then it is
    considered 'tied', and no winner is announced.
    
    Arguments:
        pieces (list): all existing instances of Piece
    
    Returns:
        winner (str or None): 'red' or 'yellow' representing the winner of the
                              match. If no winner exists, it is set to None.
    '''                
    def check_winner(self, pieces):
        winner = None
        
        # check all existing instance of Piece (p1) with all other instances
        # of Pieces (p2) for alignment, and place the distinguishing attribute
        # of the instance of Piece in the appropriate array (ver, hor, n_dia,
        # p_dia). The comparison is done for stationary instance of Piece only.
        for p1 in pieces:
            ver = [p1.y] # pieces aligned vertically with p1
            hor = [p1.x] # pieces aligned horizontally with p1
            n_dia = [p1.x] # pieces aligned negative diagonally with p1
            p_dia = [p1.x] # pieces aligned positive diagonally with p1
           
            if p1.is_stationary:
                for p2 in pieces:
                    if p1.colour == p2.colour and p2.is_stationary:
                        if p1.x == p2.x and p1.y != p2.y:
                            ver.append(p2.y)
                        elif p1.y == p2.y and p1.x != p2.x:
                            hor.append(p2.x)
                        elif p1.x != p2.x and (p2.y - p1.y)/(p2.x - p1.x) == 1:
                            n_dia.append(p2.x)
                        elif p1.x != p2.x and (p2.y - p1.y)/(p2.x - p1.x) == -1:
                            p_dia.append(p2.x)

                # place the all resulting arrays into a single array to
                # allow for looping
                aligned = [ver, hor, n_dia, p_dia]
                for _aligned in aligned:
                    counter = 0
                    
                    # if 4 or more pieces are aligned in the given orientation
                    # then proceed to sort the position values in the given
                    # array in an increasing order.
                    if len(_aligned) >= 4:
                        _aligned.sort()
                        
                        # loop through each number starting from index 1,
                        # if the difference between the current and previous
                        # position value is equal to the distance between the
                        # center of the holes, then increment the counter
                        # representing the number of connected pieces by 1.
                        # Otherwise, reset the counter since the sequence
                        # has been broken.
                        for i in range(1, len(_aligned)):
                            if _aligned[i] - _aligned[i-1] == self.unit_size:
                                counter += 1
                            else:
                                counter = 0
                            
                            # If the counter reaches 3, which means that a
                            # sequence of 4 connect pieces is achieved, the
                            # colour of the pieces is assigned to the variable
                            # "winner". However, If the opposing player has
                            # also achieved a sequence of 4 connected pieces
                            # at the current state of the match, then the
                            # winner is assigned 'tied'.
                            if counter == 3:
                                if winner != 'tied' and \
                                   (winner is None or winner == p1.colour):
                                    winner = p1.colour
                                else:
                                    winner = 'tied'

        # After checking all pieces (p1), return the winner of match.
        # If no winner exist or the match is 'tied' at the current state
        # of the match, return None.
        if winner == red:
            return 'red'
        elif winner == yellow:
            return 'yellow'
        elif winner == 'tied':
            return None
