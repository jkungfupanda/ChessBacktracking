from eightQueens import EightQueens
from board import Board
import pygame
import os
# import time

WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("N QUEENS PROBLEM")
w_queen = pygame.image.load(os.path.join("white_queen.png"))
w_queen= pygame.transform.scale(w_queen,(25,20))
chess_board = pygame.image.load(os.path.join("chess_board.png"))
w_queen= pygame.transform.scale(w_queen,(200,50))



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 60


class chessBoard:
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]





def draw_window():
    WIN.fill(YELLOW)

    WIN.blit(chess_board,(1,1))
    WIN.blit(w_queen,(10,10))

    pygame.display.update()




def main(size):
    clock=pygame.time.Clock()

    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        draw_window()


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
    main(size)
