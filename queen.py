from re import X
import pygame
import random
from constants import *


class Queen(pygame.sprite.Sprite):

    image = queen_img

    def __init__(self,xpos,ypos,id):

        pygame.sprite.Sprite.__init__(self)

        
        self.clicked=False
        self.rect = self.image.get_rect()
        self.rect.y=ypos
        self.rect.x=xpos
        self.id=id

    def updatePosition(self,x,y):
        
        self.rect.y=y
        self.rect.x=x