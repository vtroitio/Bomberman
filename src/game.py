import pygame
import wall
import box
import player
import obstacles
import player
import enemy
import copy
import bomba
from explosion import Explosion
from random import shuffle
import random
import speed
import LifeUp
import bombUp


class Game():

    def __init__(self):
        self.paused = False
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

        self.lalistadepowerUpsSpeed = pygame.sprite.Group()
        self.lalistaderectspowerUpsSpeed = []

        self.lalistadepowerUpsBomba = pygame.sprite.Group()
        self.lalistaderectspowerUpsBomba = []

        self.lalistadepowerUpsVida = pygame.sprite.Group()
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

    def placeEnemies(self, diccionarioObstaculos, probabilidadEnemigos):

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
                    numeroSeleccionado = random.randrange(1, probabilidadEnemigos, 1)



                    if numeroSeleccionado <= 2:
                        posicionEnemigo = [int(columna) * sizeBloque, fila * sizeBloque]
                        tipoDeMovimiento = self.determinarMovimientoEnemigo(int(columna), int(fila), diccionarioDisponibles)
                        
                        if tipoDeMovimiento is not None:
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
        
        self.rectBombas.pop(0)

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

# Cuando se rompa una caja se va a llamar(dependiendo del numero que salga a
# la creacion de alguno de estos powerups que luego seran bliteados por la 
# vista.

    def createPowerUpSpeedUp(self, powerUp, rect):
        self.lalistadepowerUpsSpeed.add(powerUp)
        self.lalistaderectspowerUpsSpeed.append(rect)

    def createPowerUpVida(self, powerUp, rect):
        self.lalistadepowerUpsVida.add(powerUp)
        self.lalistaderectspowerUpsVida.append(rect)

    def createPowerUpBombUp(self, powerUp, rect):
        self.lalistadepowerUpsBomba.add(powerUp)
        self.lalistaderectspowerUpsBomba.append(rect)


# Crea los obstaculos no rompibles, los pilares grises, estos creandose segun
# las dimensiones que tenga la pantalla, idealmente para que los bloques queden
# bien situados, la altura y ancho de la pantalla de pygame deben ser multiplos
# de 37 ya que ese es el ancho y alto de nuestro bloque, de lo contrario no
# quedara una pantalla simetrica.

    def createObstacles(self, dimensions):
        WidthHeightObstacle = 37  # Tamaño del bloque utilizado

        # En self.bordes van a estar solamente los pilares grises, esto me va a servir
        # para que el movimiento diagonal no se active al colisionar con los mismos.

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

    def bombermanIsDead(self):
        return self.player.isDead()

    def getBombermanVidas(self):
        return self.player.lifes

# Setters
    
    def inicializarPosicionesEsquinas(self, pilaresPorColumna, pilaresPorFila):
        posicionesEsquinas = {"right": [], "left": [], "up": [], "down": []}

        tolerancia = 16
        
        startingPositionBloque = 46
        

        for i in range(0, pilaresPorColumna):

            
            finDeBloque = startingPositionBloque + 64

            tuplaRight = (startingPositionBloque, startingPositionBloque + tolerancia, "up")
            posicionesEsquinas["right"].append(tuplaRight)

            tuplaRight = (finDeBloque - tolerancia , finDeBloque, "down")
            posicionesEsquinas["right"].append(tuplaRight)


            tuplaLeft = (startingPositionBloque, startingPositionBloque + tolerancia, "up")
            posicionesEsquinas["left"].append(tuplaLeft)

            tuplaLeft = (finDeBloque - tolerancia , finDeBloque, "down")
            posicionesEsquinas["left"].append(tuplaLeft)
            
            startingPositionBloque = startingPositionBloque + 74



        startingPositionBloque = 46
        
        for i in range(0, pilaresPorFila):

            finDeBloque = startingPositionBloque + 64

            tuplaUp = (startingPositionBloque, startingPositionBloque + tolerancia, "left")
            posicionesEsquinas["up"].append(tuplaUp) 
            
            tuplaUp = (finDeBloque - tolerancia , finDeBloque, "right")
            posicionesEsquinas["up"].append(tuplaUp) 

            tuplaDown = (startingPositionBloque, startingPositionBloque + tolerancia, "left")
            posicionesEsquinas["down"].append(tuplaDown) 

            tuplaDown = (finDeBloque - tolerancia , finDeBloque, "right")
            posicionesEsquinas["down"].append(tuplaDown) 

            startingPositionBloque = startingPositionBloque + 74
        
                
        return posicionesEsquinas

    def setBombermanPosition(self, position, direccion, esPilar):

        
        self.player.setPosition(position)
        self.player.setBombermanDireccion(direccion)
        
        # Voy a verificar el choque con esquinas a partir de las dimensiones del mapa
        # Lo cual quiere decir que si se esta movimiendo a la derecha
        # en una determinada altura (en esa altura siempre va a estar colisionando
        # con una esquina) voy a hacer que se mueva diagonalmente. Lo ideal seria
        # que esta altura se calculara automaticamente tomando en cuenta
        # self.dimensions de gameEngine

        # posicionesEsquinas = {"right" : [(47,57, "up"), (97,107,"down")]}

        # Inicializo el diccionario

        
        if not esPilar:        
            if direccion == "right" and self.bombermanEntrePosiciones(self.posicionesEsquinas["right"], [1,0]):
                self.player.move(self.direccionDiagonal)
            elif direccion == "left" and self.bombermanEntrePosiciones(self.posicionesEsquinas["left"], [-1,0]):
                self.player.move(self.direccionDiagonal)
            elif direccion == "down" and self.bombermanEntrePosiciones(self.posicionesEsquinas["down"], [0,1]):
                self.player.move(self.direccionDiagonal)
            elif direccion == "up" and self.bombermanEntrePosiciones(self.posicionesEsquinas["up"], [0,-1]):
                self.player.move(self.direccionDiagonal)
        

    def setBombermanPosicionDeInicio(self):
        self.player.setPosition([37, 37])

    def setBombermanState(self):
        self.player.setState()
    
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

    def getRectsCercanosEnemy(self, enemy):
        
        offset = 8

        rectActual = enemy.getEnemyRect()

        rectDerecha = rectActual.move(offset, 0)
        rectIzquierda = rectActual.move(-offset, 0)
        rectArriba = rectActual.move(0, -offset)
        rectAbajo = rectActual.move(0, offset)

        return rectDerecha, rectIzquierda, rectArriba, rectAbajo

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

    def borrarPlayerHitbox(self):
        self.player.borrarHitbox()
    
    def borrarPowerUps(self):
        
        self.rectBombas.clear()
        self.bombas.clear()
        
        self.lalistadepowerUpsBomba.empty()
        self.lalistaderectspowerUpsBomba.clear()
        
        self.lalistadepowerUpsVida.empty()
        self.lalistaderectspowerUpsVida.clear()
        
        self.lalistadepowerUpsSpeed.empty()
        self.lalistaderectspowerUpsSpeed.clear()

        

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
    
    def getPlayerHitbox(self):
        return self.player.getPlayerHitbox()

    def getSpeedUpRect(self):
        return self.lalistaderectspowerUpsSpeed

    def getLifeUpRect(self):
        return self.lalistaderectspowerUpsVida

    def getBombUpRect(self):
        return self.lalistaderectspowerUpsBomba

# Setters de listas de rects

    def setPlayerRect(self, rect):
        self.player.setPlayerRect(rect)

    def setPlayerHitbox(self):
        self.player.setHitbox()

    def setlalistaderectsenemigos(self, cosa):
        self.lalistaderectsenemigos.append(cosa)

    def setLalistaDeRectsCajas(self, rect):
        self.lalistaderectscajas.append(rect)

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
   
    def addExplosion(self, pos, id_bomba, rects):
        # Explosiones es pos, id bomba
        explosion = Explosion(pos, id_bomba, rects)
        
        self.explosiones.append(explosion)

    def limpiarExplosiones(self):
        self.explosiones.clear()

    def borrarExplosion(self, id):
        for explosion in self.explosiones:
            if explosion.getId() == id:
                self.explosiones.pop(0)
        
        # if self.explosiones != []:
        #     if self.explosiones[0][1] == id:
        #         self.explosiones.pop(0)

    def get_todas_las_bombas(self):
        return self.bombas
    
    def getExplosiones(self):
        return self.explosiones
    
    def borrarSpeedUp(self, indice):
        if len(self.lalistaderectspowerUpsSpeed) > 0 and len(self.lalistadepowerUpsSpeed) > 0:

            self.lalistadepowerUpsSpeed.pop(indice)
            self.lalistaderectspowerUpsSpeed.pop(indice)

    def borrarBombUp(self, indice):
        if len(self.lalistaderectspowerUpsBomba) > 0 and len(self.lalistadepowerUpsBomba) > 0:

            self.lalistadepowerUpsBomba.pop(indice)
            self.lalistaderectspowerUpsBomba.pop(indice)

    def borrarLifeUp(self, indice):
        if len(self.lalistaderectspowerUpsVida) > 0 and len(self.lalistadepowerUpsVida) > 0:
     
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
        playerRect = self.player.getPlayerRect()

        for life in self.lalistadepowerUpsVida:
            lifeRect = life.getWorldRect()
            if lifeRect.colliderect(playerRect):
                life.kill()
                return True

        return False

    def agarroBomba(self):
        playerRect = self.player.getPlayerRect()

        for bomb in self.lalistadepowerUpsBomba:
            bombRect = bomb.getWorldRect()
            if bombRect.colliderect(playerRect):
                bomb.kill()
                return True

        return False

    def agarroVelocidad(self):
        playerRect = self.player.getPlayerRect()

        for velocity in self.lalistadepowerUpsSpeed:
            velocityRect = velocity.getWorldRect()
            if velocityRect.colliderect(playerRect):
                velocity.kill()
                return True

        return False
    
    def pause(self):
        self.paused = not self.paused
    
    def isPaused(self):
        return self.paused