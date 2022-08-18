from constants import *
import time
from queen import Queen


class ChessBoard:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        rect = (113, 113, 525, 525)
        self.listOfQueens = []


    def draw_squares(self, win, size, clicked):
        """
        Draw squares of size 'size' on the window.
        :param win: the given window of size height x width.
        :param size: size of each square.
        """
        if not clicked:
            listOfRedSquares = []
            listOfYellowSquares = []

            rows = size
            cols = size
            num_queens = size
            queenId = 1

            board_size = size * SQUARE_SIZE
            remaining_space = HEIGHT - board_size
            space_on_sides = remaining_space / 2
            border = int(space_on_sides / SQUARE_SIZE)

            win.fill(BLACK)
            for row in range(border, rows + border):
                for col in range(row % 2 + border - 1, cols + border - 1, 2):
                    pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    listOfRedSquares.append((row * SQUARE_SIZE, col * SQUARE_SIZE))

                for col in range((row + 1) % 2 + border - 1, cols + border - 1, 2):   
                    pygame.draw.rect(win, YELLOW, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    listOfYellowSquares.append((row * SQUARE_SIZE, col * SQUARE_SIZE))



            queens_padding = 0
            for i in range(num_queens):
                x = space_on_sides + queens_padding
                y = space_on_sides + (HEIGHT - remaining_space)
                queen = Queen(x,y,queenId)
                self.listOfQueens.append(queen)
                # win.blit(queen.image, (queen.rect.x, queen.rect.y))
                self.draw_queen(win, queen)
                queens_padding += board_size / size
                queenId +=1
                # if (queenId < size):
                #     print(queen.id,queen.rect.x, queen.rect.y)

        else:
            pass



    # def draw_starting_queens(self, win, num_queens):
    #     queens_padding = 0
    #     for i in range(num_queens):
    #         x = space_on_sides + queens_padding
    #         y = space_on_sides + (HEIGHT - remaining_space)
    #         queen = Queen(x,y,queenId)
    #         self.listOfQueens.append(queen)
    #         # win.blit(queen.image, (queen.rect.x, queen.rect.y))
    #         self.draw_queen(win, queen)
    #         queens_padding += board_size / size
    #         queenId +=1
    #         # if (queenId < size):
    #         #     print(queen.id,queen.rect.x, queen.rect.y)
    #     win.blit(queen.image, (queen.rect.x, queen.rect.y))

    def draw_queen(self, win, queen):
        win.blit(queen.image, (queen.rect.x, queen.rect.y))




        # coordinates = zip(listOfRedSquares, listOfYellowSquares)
        # [print(i) for i in coordinates]

        # coordinates = [(x, y) for x, y in zip(listOfRedSquares, listOfYellowSquares)]
        # for i, j in coordinates:
        #     x = 1
        #     if x == 36:
        #         break
        #     print(i, j, end=" ")
        #     x += 1
        # print(coordinates)


        # [print(i) for i in listOfRedSquares]
        # print("\n")
        # print("yellow starts here")
        # [print(i) for i in listOfYellowSquares]
        # time.sleep(300)


    """
    def draw_squares(self, win, size):
        rows = size
        cols = size
        win.fill(BLACK)
        for row in range(rows):
            for col in range(row % 2, cols, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    """
