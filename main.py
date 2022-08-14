from eightQueens import EightQueens
from board import Board
import pygame
import os
from constants import *
from chessBoard import ChessBoard
import time




WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("N QUEENS PROBLEM")


# chess_board = pygame.image.load(os.path.join("chess_board.png"))
# chess_board = pygame.transform.scale(chess_board,(700,350))


w_queen = pygame.image.load(os.path.join("white_queen.png"))
w_queen= pygame.transform.scale(w_queen,(25,20))







# def create_board(size):
#    field = [[0 for _ in range(size)]for _ in range(size)]


# def draw_window():
#     WIN.fill(YELLOW)

#     WIN.blit(chess_board,(100,60))
#     WIN.blit(w_queen,(10,10))

#     pygame.display.update()




def main(size):
    clock=pygame.time.Clock()

    board = ChessBoard()

    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False


            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                  
        board.draw_squares(WIN, size)
        pygame.display.update()
        #draw_window()


    pygame.quit()






    # b = Board(size)
    # x = EightQueens(b)

    # [print(i) for i in x.outputs]

    # print("-----------------------------")
    # print("Number of iterations: " + str(len(x.outputs)))
    # print("Final board: ")
    # print(x.outputs[-1])


if __name__ == "__main__":
    size = int(input("Enter the size of the board: "))

    time.sleep(2)
    main(size)
