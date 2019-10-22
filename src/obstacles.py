class Obstacles():

    def __init__(self):
        self.position = []
        self.sprites = None
        self.x = 0
        self.y = 0
        self.width = 37
        self.height = 37
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.getrect = ()
        self.columnasDerechaRect = None
        self.columnasIzquierdaRect = None
        self.filasAbajoRect = None
        self.filasArribaRect = None

    def setPosition(position):
        self.position = position

    def setSprite(sprite):
        self.sprite = sprite
