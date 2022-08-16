from board import Board
from chessBoard import ChessBoard
from constants import *
from eightQueens import EightQueens
import pygame, sys
from pygame.locals import *
import math



def main(size, make_board=True, run_eight_queens=False):
    """
    Run either the 8-Queens problem or create a size-by-size board for the game.
    :param size: size of the 8-queens problem or size of the board.
    :param make_board: boolean true if to make a board.
    :param run_eight_queens: boolean true if to run the 8-queens problem.
    """

    if make_board:
        window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("N QUEENS PROBLEM")

        clock = pygame.time.Clock()
        chess_board = ChessBoard()

        mx, my = pygame.mouse.get_pos()


        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     m_x, m_y = pygame.mouse.get_pos()
                #         for queen in queens: #for each queen
                #             dis=math.sqrt((x-m_x)**2+(y-m_y)**2) #distance mouse is from border of each queen
                #                 if dis<RADIUS:              # if mouse is within the borders of one of the queens
                    
                    
                    
                    
                    
                    # if event.button == 1:
                    #     clicking = True
                        # chess_board.draw_squares(window, size)
                    


            chess_board.draw_squares(window, size)
            pygame.display.update()
            # draw_window()

        pygame.quit()

    if run_eight_queens:
        b = Board(size)
        x = EightQueens(b)

        [print(i) for i in x.outputs]
        print("-----------------------------")
        print("Number of iterations: " + str(len(x.outputs)))
        print("Final board: ")
        print(x.outputs[-1])


if __name__ == "__main__":
    n = int(input("Enter the size of the board: "))
    main(n)

# TODO
"""
1. how to move queens 
    a. get the x and y coordinates of the queens
    b. if the mouse is within some distance from a queen AND clicking then move the queen wherever the mouse goes
    c. get the x and y coordinates of each of the squares on the board
    d. If the queen is close to a defined square on the board then place the queen there...else return the queen to it's original posiiton
2. write program to tell the user if the queen is not attacking other queens
3. if they win the game it says they won,,, if not backtracking algorithm solves for them
"""


"""
--------------------------- OLD CODE ------------------------------

chess_board = pygame.image.load(os.path.join("chess_board.png"))
chess_board = pygame.transform.scale(chess_board,(700,350))

def create_board(size):
   field = [[0 for _ in range(size)]for _ in range(size)]

def draw_window():
    WIN.fill(YELLOW)
    WIN.blit(chess_board,(100,60))
    WIN.blit(w_queen,(10,10))
    pygame.display.update()
"""
