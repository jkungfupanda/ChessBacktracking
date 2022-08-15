from re import X
from turtle import width
import pygame
from constants import *

class ChessBoard:

    def __init__(self):
        self.board=[]
        self.selected_piece = None
        rect = (113, 113, 525, 525)
        startX = rect[0]
        startY = rect[1]

    # def draw_squares(self, win, size):
    #     rows = size
    #     cols = size

    #     win.fill(BLACK)
    #     for row in range(rows):
    #         for col in range(row % 2, cols, 2):
    #             pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    def draw_squares(self, win, size):
        rows = size
        cols = size
        numOfQueens = size
        


        boardSize = size * SQUARE_SIZE

        remainingSpace = HEIGHT - (boardSize)

        spaceOnAllSides = remainingSpace/2
        
        border = int(spaceOnAllSides/SQUARE_SIZE)

        win.fill(BLACK)
        for row in range(border, rows + border):
            for col in range(row % 2 + border - 1, cols + border - 1, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


        widthBetweenQueens = 0
        for i in range(numOfQueens):
            
            x = spaceOnAllSides + widthBetweenQueens
            y = spaceOnAllSides + (HEIGHT - remainingSpace) 
            
            win.blit(w_queen,(x,y))
            widthBetweenQueens += boardSize/size  


        





