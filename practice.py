from board import Board
from chessBoard import ChessBoard
from constants import *
from eightQueens import EightQueens
import pygame, sys
from pygame.locals import *
import math
import time
from queen import Queen




def main():
    run = True
    while run:
        clock.tick(60)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

        group.update(event_list)

        window.fill(0)
        group.draw(window)
        pygame.display.flip()

    pygame.quit()
    exit()

class DragOperator:
    def __init__(self, sprite):
        self.sprite = sprite
        self.dragging = False
        self.rel_pos = (0, 0)
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dragging = self.sprite.rect.collidepoint(event.pos)
                self.rel_pos = event.pos[0] - self.sprite.rect.x, event.pos[1] - self.sprite.rect.y
            if event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            if event.type == pygame.MOUSEMOTION and self.dragging:
                self.sprite.rect.topleft = event.pos[0] - self.rel_pos[0], event.pos[1] - self.rel_pos[1]

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 
        self.original_image = queen_img
        window.blit(self.original_image, (x, y))
        # pygame.draw.circle(self.original_image, color, (25, 25), 25)
        self.drag_image = self.original_image
        # pygame.draw.circle(self.drag_image, color, (25, 25), 25)
        # pygame.draw.circle(self.drag_image, (255, 255, 255), (25, 25), 25, 4)
        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.drag = DragOperator(self)
    def update(self, event_list):
        self.drag.update(event_list) 
        self.image = self.drag_image if self.drag.dragging else self.original_image


# print("before init")
# pygame.init()
# print("after init")
window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("N QUEENS PROBLEM")
clock = pygame.time.Clock()

sprite_object = SpriteObject(*window.get_rect().center, (255, 255, 0))
group = pygame.sprite.Group([
    SpriteObject(window.get_width() // 3, window.get_height() // 3, (255, 0, 0)),
    SpriteObject(window.get_width() * 2 // 3, window.get_height() // 3, (0, 255, 0)),
    SpriteObject(window.get_width() // 3, window.get_height() * 2 // 3, (0, 0, 255)),
    SpriteObject(window.get_width() * 2// 3, window.get_height() * 2 // 3, (255, 255, 0)),
])







if __name__ == "__main__":
    # n = int(input("Enter the size of the board: "))
    print("main")
    main()