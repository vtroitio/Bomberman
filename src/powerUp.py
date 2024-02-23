import pygame
import item

class PowerUp(item.Item):
    def __init__(self, tipo, image, position):
        super().__init__()
        self.type = tipo
        self.image = image
        self.rect = self.image.get_rect()
        self.x, self.y = position
        self.lifeSpan = 6000
        self.birthTime = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.birthTime >= self.lifeSpan:
            self.kill()

    def getType(self):
        return self.type

    def getPosition(self):
        return self.x, self.y
    
    def getWorldRect(self):
        return pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
