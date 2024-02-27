from item import Item
import copy
import pygame

class Bomb(Item):
    def __init__(self, pos, bombaid):
        super().__init__()
        self.posicion_actual = copy.deepcopy(pos)
        self.x, self.y = pos
        self.id = copy.deepcopy(bombaid)
        self.width = 37
        self.height = 37
        self.hitbox = self.posicion_actual[0], self.posicion_actual[1], self.width, self.height
        self.exlpoded = False
        self.lifeSpan = 2000
        self.actualSprite = 0
        self.birthTime = pygame.time.get_ticks()
        self.frameChange = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.birthTime >= self.lifeSpan:
            self.exlpoded = True
        
        if pygame.time.get_ticks() - self.frameChange >= 250:
            self.actualSprite += 1
            if self.actualSprite > len(self.sprites) - 1: self.actualSprite = 0
            self.image = self.sprites[self.actualSprite]
            self.frameChange = pygame.time.get_ticks()

    
    def setImage(self, image):
        self.sprites = image
        self.sprites.append(self.sprites[1]) 
        self.image = self.sprites[self.actualSprite]
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
