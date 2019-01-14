Included Files:
   /Objects
   Board.py
   Computer.py
   Input_cursor.py
   Piece.py
   Screen.py
   /Scenes
       Game_over.py
       Instruction.py
       Match.py
       Menu.py
   Connect4.py
   README
    
Running Instructions:
    1. Navigate to the folder containing the file "Connect4.py"
    2. Open the terminal and enter the command "python3 Connect4.py"
        
Notes and Assumptions:
   This program is a video simulation of the board game Connect 4. In a basic game of Connect 4, two players take
   turn dropping a piece of a distinct colour (typically red vs. yellow) into a 6 x 7 board. The objective is
   to be the first to achieve a sequence of 4 connected pieces in any of the 4 orientations (vertical, horizontal,
   positive diagonal, negative diagonal).
   
   In addition to the basic mechanics of Connect 4, players can choose to delete (or pop out) a piece of their own
   colour located at the bottom row as a single move, which causes all existing pieces above to drop by 1 unit. This 
   allows for a greater strategic depth while preventing the match to end in a stalemate when the 42 slots of the
   board are completely filled.
   
