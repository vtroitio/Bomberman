import pygame

class Explosion():
    def __init__(self, pos, id_bomba, rects):
        self.lifeSpan = 300
        self.birthTime = pygame.time.get_ticks()
        self.concluded = False
        self.position = pos
        self.id = id_bomba
        self.rects = rects

    def update(self):
        if pygame.time.get_ticks() - self.birthTime >= self.lifeSpan:
            self.concluded = True

    def getPosition(self):
        return self.position
    
    def getId(self):
        return self.id
    
    def conclude(self):
        return self.concluded