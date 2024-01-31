import wall
import box
import player
import obstacles
import player
import enemy
import copy
import bomba
from random import shuffle
import random
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
        self.rectBombas = []
        
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

        self.listarandom = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10 , 11, 12, 13, 14, 15]

        self.salida = None
        self.salidaRect = None
        self.cajaConSalida = None

        self.posicionesEsquinas = self.inicializarPosicionesEsquinas(6, 11)
        self.direccionDiagonal = None
        self.bordes = []
        self.rectBordes = []
        


    def crearSalida(self):
        
        maxInt = len(self.lalistadecajas) - 1
        indiceElegido = random.randint(0, maxInt)
        
        cajaSeleccionada = self.lalistadecajas[indiceElegido]
        self.cajaConSalida = cajaSeleccionada

        x, y = cajaSeleccionada.getPosition()
        
        self.salida = obstacles.Obstacle(x, y)

    def getSalidaRect(self):
        return self.salidaRect

    def getSalida(self):
        return self.salida

    def placeEnemies(self, diccionarioObstaculos):

        # Recorro el diccionario de obstaculos y pongo los enemigos si esta vacia
        # de manera aleatoria
        
        sizeBloque = 37.3
        cantFilasMax = 13
        cantColumnas = 23

        diccionarioDisponibles = {}

        # Inicializo el diccionario de disponibles

        for i in range(1, cantColumnas):
            diccionarioDisponibles[str(i)] = []

            
        # Populo el diccionario de disponibles

        for columna in diccionarioObstaculos:
            
            posicionesDisponibles = []
            posicionesOcupadas = diccionarioObstaculos[columna]

            for i in range(1, cantFilasMax):
                if i in posicionesOcupadas:
                    pass
                else:
                    posicionesDisponibles.append(i)
            
            diccionarioDisponibles[str(columna)] = posicionesDisponibles


        # Ahora pongo los enemigos en las posiciones disponibles, siempre
        # y cuando no sea (par, par) y siempre y cuando no sean los bordes del juego

        # Es importante prohibir que pongan enemigos donde aparece el 
        # bomberman, estos serian 1: [1,2], 2:[1], tambien los bordes de la
        # pantalla
        
        posicionesProhibidas = {'0':[0,1,2,3,4,5,6,7,8,9,10,11,12,13],
                                '1': [1,2],
                                '2': [1],
                                '24': [0,1,2,3,4,5,6,7,8,9,10,11,12,13]}

        for columna in diccionarioDisponibles:

            posicionesDisponibles = diccionarioDisponibles[columna]


            for fila in posicionesDisponibles:
                
                if columna in posicionesProhibidas and fila in posicionesProhibidas[columna]:
                    pass    
                elif fila % 2 == 0 and int(columna) % 2 == 0:
                    pass
                else:
                    numeroSeleccionado = random.randrange(1, 13, 1)



                    if numeroSeleccionado <= 2:
                        posicionEnemigo = [int(columna) * sizeBloque, fila * sizeBloque]
                        tipoDeMovimiento = self.determinarMovimientoEnemigo(int(columna), int(fila), diccionarioDisponibles)
                        self.enemigos.append(enemy.Enemy(posicionEnemigo, tipoDeMovimiento[0], tipoDeMovimiento[1]))




    def bombermanEntrePosiciones(self, rangoDePosiciones, direccion):

        for i in range(0, len(rangoDePosiciones)):
            
            if direccion == [0,1] or direccion == [0,-1]:
                axisBomberman = self.getBombermanPosition()[0]
                indice = 0
            else:
                axisBomberman = self.getBombermanPosition()[1]
                indice = 1
            
            # Si el bomberman se encuentra en determinada altura
            if axisBomberman >= rangoDePosiciones[i][0] and axisBomberman <= rangoDePosiciones[i][1]:
                print("En esquina")
                
                
                if i % 2 == 0:
                    #Arriba
                    direccion[indice] = -1
                    self.direccionDiagonal = direccion
                else:
                    #Abajo 
                    direccion[indice] = 1
                    self.direccionDiagonal = direccion
                
                return True
        

        return False

    def determinarMovimientoEnemigo(self, columna, fila, diccionarioDisponibles):
        # Tengo que verificar para donde se puede mover el enemigo

        # Verifico si misma columna y fila de arriba esta libre
       
        filaArriba = fila - 1
        filaAbajo = fila + 1

        columnaIzquierda = columna - 1
        columnaDerecha = columna + 1

        if fila in diccionarioDisponibles[str(columnaDerecha)]:
            return ("horizontal", "horizontal1")
        if fila in diccionarioDisponibles[str(columnaIzquierda)]:
            return ("horizontal", "horizontal1")
        
        if filaArriba in diccionarioDisponibles[str(columna)]:
            return ("vertical", "vertical1")
        if filaAbajo in diccionarioDisponibles[str(columna)]:
            return ("vertical", "vertical1")





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

        
        pos =  self.obtenerPosicionCentrada(self.getBombermanPosition())
        bomb = bomba.Bomb(pos, id_bomba)
        
        self.bombas.append(bomb)

        return bomb

    def getBombRects(self):
        return self.rectBombas

    def addBombRect(self, rect):
        self.rectBombas.append(rect)

    def sacar_bomba(self, idbomba):

        for bomba in self.bombas:

            if bomba.getId() == idbomba:
                self.bombas.remove(bomba)
        
        self.rectBombas.pop()

    def getBombPos(self, id):
        
        # print("Quiero obtener la pos de la bomba con id: " + str(id))
        
        # for i in range(len(self.bombas)):
        #     print("Bomba id = " + str(self.bombas[i].getId()))
        
        for i in range (len(self.bombas)):
            if self.bombas[i].getId() == id:
                return self.bombas[i].getposicion()
        
        print("Id de la bomba no encontrado")

    def get_todas_las_bombas(self):
        return self.bombas                


# Crea a los enemigos que ya tienen una posicion pre establecida en el mapa
# al instanciarlos les pasa su posicion y como va a ser su movimiento pre
# establecido.

    # def placeEnemies(self):
    #     self.enemigos.append(enemy.Enemy([39, 259],
    #                                               "vertical", "vertical1"))
    #     self.enemigos.append(enemy.Enemy([111, 187],
    #                                               "horizontal", "horizontal1"))
    #     self.enemigos.append(enemy.Enemy([187, 40],
    #                                               "vertical", "vertical1"))
    #     self.enemigos.append(enemy.Enemy([185, 335],
    #                                               "horizontal", "horizontal1"))
    #     self.enemigos.append(enemy.Enemy([484, 37],
    #                                               "horizontal", "horizontal1"))
    #     self.enemigos.append(enemy.Enemy([407, 148],
    #                                               "vertical", "vertical1"))
    #     self.enemigos.append(enemy.Enemy([484, 400],
    #                                               "vertical", "vertical1"))
    #     self.enemigos.append(enemy.Enemy([632, 400],
    #                                               "vertical", "vertical1"))
    #     self.enemigos.append(enemy.Enemy([669, 487],
    #                                               "horizontal", "horizontal1"))
    #     self.enemigos.append(enemy.Enemy([780, 333],
    #                                               "vertical", "vertical1"))
    #     self.enemigos.append(enemy.Enemy([777, 260],
    #                                               "horizontal", "horizontal1"))
    #     self.enemigos.append(enemy.Enemy([851, 400],
    #                                               "vertical", "vertical1"))

# Cuando se rompa una caja se va a llamar(dependiendo del numero que salga a
# la creacion de alguno de estos powerups que luego seran bliteados por la 
# vista.

    def createPowerUpSpeedUp(self, posicion, rect):
        self.lalistadepowerUpsSpeed.append(speed.Speed(posicion))
        self.lalistaderectspowerUpsSpeed.append(rect)

    def createPowerUpVida(self, posicion, rect):
        self.lalistadepowerUpsVida.append(LifeUp.LifeUp(posicion))
        self.lalistaderectspowerUpsVida.append(rect)

    def createPowerUpBombUp(self, posicion, rect):
        self.lalistadepowerUpsBomba.append(bombUp.BombUp(posicion))
        self.lalistaderectspowerUpsBomba.append(rect)


# Crea los obstaculos no rompibles, los pilares grises, estos creandose segun
# las dimensiones que tenga la pantalla, idealmente para que los bloques queden
# bien situados, la altura y ancho de la pantalla de pygame deben ser multiplos
# de 37 ya que ese es el ancho y alto de nuestro bloque, de lo contrario no
# quedara una pantalla simetrica.

    def createObstacles(self, dimensions):
        WidthHeightObstacle = 37  # Tamaño del bloque utilizado

        for i in range(0, int((dimensions[0] / WidthHeightObstacle)) + 1):  # De 0 a 26
            bloqueArriba = obstacles.Obstacle(i * WidthHeightObstacle, 0)
            self.LaListaDeObstaculos.append(bloqueArriba)  # Creo los bloques de la fila de arriba
            self.bordes.append(bloqueArriba)
            
            bloqueAbajo = obstacles.Obstacle(i * WidthHeightObstacle, dimensions[1] - WidthHeightObstacle)
            self.LaListaDeObstaculos.append(bloqueAbajo)  # Creo los bloques de la fila de abajo
            self.bordes.append(bloqueAbajo)

        for i in range(0, int((dimensions[1] / WidthHeightObstacle)) + 1):  # De 0 a 16
            
            bloqueIzquierda = obstacles.Obstacle(0, i * WidthHeightObstacle)
            self.LaListaDeObstaculos.append(bloqueIzquierda)  # Creo los bloques de las columnas de la izquierda
            self.bordes.append(bloqueIzquierda)

            bloqueDerecha = obstacles.Obstacle(dimensions[0] - WidthHeightObstacle, i * WidthHeightObstacle)
            self.LaListaDeObstaculos.append(bloqueDerecha)  # Creo los bloques de las columnas de la derecha
            self.bordes.append(bloqueDerecha)

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
        for obstaculo in self.bordes:
            self.rectBordes.append(obstaculo.getObstacleRect())

    def createEnemiesRects(self):
        for enemy in self.enemigos:
            self.lalistaderectsenemigos.append(enemy.getEnemyRect())

    def createBoxesRects(self):
        for cajas in self.lalistadecajas:
            self.lalistaderectscajas.append(cajas.getObstacleRect())

# MOVIMIENTO

    def givePosition(self, position):
        self.player.move(position)
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
    
    def inicializarPosicionesEsquinas(self, pilaresPorColumna, pilaresPorFila):
        posicionesEsquinas = {"right": [], "left": [], "up": [], "down": []}

        startingPosition = 47


        for i in range(0, pilaresPorColumna):

            
            offsetEsquinas = 50

            tuplaRight = (startingPosition, startingPosition + 10, "up")
            posicionesEsquinas["right"].append(tuplaRight)

            tuplaRight = (startingPosition + offsetEsquinas, startingPosition + offsetEsquinas + 10, "down")
            posicionesEsquinas["right"].append(tuplaRight)


            tuplaLeft = (startingPosition, startingPosition + 10, "up")
            posicionesEsquinas["left"].append(tuplaLeft)

            tuplaLeft = (startingPosition + offsetEsquinas, startingPosition + offsetEsquinas + 10, "down")
            posicionesEsquinas["left"].append(tuplaLeft)
            
            startingPosition = startingPosition + 75



        startingPosition = 47
        
        for i in range(0, pilaresPorFila):

            offsetEsquinas = 50

            tuplaUp = (startingPosition, startingPosition + 10, "left")
            posicionesEsquinas["up"].append(tuplaUp) 
            
            tuplaUp = (startingPosition + offsetEsquinas, startingPosition + offsetEsquinas + 10, "right")
            posicionesEsquinas["up"].append(tuplaUp) 

            tuplaDown = (startingPosition, startingPosition + 10, "left")
            posicionesEsquinas["down"].append(tuplaDown) 

            tuplaDown = (startingPosition + offsetEsquinas, startingPosition + offsetEsquinas + 10, "right")
            posicionesEsquinas["down"].append(tuplaDown) 

            startingPosition = startingPosition + 75
        
                
        return posicionesEsquinas

    def setBombermanPosition(self, direccion, esBorde):
        

        self.player.setBombermanDireccion(direccion)
        
        # Voy a verificar el choque con esquinas a partir de las dimensiones del mapa
        # Lo cual quiere decir que si se esta movimiendo a la derecha
        # en una determinada altura (en esa altura siempre va a estar colisionando
        # con una esquina) voy a hacer que se mueva diagonalmente. Lo ideal seria
        # que esta altura se calculara automaticamente tomando en cuenta
        # self.dimensions de gameEngine

        # posicionesEsquinas = {"right" : [(47,57, "up"), (97,107,"down")]}

        # Inicializo el diccionario

        
        if not esBorde:        
        
            if direccion == "right" and self.bombermanEntrePosiciones(self.posicionesEsquinas["right"], [1,0]):
                self.player.move(self.direccionDiagonal)
            elif direccion == "left" and self.bombermanEntrePosiciones(self.posicionesEsquinas["right"], [-1,0]):
                self.player.move(self.direccionDiagonal)
            elif direccion == "down" and self.bombermanEntrePosiciones(self.posicionesEsquinas["down"], [0,1]):
                self.player.move(self.direccionDiagonal)
        
        # Si la direccion es derecha o izquierda el moviemnto puede ser abajo o arriba
        

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

    def getRectsBordes(self):
        return self.rectBordes

    def getBordes(self):
        return self.bordes
    
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

    def borrarPowerUps(self):
        self.lalistadepowerUpsBomba = []
        self.lalistadepowerUpsVida = []
        self.lalistadepowerUpsSpeed = [] 
        self.bombas = []

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

    # def setRectSpeedUp(self, rect):
    #     self.speed

    # def setRectBombUp(self, rect):
    #     self.lalistaderectspowerUpsBomba.append(rect)

    # def setRectLifeUp(self, rect):
    #     self.lalistaderectspowerUpsVida.append(rect)

# Borrar Rects y Sprites

    def romperCaja(self, numerodecaja):
        caja = self.lalistadecajas[numerodecaja]
        
        # Asigno el rect de la salida al momento de romper la caja para evitar un colision
        # sin que la caja este rota

        if caja == self.cajaConSalida:
            self.salidaRect = self.lalistaderectscajas[numerodecaja]
        
        self.posicioncajarota = caja.getPosition()
        
        self.lalistadecajas.pop(numerodecaja)
        self.lalistaderectscajas.pop(numerodecaja)
# Bombas
   
    def addExplosion(self, explosion):
        # Explosiones es pos, id bomba

        
        self.explosiones.append(explosion)



    def borrarExplosion(self, id):
        if self.explosiones[0][1] == id:
            self.explosiones.pop(0)

    def get_todas_las_bombas(self):
        return self.bombas
    
    def getExplosiones(self):
        return self.explosiones
    
    def borrarSpeedUp(self, indice):
        print(str(self.lalistaderectspowerUpsSpeed) + " y no rects: " + str(self.lalistadepowerUpsSpeed))
        
        if len(self.lalistaderectspowerUpsSpeed) > 0 and len(self.lalistadepowerUpsSpeed) > 0:
            print("Borro el powerUp")
            self.lalistadepowerUpsSpeed.pop(indice)
            self.lalistaderectspowerUpsSpeed.pop(indice)

    def borrarBombUp(self, indice):
        print(str(self.lalistaderectspowerUpsBomba) + " y no rects: " + str(self.lalistadepowerUpsBomba))
        if len(self.lalistaderectspowerUpsBomba) > 0 and len(self.lalistadepowerUpsBomba) > 0:
            print("Borro el powerUp")
            self.lalistadepowerUpsBomba.pop(indice)
            self.lalistaderectspowerUpsBomba.pop(indice)

    def borrarLifeUp(self, indice):
        print(str(self.lalistaderectspowerUpsVida) + " y no rects: " + str(self.lalistadepowerUpsVida))
        if len(self.lalistaderectspowerUpsVida) > 0 and len(self.lalistadepowerUpsVida) > 0:
            print("Borro el powerUp")
            self.lalistadepowerUpsVida.pop(indice)
            self.lalistaderectspowerUpsVida.pop(indice)

    def borrarDatosCajas(self):
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
    
    def getBombas(self):
        return self.bombas
    
# Auxiliares
    def obtenerPosicionCentrada(self, pos):
        celda = 37

        celdaX = round(pos[0] / celda) 
        celdaY = round(pos[1] / celda)

        aux = [0,0]

        aux[0] = celdaX * celda
        aux[1] = celdaY * celda


        return aux
    
    def borrarEnemigo(self, indice):
        self.enemigos.pop(indice)
        self.lalistaderectsenemigos.pop(indice)
        # self.positionAnteriorEnemy.pop(indice)

    def agarroVida(self):

        agarroVida = False
        playerRect = self.player.getPlayerRect()
        powerLifeRects = self.lalistaderectspowerUpsVida

        if len(powerLifeRects) > 0:
            if (playerRect.collidelist(powerLifeRects)) > -1:
                
                agarroVida = True
                self.lalistadepowerUpsVida.pop(playerRect.collidelist(powerLifeRects))
                self.lalistaderectspowerUpsVida.pop(playerRect.collidelist(powerLifeRects))

        return agarroVida

    def agarroBomba(self):
        
        agarroBomba = False
        playerRect = self.player.getPlayerRect()
        powerBombRects = self.lalistaderectspowerUpsBomba

        if len(powerBombRects) > 0:
            if (playerRect.collidelist(powerBombRects)) > -1:
                
                agarroBomba = True
                self.lalistadepowerUpsBomba.pop(playerRect.collidelist(powerBombRects))
                self.lalistaderectspowerUpsBomba.pop(playerRect.collidelist(powerBombRects))

        return agarroBomba

    def agarroVelocidad(self):
        
        agarroVelocidad = False
        playerRect = self.player.getPlayerRect()
        powerSpeedRects = self.lalistaderectspowerUpsSpeed

        if len(powerSpeedRects) > 0:
            if (playerRect.collidelist(powerSpeedRects)) > -1:
                
                agarroVelocidad = True
                self.lalistadepowerUpsSpeed.pop(playerRect.collidelist(powerSpeedRects))
                self.lalistaderectspowerUpsSpeed.pop(playerRect.collidelist(powerSpeedRects))

        return agarroVelocidad