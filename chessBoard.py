import pygame
from constants import *

class ChessBoard:

    def __init__(self):
        self.board=[]
        self.selected_piece = None
        rect = (113, 113, 525, 525)
        startX = rect[0]
        startY = rect[1]

    def draw_squares(self, win, size):
        rows = size
        cols = size

        win.fill(BLACK)
        for row in range(rows):
            for col in range(row % 2, cols, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

