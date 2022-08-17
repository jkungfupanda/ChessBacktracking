import pygame
import random
from constants import *


class Queen:

    image = queen_img

    def __init__(self,xpos,ypos,id):

        
        self.clicked=False
        self.rect = self.image.get_rect()
        self.rect.y=ypos
        self.rect.x=xpos
        self.id=id