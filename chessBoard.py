from constants import *


class ChessBoard:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        rect = (113, 113, 525, 525)

    @classmethod
    def draw_squares(cls, win, size):
        """
        Draw squares of size 'size' on the window.
        :param win: the given window of size height x width.
        :param size: size of each square.
        """

        rows = size
        cols = size
        num_queens = size

        board_size = size * SQUARE_SIZE
        remaining_space = HEIGHT - board_size
        space_on_sides = remaining_space / 2
        border = int(space_on_sides / SQUARE_SIZE)

        win.fill(BLACK)
        for row in range(border, rows + border):
            for col in range(row % 2 + border - 1, cols + border - 1, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        queens_padding = 0
        for i in range(num_queens):
            x = space_on_sides + queens_padding
            y = space_on_sides + (HEIGHT - remaining_space)

            win.blit(queen_img, (x, y))
            queens_padding += board_size / size

    """
    def draw_squares(self, win, size):
        rows = size
        cols = size
        win.fill(BLACK)
        for row in range(rows):
            for col in range(row % 2, cols, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    """
