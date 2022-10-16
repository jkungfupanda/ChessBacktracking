import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (32,42,68)
GRAY = (211,211,211)
FPS = 60
WIDTH, HEIGHT = 1000, 1000
SQUARE_SIZE = 70
QUEEN_SIZE = 50
queen_img = pygame.image.load(os.path.join("Assets", "white_queen.png"))
queen_img = pygame.transform.scale(queen_img, (QUEEN_SIZE, QUEEN_SIZE))
