class Obstacle():

    def __init__(self, x, y):
        self.position = []
        self.sprites = None
        self.x = x
        self.y = y
        self.width = 37
        self.height = 37
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.obstacleRect = None
        self.rompible = None

# Setters

    def setObstacleRect(self, ObstacleRect):
        self.obstacleRect = ObstacleRect

    def setPosition(self, position):
        self.position = position

    def setSprite(self, sprite):
        self.sprite = sprite

    def setRompible(self, valor): #Cuando instancie los objetos rompibles les seteo esto para despues poder usarlo con la explosion de la bomba
        self.rompible = valor

# Getters

    def getHitbox(self):
        return self.hitbox

    def getPosition(self):
        return [self.x, self.y]

    def getObstacleRect(self):
        return self.obstacleRect
    
    def getObstacleRompible():
        return self.rompible
