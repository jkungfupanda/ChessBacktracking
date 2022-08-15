import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 60
WIDTH,HEIGHT=1000,1000
SQUARE_SIZE = 70
QUEEN_SIZE = 50
w_queen = pygame.image.load(os.path.join("white_queen.png"))
w_queen= pygame.transform.scale(w_queen,(QUEEN_SIZE, QUEEN_SIZE))

