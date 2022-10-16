from re import X
import pygame
import random
from constants import *
import pygame, sys
from pygame.locals import *


class Queen(pygame.sprite.Sprite):

    image = queen_img

    def __init__(self, x, y, window):
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








    # def __init__(self,xpos,ypos,id):

    #     pygame.sprite.Sprite.__init__(self)

        
    #     self.clicked=False
    #     self.rect = self.image.get_rect()
    #     self.rect.y=ypos
    #     self.rect.x=xpos
    #     self.id=id

    # def updatePosition(self,x,y,win):
        
    #     self.rect.y=y
    #     self.rect.x=x
    #     win.blit(Queen.image, (self.rect.x, self.rect.y))




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



