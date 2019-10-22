class Obstacles():

    def __init__(self, x, y):
        self.position = []
        self.sprites = None
        self.x = 0
        self.y = 0
        self.width = 37
        self.height = 37
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.listadeobstaculos = []

    def setPosition(self, position):
        self.position = position

    def setSprite(self, sprite):
        self.sprite = sprite

    def loadObstacles(self):
        self.listadeobstaculos.append(self.x, self.y)

    def setListaDeObstaculos(self, ubicacion):
        self.listadeobstaculos.append(ubicacion)
