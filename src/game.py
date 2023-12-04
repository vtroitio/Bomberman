import wall
import box
import player
import obstacles
import player
import enemy
import copy
from random import shuffle
import speed
import LifeUp
import bombUp


class Game():

    def __init__(self):
        self.wall = wall.Wall()
        self.box = box.Box()
        self.player = player.Player()

        self.LaListaDeObstaculos = []
        self.lalistaderects = []

        self.lalistadeenemigos = []
        self.lalistaderectsenemigos = []
        self.positionAnteriorEnemy = []

        self.lalistadecajas = []
        self.lalistaderectscajas = []

        self.listarandom = [0, 1, 2, 3, 4, 5]

        self.lalistadepowerUpsSpeed = []
        self.lalistadepowerUpsVida = []
        self.lalistadepowerUpsBomba = []

        self.lalistadepowerUpsSpeed = []
        self.lalistaderectspowerUpsSpeed = []

        self.lalistadepowerUpsBomba = []
        self.lalistaderectspowerUpsBomba = []

        self.lalistadepowerUpsVida = []
        self.lalistaderectspowerUpsVida = []

# Crea a los enemigos que ya tienen una posicion pre establecida en el mapa
# al instanciarlos les pasa su posicion y como va a ser su movimiento pre
# establecido.

    def placeEnemies(self):
        self.lalistadeenemigos.append(enemy.Enemy([39, 259],
                                                  "vertical", "vertical1"))
        self.lalistadeenemigos.append(enemy.Enemy([111, 187],
                                                  "horizontal", "horizontal1"))
        self.lalistadeenemigos.append(enemy.Enemy([187, 40],
                                                  "vertical", "vertical1"))
        self.lalistadeenemigos.append(enemy.Enemy([185, 335],
                                                  "horizontal", "horizontal1"))
        self.lalistadeenemigos.append(enemy.Enemy([484, 37],
                                                  "horizontal", "horizontal1"))
        self.lalistadeenemigos.append(enemy.Enemy([407, 148],
                                                  "vertical", "vertical1"))
        self.lalistadeenemigos.append(enemy.Enemy([484, 400],
                                                  "vertical", "vertical1"))
        self.lalistadeenemigos.append(enemy.Enemy([632, 400],
                                                  "vertical", "vertical1"))
        self.lalistadeenemigos.append(enemy.Enemy([669, 487],
                                                  "horizontal", "horizontal1"))
        self.lalistadeenemigos.append(enemy.Enemy([780, 333],
                                                  "vertical", "vertical1"))
        self.lalistadeenemigos.append(enemy.Enemy([777, 260],
                                                  "horizontal", "horizontal1"))
        self.lalistadeenemigos.append(enemy.Enemy([851, 400],
                                                  "vertical", "vertical1"))

# Cuando se rompa una caja se va a llamar(dependiendo del numero que salga a
# la creacion de alguno de estos powerups que luego seran bliteados por la 
# vista.

    def createPowerUpSpeedUp(self, posicion):
        self.lalistadepowerUpsSpeed.append(speed.Speed(posicion))

    def createPowerUpVida(self, posicion):
        self.lalistadepowerUpsVida.append(LifeUp.LifeUp(posicion))

    def createPowerUpBombUp(self, posicion):
        self.lalistadepowerUpsBomba.append(bombUp.BombUp(posicion))


# Crea los obstaculos no rompibles, los pilares grises, estos creandose segun
# las dimensiones que tenga la pantalla, idealmente para que los bloques queden
# bien situados, la altura y ancho de la pantalla de pygame deben ser multiplos
# de 37 ya que ese es el ancho y alto de nuestro bloque, de lo contrario no
# quedara una pantalla simetrica.

    def createObstacles(self, dimensions):
        WidthHeightObstacle = 37  # Tamaño del bloque utilizado

        for i in range(0, int((dimensions[0] / WidthHeightObstacle)) + 1):  # De 0 a 26

            self.LaListaDeObstaculos.append(obstacles.Obstacle(i * WidthHeightObstacle, 0))  # Creo los bloques de la fila de arriba

            self.LaListaDeObstaculos.append(obstacles.Obstacle(i * WidthHeightObstacle, dimensions[1] - WidthHeightObstacle))  # Creo los bloques de la fila de abajo

        for i in range(0, int((dimensions[1] / WidthHeightObstacle)) + 1):  # De 0 a 16

            self.LaListaDeObstaculos.append(obstacles.Obstacle(0, i * WidthHeightObstacle))  # Creo los bloques de las columnas de la izquierda

            self.LaListaDeObstaculos.append(obstacles.Obstacle(dimensions[0] - WidthHeightObstacle, i * WidthHeightObstacle))  # Creo los bloques de las columnas de la derecha

        for x in range(1, int((dimensions[0] / (WidthHeightObstacle * 2))) + 1):  # De 1 a 13
            for y in range(1, int((dimensions[1]) / (WidthHeightObstacle * 2)) + 1):  # De 1 a 8
                self.LaListaDeObstaculos.append(obstacles.Obstacle(x * (WidthHeightObstacle * 2), y * (WidthHeightObstacle * 2))) # Creo los bloques en el centro de la pantalla

# Crea los rects que se utilizan para colisiones recorriendo cada
# tipo de objeto en memoria agregado previamente a la lista que le
# corresponde y lo agrega a la lista de rects de su tipo.
    def createRects(self):
        for obstaculo in self.LaListaDeObstaculos:
            self.lalistaderects.append(obstaculo.getObstacleRect())
        for enemy in self.lalistadeenemigos:
            self.lalistaderectsenemigos.append(enemy.getEnemyRect())
        for cajas in self.lalistadecajas:
            self.lalistaderectscajas.append(cajas.getObstacleRect())

    def createEnemiesRects(self):
        for enemy in self.lalistadeenemigos:
            self.lalistaderectsenemigos.append(enemy.getEnemyRect())

    def createBoxesRects(self):
        for cajas in self.lalistadecajas:
            self.lalistaderectscajas.append(cajas.getObstacleRect())

# MOVIMIENTO

    def givePosition(self, position, ventana):
        self.player.move(position, ventana)
# Geters

    def getBombermanPosition(self):
        return self.player.getBombermanPosition()

    def getBombermanPositionAnterior(self):
        return self.player.getBobmermanPositionAnterior()

    def getBombermanSpeed(self):
        return self.player.getBombermanSpeed()

    def getBombermanDirection(self):
        return self.player.getBombermanDirection()

    def getdireccionenemigo(self, numerodeenemigo):
        enemigodeseado = self.lalistadeenemigos[numerodeenemigo]
        return enemigodeseado.getEnemyDireccion()

    def getPlayerHitbox(self):
        return self.player.getPlayerHitbox()

    def getBombermanVidas(self):
        return self.player.lifes

# Setters
    def setBombermanPosition(self):
        self.player.setBombermanPosition()

    def setBombermanPosicionDeInicio(self):
        self.player.setPosition([37, 37])

    def setPositionAnterior(self, enemigodeseado):
        enemy = self.lalistadeenemigos[enemigodeseado]
        enemy.setPosition(enemy.getEnemyPosicionAnterior())

    def setdireccionenemigo(self, direccion, numerodeenemigo):
        enemigodeseado = self.lalistadeenemigos[numerodeenemigo]
        enemigodeseado.setEnemyDireccion(direccion)

    def setBombermanSpeed(self, velocidad):
        self.player.setSpeed(velocidad)

    def setBombermanVidas(self, vida):
        self.player.setLifes(vida)

# El movimiento del enemigo funciona de forma que al que lo
# que hace es revisar el self.movimiento del enemigo para
# saber si debe moverse vertical o horizontalmente y lo mueve
# dependiendo su velocidad y su direccion la cual se cambia
# en el controlador cuando este detecte que el enemigo
# colisiono.

    def moverEnemigo(self):
        for enemy in self.lalistadeenemigos:
            tipodemovimiento = enemy.getEnemyTipoDeMovimiento()
            if tipodemovimiento == "vertical":
                enemy.setPosicionAnterior(copy.deepcopy(enemy.getEnemyPosition())) 
                self.positionAnteriorEnemy = enemy.getEnemyPosicionAnterior()  

                self.nuevaposicion = [self.positionAnteriorEnemy[0], (self.positionAnteriorEnemy[1] + (1 * enemy.getEnemySpeed()) * enemy.getEnemyDireccion())]
                enemy.setPosition(self.nuevaposicion)

                self.lalistaderectsenemigos.clear()
            else:
                enemy.setPosicionAnterior(copy.deepcopy(enemy.getEnemyPosition())) 
                self.positionAnteriorEnemy = enemy.getEnemyPosicionAnterior()      

                self.nuevaposicion = [(self.positionAnteriorEnemy[0] + (1 * enemy.getEnemySpeed()) * enemy.getEnemyDireccion()), self.positionAnteriorEnemy[1]]
                enemy.setPosition(self.nuevaposicion)

                self.lalistaderectsenemigos.clear()

# COLISIONES
# Getters de listas de objetos

    def getListaDeObstaculos(self):
        return self.LaListaDeObstaculos

    def getListaDeCajas(self):
        return self.lalistadecajas

    def getListaDeEnemigos(self):
        return self.lalistadeenemigos

    def getListaDeSpeedPowerUp(self):
        return self.lalistadepowerUpsSpeed

    def getListaDeLifePowerUp(self):
        return self.lalistadepowerUpsVida

    def getListaDeBombPowerUp(self):
        return self.lalistadepowerUpsBomba


# Setters de listas de objetos

    def setLaListaDeCajas(self, x, y):
        self.lalistadecajas.append(obstacles.Obstacle(x, y))

# Getters de listas de rects

    def getlalisaderectsenemigos(self):
        return self.lalistaderectsenemigos

    def getListaDeRects(self):
        return self.lalistaderects

    def getEnemyRect(self):
        return self.lalistaderectsenemigos

    def getLaListaDeRectsCajas(self):
        return self.lalistaderectscajas

    def getPlayerRect(self):
        return self.player.getPlayerRect()

    def getSpeedUpRect(self):
        return self.lalistaderectspowerUpsSpeed

    def getLifeUpRect(self):
        return self.lalistaderectspowerUpsVida

    def getBombUpRect(self):
        return self.lalistaderectspowerUpsBomba

# Setters de listas de rects

    def setPlayerRect(self, rect):
        self.player.setPlayerRect(rect)

    def setlalistaderectsenemigos(self, cosa):
        self.lalistaderectsenemigos.append(cosa)

    def setLalistaDeRectsCajas(self, rect):
        self.lalistaderectscajas.append(rect)

    def setRectSpeedUp(self, rect):
        self.lalistaderectspowerUpsSpeed.append(rect)

    def setRectBombUp(self, rect):
        self.lalistaderectspowerUpsBomba.append(rect)

    def setRectLifeUp(self, rect):
        self.lalistaderectspowerUpsVida.append(rect)

# Borrar Rects y Sprites

    def romperCaja(self, numerodecaja):
        caja = self.lalistadecajas[numerodecaja]
        self.posicioncajarota = caja.getPosition()
        self.lalistadecajas.pop(numerodecaja)
        self.lalistaderectscajas.pop(numerodecaja)

    def borarSpeedUp(self, indice):
        self.lalistadepowerUpsSpeed.pop(indice)
        self.lalistaderectspowerUpsSpeed.pop(indice)

    def borarBombUp(self, indice):
        self.lalistadepowerUpsBomba.pop(indice)
        self.lalistaderectspowerUpsBomba.pop(indice)

    def borarLifeUp(self, indice):
        self.lalistadepowerUpsVida.pop(indice)
        self.lalistaderectspowerUpsVida.pop(indice)

    def borarDatosCajas(self):
        self.lalistadecajas.clear()
        self.lalistaderectscajas.clear()

    def borrarDatosEnemigos(self):
        self.lalistadeenemigos.clear()
        self.lalistaderectsenemigos.clear()

# Getters

    def getCajaRota(self):  # Devuelvo la posicion de la caja que se rompio que previamente guarde en rompercaja
        return self.posicioncajarota

    def getListaRandom(self):  # Esto lo uso para randomizar la aparicion de determinados PowerUps
        shuffle(self.listarandom)
        return self.listarandom[0]