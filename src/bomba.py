from item import *
import time
import copy
import pygame
import threading
from explosion import Explosion

class Bomb(Item):
    def __init__(self, pos, bombaid):
        super().__init__()
        self.posicion_actual = copy.deepcopy(pos)
        self.x, self.y = pos
        self.id = copy.deepcopy(bombaid)
        self.width = 21
        self.height = 18
        self.offset = 8
        self.hitbox = self.posicion_actual[0] + self.offset, self.posicion_actual[1] + self.offset, self.width, self.height
        self.exlpoded = False
        self.lifeSpan = 2000
        self.birthTime = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.birthTime >= self.lifeSpan:
            self.exlpoded = True
    
    def setImage(self, image):
        self.image = image
        self.rect = self.image.get_rect()
    
    def getposicion(self):
        return self.posicion_actual
    
    def getId(self):
        return self.id
    
    def getHitbox(self):
        return self.hitbox 

    def getRect(self):
        return self.rect
    
    def setRect(self, rect):
        self.rect = rect
    
    def setBombRect(self, attr):
        self.rect = attr

    def getBombRect(self):
        return self.rect
    
    def explode(self):
        return self.exlpoded