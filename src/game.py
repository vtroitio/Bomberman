import wall
import box
import player
import obstacles
import player
import enemy
import copy
import bomba
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

        self.enemigos = []
        self.lalistaderectsenemigos = []
        self.positionAnteriorEnemy = []

        self.lalistadecajas = []
        self.lalistaderectscajas = []

        self.bombas = []
        
        self.lalistadepowerUpsSpeed = []
        self.lalistadepowerUpsVida = []
        self.lalistadepowerUpsBomba = []

        self.lalistadepowerUpsSpeed = []
        self.lalistaderectspowerUpsSpeed = []

        self.lalistadepowerUpsBomba = []
        self.lalistaderectspowerUpsBomba = []

        self.lalistadepowerUpsVida = []
        self.lalistaderectspowerUpsVida = []

        self.explosiones = []
        self.rectsExplosiones = []

        self.listarandom = [0, 1, 2, 3, 4, 5]

    def placeEnemies(self):
        self.enemigos.append(enemy.Enemy([39, 259],"vertical"))
        self.enemigos.append(enemy.Enemy([111, 187],"horizontal"))
        self.enemigos.append(enemy.Enemy([187, 40],"vertical"))
        self.enemigos.append(enemy.Enemy([185, 335],"horizontal"))
        self.enemigos.append(enemy.Enemy([484, 37],"horizontal"))
        self.enemigos.append(enemy.Enemy([407, 148],"vertical"))
        self.enemigos.append(enemy.Enemy([484, 400],"vertical"))
        self.enemigos.append(enemy.Enemy([632, 400],"vertical"))
        self.enemigos.append(enemy.Enemy([669, 487],"horizontal"))
        self.enemigos.append(enemy.Enemy([780, 333],"vertical"))
        self.enemigos.append(enemy.Enemy([777, 260],"horizontal"))
        self.enemigos.append(enemy.Enemy([851, 400],"vertical"))

    def createBackground(self):
        pass

    def createWall(position, sprite):
        self.wall.setPosition(position)
        self.wall.setSprite(sprite)

    def createBoxes(self):
        # Creo la primera columna
        for i in range(1,14):
            if i == 5 or i ==9 or i ==10 or i ==11:
                self.lalistadecajas.append(obstacles.Obstacle(37, i * 37))
            else:
                pass  
        # Creo la segunda columna
        for i in range(1,14):
            if i == 3 or i ==5 or i ==7 or i ==9 or i ==11:
                self.lalistadecajas.append(obstacles.Obstacle(74, i * 37))
            else:
                pass  
        # Creo la tercera columna
        for i in range(1,14):
            if i == 1 or i ==4 or i ==6 or i ==7 or i ==10 or i ==11 or i==13:
                self.lalistadecajas.append(obstacles.Obstacle(111, i * 37))
            else:
                pass  
        # Creo la quinta columna
        for i in range(1,14):
            if i == 4 or i ==6 or i ==8 or i ==10 or i ==12:
                self.lalistadecajas.append(obstacles.Obstacle(185, i * 37))
            else:
                pass  
        # Creo la sexta columna
        for i in range(1,14):
            if i == 1 or i == 9:
                self.lalistadecajas.append(obstacles.Obstacle(222, i * 37))
            else:
                pass
        # Creo la septima columna
        for i in range(1,14):
            if i == 1 or i == 3 or i == 4 or i == 5 or i ==10 or i ==11 or i ==13:
                self.lalistadecajas.append(obstacles.Obstacle(259, i * 37))
            else:
                pass
        # Creo la novena columna
        for i in range(1,14):
            if i == 2 or i == 3 or i == 4 or i == 10:
                self.lalistadecajas.append(obstacles.Obstacle(333, i * 37))
            else:
                pass
        # Creo la decima columna
        for i in range(1,14):
            if i == 3:
                self.lalistadecajas.append(obstacles.Obstacle(370, i * 37))
            else:
                pass
        # Creo la onceava columna
        for i in range(1,14):
            if i == 2 or i == 5 or i == 10:
                self.lalistadecajas.append(obstacles.Obstacle(407, i * 37))
            else:
                pass
        # Doceava
        for i in range(1,14):
            if i == 3 or i == 5 or i == 7 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(444, i * 37))
            else:
                pass
        # 13
        for i in range(1,14):
            if i == 2 or i == 13:
                self.lalistadecajas.append(obstacles.Obstacle(481, i * 37))
            else:
                pass
        # 14
        for i in range(1,14):
            if i== 1 or i == 3 or i == 5 or i == 7 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(518, i * 37))
            else:
                pass
        # 15
        for i in range(1,14):
            if i== 1 or i == 2 or i == 4:
                self.lalistadecajas.append(obstacles.Obstacle(555, i * 37))
            else:
                pass
       # 16
        for i in range(1,14):
            if i== 1 or i == 7 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(592, i * 37))
            else:
                pass
        # 17
        for i in range(1,14):
            if i== 1 or i == 2 or i == 4 or i == 6 or i == 7 or i == 13:
                self.lalistadecajas.append(obstacles.Obstacle(629, i * 37))
            else:
                pass
               # 18
        for i in range(1,14):
            if i== 1 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(666, i * 37))
            else:
                pass
               # 18
        for i in range(1,14):
            if i== 1 or i == 2 or i == 3 or i == 6 or i == 8 or i == 9 or i == 10 or i == 12:
                self.lalistadecajas.append(obstacles.Obstacle(703, i * 37))
            else:
                pass
        for i in range(1,14):
            if i== 1 or i == 3 or i == 9:
                self.lalistadecajas.append(obstacles.Obstacle(740, i * 37))
            else:
                pass
        for i in range(1,14):
            if i== 1 or i == 2 or i == 3 or i == 6 or i == 8 or i == 12:
                self.lalistadecajas.append(obstacles.Obstacle(777, i * 37))
            else:
                pass
        for i in range(1,14):
            if i== 1 or i == 3 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(814, i * 37))
            else:
                pass
        for i in range(1,14):
            if i== 1 or i == 2 or i == 3 or i == 7 or i == 7 or i == 13:
                self.lalistadecajas.append(obstacles.Obstacle(851, i * 37))
            else:
                pass
        
    def poner_bomba(self, id):
        id_bomba = id

        print('La posicion del bomberman es: ' + str(self.getBombermanPosition()))
        
        pos =  self.obtenerPosicionCentrada(self.getBombermanPosition())
        

        
        self.bombas.append(bomba.Bomb(pos, id_bomba))

    def sacar_bomba(self, idbomba):
        for i in range(len(self.bombas)):
            for bomba in self.bombas:


                if bomba.getId() == idbomba:
                    self.bombas.remove(bomba)

    def getBombPos(self, id):
        for i in range (len(self.bombas)):
            if self.bombas[i].getId() == id:
                return self.bombas[i].getposicion()
        
        print("Id de la bomba no encontrado")

    def get_todas_las_bombas(self):
        return self.bombas                


# Crea a los enemigos que ya tienen una posicion pre establecida en el mapa
# al instanciarlos les pasa su posicion y como va a ser su movimiento pre
# establecido.

    def placeEnemies(self):
        self.enemigos.append(enemy.Enemy([39, 259],
                                                  "vertical", "vertical1"))
        self.enemigos.append(enemy.Enemy([111, 187],
                                                  "horizontal", "horizontal1"))
        self.enemigos.append(enemy.Enemy([187, 40],
                                                  "vertical", "vertical1"))
        self.enemigos.append(enemy.Enemy([185, 335],
                                                  "horizontal", "horizontal1"))
        self.enemigos.append(enemy.Enemy([484, 37],
                                                  "horizontal", "horizontal1"))
        self.enemigos.append(enemy.Enemy([407, 148],
                                                  "vertical", "vertical1"))
        self.enemigos.append(enemy.Enemy([484, 400],
                                                  "vertical", "vertical1"))
        self.enemigos.append(enemy.Enemy([632, 400],
                                                  "vertical", "vertical1"))
        self.enemigos.append(enemy.Enemy([669, 487],
                                                  "horizontal", "horizontal1"))
        self.enemigos.append(enemy.Enemy([780, 333],
                                                  "vertical", "vertical1"))
        self.enemigos.append(enemy.Enemy([777, 260],
                                                  "horizontal", "horizontal1"))
        self.enemigos.append(enemy.Enemy([851, 400],
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
        for enemy in self.enemigos:
            self.lalistaderectsenemigos.append(enemy.getEnemyRect())
        for cajas in self.lalistadecajas:
            self.lalistaderectscajas.append(cajas.getObstacleRect())

    def createEnemiesRects(self):
        for enemy in self.enemigos:
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

    def getDireccionEnemigo(self, enemigo):
        enemigodeseado = self.enemigos[enemigo]
        return enemigodeseado.getEnemyDireccion()

    def getPlayerHitbox(self):
        return self.player.getPlayerHitbox()

    def getBombermanVidas(self):
        return self.player.lifes

# Setters
    def setBombermanPosition(self):
        self.player.setBombermanPosition()

    def setBombermanPosicionDeInicio(self):
        self.player.setPosition([40, 40])

    def setPositionAnterior(self, enemigodeseado):
        enemy = self.enemigos[enemigodeseado]
        enemy.setPosition(enemy.getEnemyPosicionAnterior())

    def setDireccionEnemigo(self, direccion, enemigo):
        enemigodeseado = self.enemigos[enemigo]
        
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
        for enemy in self.enemigos:
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

    def setAnimacionEnemigo(self, i):
        enemigo = self.enemigos[i]
        
        if enemigo.getAnimacion() == "vertical1":
            enemigo.setAnimacion("vertical2")
        elif enemigo.getAnimacion() == "horizontal1":
            enemigo.setAnimacion("horizontal2")
        elif enemigo.getAnimacion() == "horizontal2":
            enemigo.setAnimacion("horizontal1")
        elif enemigo.getAnimacion() == "vertical2":
            enemigo.setAnimacion("vertical1")

# COLISIONES
# Getters de listas de objetos

    def getListaDeObstaculos(self):
        return self.LaListaDeObstaculos

    def getListaDeCajas(self):
        return self.lalistadecajas

    def getListaDeEnemigos(self):
        return self.enemigos

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
# Bombas
   
    def addExplosion(self, explosion):
        # Explosiones es pos, id bomba

        
        self.explosiones.append(explosion)



    def borrarExplosion(self, id):
        for i in range(0, len(self.explosiones)):
            if self.explosiones[i][1] == id:
                self.explosiones.pop(i)

    def get_todas_las_bombas(self):
        return self.bombas
    
    def getExplosiones(self):
        return self.explosiones
    
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
        self.enemigos.clear()
        self.lalistaderectsenemigos.clear()

# Getters

    def getCajaRota(self):  # Devuelvo la posicion de la caja que se rompio que previamente guarde en rompercaja
        return self.posicioncajarota

    def getListaRandom(self):  # Esto lo uso para randomizar la aparicion de determinados PowerUps
        shuffle(self.listarandom)
        return self.listarandom[0]
    
# Auxiliares

    def obtenerPosicionCentrada(self, pos):

        celda = 37

        celdaX = round(pos[0] / celda) 
        celdaY = round(pos[1] / celda)

        aux = [0,0]

        aux[0] = celdaX * celda
        aux[1] = celdaY * celda

        print('La posicion centrada es: ' + str(aux))
        return aux