from dynamicObject import DynamicObject


class Enemy(DynamicObject):
    def __init__(self, position, tipodemovimiento):
        super().__init__()
        self.position = position
        self.lifes = None
        self.speed = 1
        self.sprite = None
        self.posicionanterior = None
        self.direccion = 1
        self.tipodemovimiento = tipodemovimiento
        self.animacion = tipodemovimiento

        # Colisiones
        self.x = self.position[0]
        self.y = self.position[1]
        self.width = 30
        self.height = 30
        self.hitbox = (self.x , self.y , self.width, self.height)  # Dibujo un cuadrado
        self.rect = None

    def defineMovement(self):
        pass

    #Getters

    def getEnemyPosition(self):
        return self.position
    
    def getEnemyLifes(self):
        return self.lifes

    def getEnemySpeed(self):
        return self.speed

    def getEnemyHitbox(self):
        self.hitbox = (self.position[0], self.position[1], self.width, self.height)
        return self.hitbox

    def getEnemyRect(self):
        return self.rect

    def getEnemyPosicionAnterior(self):
        return self.posicionanterior

    def getEnemyDireccion(self):
        return self.direccion

    def getEnemyTipoDeMovimiento(self):
        return self.tipodemovimiento
    #Setters

    def setEnemySprite(self, sprite):
        self.sprite = sprite

    def setEnemyRect(self, rect):
        self.rect = rect
    
    def setPosition(self, position):
        self.position = position
    
    def setPosicionAnterior(self, posicion):
        self.posicionanterior = posicion
    
    def setEnemyDireccion(self, direccion):
        self.direccion = direccion
    
    def setEnemyAnimacion(self, numero):
        self.animacion = tipodemovimiento + str(numero)

