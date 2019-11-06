from item import *
import time
import copy
import pygame
import threading

class Bomb(Item):
    def __init__(self, pos, bombaid):
        self.posicion_actual = copy.deepcopy(pos)
        self.explotar()
        self.id = copy.deepcopy(bombaid)

    def getposicion(self):
        return self.posicion_actual
    
    def explotar(self):
        pass
    
    def getId(self):
        return self.id
        