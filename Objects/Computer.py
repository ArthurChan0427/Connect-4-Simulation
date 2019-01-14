import numpy
import pygame
import random
import math
import collections

from Objects.Piece import Piece

# global identifiers each representing a RGB colour
blue = (0,0,255)
black = (0,0,0)
red = (255, 0, 0)
yellow = (255, 255, 0)

class Computer(): 
    def __init__(self):
        self._first_move = True
        self._second_move = True
        self._third_move = True
        self._fourth_move = True


    def drop_piece(self, board, pieces):
        ypos = 0
        xpos_list = []
        for piece in pieces:
            xpos_list.append(piece.x)

        redxpos_list = []
        for piece in pieces:
            if piece.colour == red:
                redxpos_list.append(piece.x)

        yellowxpos_list = []
        for piece in pieces:
            if piece.colour == yellow:
                yellowxpos_list.append(piece.x) 
                
        sortedredxpos_list = sorted(redxpos_list)
        
        sortedxpos_list = sorted(xpos_list)
        
        sortedyellowxpos_list = sorted(yellowxpos_list)
        
        ypos_list = []
        for piece in pieces:
            ypos_list.append(piece.y)        
        
        redypos_list = []
        for piece in pieces:
            if piece.colour == red:
                redypos_list.append(piece.y)
        
        yellowypos_list = []
        for piece in pieces:
            if piece.colour == yellow:
                yellowypos_list.append(piece.y)
                
        sortedredypos_list = sorted(redypos_list)
        
        sortedypos_list = sorted(ypos_list)
        
        sortedyellowypos_list = sorted(yellowypos_list)
                
        while True:          
            if self._first_move == True: #first move 
                self._first_movexpos = int((2 + 0.5) * board.unit_size)
                pieces.append(Piece((self._first_movexpos,ypos), board.c_radius, yellow))
                self._first_move = False
                break
            
            elif self._second_move == True: #second move
                self._second_movexpos = int((random.randint(4,6) + 0.5) * board.unit_size)
                pieces.append(Piece((self._second_movexpos,ypos), board.c_radius, yellow))
                self._second_move = False
                break
            
            #if there is a 3 stack block it
            elif [item for item, count in collections.Counter(sortedxpos_list).items() if count == 3]:
                dupxpos_list = [item for item, count in collections.Counter(sortedxpos_list).items() if count == 3]
                vertical_blockxpos = dupxpos_list[0]
                if not any((piece.y <= 1.5 * board.unit_size and piece.x == vertical_blockxpos) for piece in pieces):
                    pieces.append(Piece((vertical_blockxpos,ypos), board.c_radius, yellow))
                    break  
                
            #if you have a 3 stack attack it
            elif [item for item, count in collections.Counter(sortedxpos_list).items() if count == 3]:
                dupxpos_list = [item for item, count in collections.Counter(sortedyellowxpos_list).items() if count == 3]
                vertical_attackxpos = dupxpos_list[0]
                if not any((piece.y <= 1.5 * board.unit_size and piece.x == vertical_attackxpos) for piece in pieces):
                    pieces.append(Piece((vertical_attackxpos,ypos), board.c_radius, yellow))
                    break             
                
            #Initial moves to not get wrecked if needed   
            elif self._third_move == True:
                self._third_movexpos =int((random.randint(0,3) + 0.5) * board.unit_size)
                pieces.append(Piece((self._third_movexpos,ypos), board.c_radius, yellow))
                self._third_move = False    
                break
            
            #Initial moves to not get wrecked if needed
            elif self._fourth_move == True:
                self._fourth_move = int((random.randint(4,6) + 0.5) * board.unit_size)
                pieces.append(Piece((self._fourth_move,ypos), board.c_radius, yellow))
                self._second_move = False
                break                      
            
            else: 
                xpos = int((random.randint(0,6)+0.5)*board.unit_size)
                if not any((piece.y <= 1.5 * board.unit_size and piece.x == xpos) for piece in pieces):
                    pieces.append(Piece((xpos,ypos), board.c_radius, yellow))
                    break