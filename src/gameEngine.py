import pygame
import game
import background
import sys
import time
from threading import Thread
from pydispatch import dispatcher
import math
import random


# Son las flechitas, se usan para el movimiento del bomberman

CONTROLES = {'1073741906': [0, -1], '1073741905': [0, 1], '1073741903': [1, 0], '1073741904': [-1, 0]}


# Uso los threads principalmente para poder ejecutar eventos luego de un tiempo gracias al sleep

class threadPowerUp(Thread):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo

    def run(self):
        # Este thread determina cuanto tiempo pasa hasta que se borra un powerUP
        time.sleep(6)
        dispatcher.send(message = self.tipo, signal= 'borrarPowerUp', sender = 'threadPowerUp')


class threadExplosion(Thread):
    def __init__(self, explosion):
        super().__init__()
        self.explosion = explosion

    def run(self):
        # Este thread determina cuanto tiempo pasa en pantalla el sprite de la explosion
        time.sleep(0.3)
        dispatcher.send(message = self.explosion, signal= 'borrarExplosion', sender = 'threadExplosion')
        
        
class threadBomba(Thread):
    def __init__(self, idbomba, game):
        super().__init__()
        self.id = idbomba
        self.game = game

    def run(self):
        # Este thread determina cuanto tiempo pasa hasta que explota la bomba
        time.sleep(3.0)
        if(self.game.getBombas() != []):
            dispatcher.send(message = self.id, signal= 'explotoBomba', sender = 'threadBomba')

class threadSpeed(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        # Este thread determina cuanto tiempo pasa hasta que te quedas sin velocidad
        time.sleep(10)
        print("Ya no corres rapido :( ")
        dispatcher.send(message = '', signal= 'resetearSpeed', sender = 'threadSpeed')



class GameEngine():
    def __init__(self):
        self.dimensions = [925, 555]
        self.game = game.Game()
        self.background = background.Background(self.dimensions, self.game)
        
        self.loadImages()

        # Cuanto mayor sea el numero, menos probabilidad
        # Si es < 6 en obstaculos pone obstaculo en todos lados
        # Si es < 2 en enemigos pone enemigos en todos lados
        # La probabilidad default es 13 en ambos 

        self.probabilidadObstaculos = 13
        self.probabilidadEnemigos = 13
        
        self.diccionarioposicionesobstaculo = None
        
        
        self.game.createObstacles(self.dimensions)   # Creo los pilares y los bordes (solo hace falta crearlos una vez -> no van a estar en crearNivel() )
        self.background.reloadBackground() # Les asigno su rect a los pilares

        self.crearNivel()
        
        # Variables que uso para saber que pantalla mostrar

        self.menu = True
        self.gameOverScreen = False
        self.winScreen = False
        self.nivelActual = 1

        # Variables para el uso de bombas (deberia delegarlas a game y mejorar esto)

        self.lista_threads = []
        self.BOMBAS_USANDO = []
        self.BOMBAS_DISPONIBLES = [1]
        self.bombas = 1
        self.byPassRectBomba = None

        self.mainLoop()

    def crearNivel(self):
        # Genero aleatoriamente la posicion de las cajas y lo guardo en un diccionario
        diccCajas = self.generateRandomObstacles(self.probabilidadObstaculos)
        
        # Una vez tengo el diccionario creo las cajas rompibles
        self.crearCajasRompibles(diccCajas)
        self.background.reloadBoxes() # Le asigno a cada una su rect
        
        # Una vez creadas las cajas puedo empezar a ubicar a los enemigos
        self.game.placeEnemies(diccCajas, self.probabilidadEnemigos)
        self.background.reloadEnemyRect() # Le asigno a cada uno su rect
        
        # Vuelvo a ubicar la salida
        self.game.crearSalida()

        # Guardo cada grupo de rects (ya creados en el reload) en su respectiva lista
        # El rect de la salida se crea recien cuando se rompe la caja que esconde la misma
        self.game.createRects()

    def limpiarNivelActual(self):
        # Este reload lo hago para dar un efecto visual de "reset"
        self.background.reloadBackgroundImage()

        # Muevo al bomberman al comienzo del mapa y reestablezco los power-ups
        self.game.setBombermanPosicionDeInicio()
        self.game.setBombermanSpeed(5)

        self.BOMBAS_USANDO = []
        self.BOMBAS_DISPONIBLES = [1]
        self.bombas = 1

        self.game.borrarPowerUps()
        self.game.borrarDatosCajas()
        self.game.borrarDatosEnemigos()
    
    def siguienteNivel(self):
        self.nivelActual += 1
        self.limpiarNivelActual()
        self.crearNivel()
        print("Pasaste al siguiente nivel :D, estas en el nivel " + str(self.nivelActual))

    def intro(self):
        clock = pygame.time.Clock()
        while self.menu:
            self.background.reloadMenu()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYUP:
                    self.menu = False
                    pygame.display.update()
                    clock.tick(60)
        
    def generateRandomObstacles(self, probabilidadObstaculos):
        
        diccionarioPilares = {}
        diccionarioObstaculos = {}

        # 23 Columnas, en las impares no hay ningun bloque

        sizeBloque = 37

        # Ancho x Altura

        ancho = self.dimensions[0]
        altura = self.dimensions[1]

        # Casteo a int ambos numeros
        cantColumnas = math.floor(ancho / sizeBloque)
        cantFilas = math.floor(altura / sizeBloque)

        
        # Populo el diccionario con la cantidad de columnas como clave
        # y como significado la lista vacia que luego voy a llenar

        for i in range(0, cantColumnas):
            diccionarioObstaculos[str(i)] = []

        for i in range(0, cantColumnas):
            diccionarioPilares[str(i)] = []
        
        # Si es (par, par) hay un bloque rompible,
        # esto quiere decir que si estoy en (2,2)
        # (2,4) (4,2) etc ahi no puedo poner un bloque rompible
        
        # Es importante prohibir que ponga bloques donde aparece el 
        # bomberman, estos serian 1: [1,2], 2:[1]
        
        posicionesProhibidas = {'1': [1,2],
                                '2': [1]}

        for i in range(0, cantColumnas):
            for j in range(1, cantFilas):

                # El rango va desde 1 ya que 0, serian
                # los bloques no rompibles
                if str(i) in posicionesProhibidas and j in posicionesProhibidas[str(i)]:
                    pass
                elif i % 2 == 0 and j % 2 == 0:
                    # Caso (par, par)
                    # diccionarioPilares[str(i)].append(j)
                    pass
                else:
                    # Caso puedo poner un bloque rompible
                    # Voy a poner un 60% de probabilidad que haya un bloque

                    numeroSeleccionado = random.randrange(1, probabilidadObstaculos, 1)

                    if numeroSeleccionado <= 6:
                        diccionarioObstaculos[str(i)].append(j)
        
        # print(str(diccionarioPilares))

        return diccionarioObstaculos
        
    def gameOver(self):
        clock = pygame.time.Clock()
        while self.gameOverScreen:
            self.background.reloadGameOverScreen()
            pygame.display.update()
            clock.tick(60)
            
    def win(self):
        clock = pygame.time.Clock()
        while self.winScreen:
            self.background.reloadWinScreen()
            pygame.display.update()
            clock.tick(60)


    def goMenu():
        pass

    def goOption():
        pass

    def exit():
        pass

    def killBomberman(self):

        self.game.setBombermanVidas(-1)
        vidasRestantes = self.game.getBombermanVidas()
        
        if vidasRestantes > 0:
            if vidasRestantes == 1:
                print("Todavia tenes " + str(vidasRestantes)+ " vida")
            else:
                print("Todavia tenes " + str(vidasRestantes)+ " vidas")
        elif vidasRestantes == 0:
            print("Tene cuidado, es tu ultima vida")
        else:
            print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ GAME OVER ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
            self.gameOverScreen = True        

        self.limpiarNivelActual()
        self.crearNivel()
        self.game.limpiarExplosiones()

        


    def loadImages(self):
        self.background.loadBombermanImage('sprites/BombermanAnimado/', (37, 37))  # Lo pone al principio del mapa
        self.background.loadObstacle("sprites/pilar.png")
        self.background.loadImagenMenu("sprites/MenuBomberman.png")
        self.background.loadBackgroundImage("sprites/pasto.png")
        self.background.loadEnemigoBomberman("sprites/EnemigoBombermanAnimado/")
        self.background.loadCaja("sprites/caja.png")
        self.background.loadBomba("sprites/Bomba.png")
        self.background.loadSpeedPowerUp("sprites/PowerUps/SpeedUp.png")
        self.background.loadGameOverScreen("sprites/GameOver.jpg")
        self.background.loadBombPowerUp("sprites/PowerUps/BombUp.png")
        self.background.loadLifePowerUp("sprites/PowerUps/HealthUp.png")
        self.background.loadExplosion("sprites/Explosion.png")
        self.background.loadSalida("sprites/Salida.png")
        self.background.loadWinScreen("sprites/victory.jpg")

    def resetearSpeed(self, message):
        self.game.setBombermanSpeed(5)

    def borrarPowerUp(self, message):
        
        # message es tupla = (tipoDePowerUp)


        if message == 'velocidad':
            self.game.borrarSpeedUp(0)
        elif message == 'bomba':
            self.game.borrarBombUp(0)
        elif message == 'vida':
            self.game.borrarLifeUp(0)
    
    
    def borrarExplosion(self, message):
        # A la hora de borrar la explosion tengo que verificar si el rect de la misma
        # rompio un bloque, mato un enemigo, o nos hiteo a nosotros.

        # message = [pos, idbomba, listaDeRectsExplosion]



        self.game.borrarExplosion(message[1])



    def exploto(self, message):
        id_bomba = message

        
        # Logica 
        if len(self.BOMBAS_USANDO) > 0:
            self.BOMBAS_USANDO.remove(id_bomba)
            
            x,y = self.game.getBombPos(id_bomba)
            offset = 1
            pos = [x , y + offset]
            
            self.BOMBAS_DISPONIBLES.append(id_bomba)
            self.game.sacar_bomba(id_bomba)    

        
        
        # Creo el rect para las colisiones
        ancho = 35
        alto = 35

        rects = []
        
        
        # 3 verticales
        for i in range(-1, 2):
            rects.append((pos[0] + (37 * i), pos[1], ancho, alto))
        
        # 3 Horizontales
        for i in range(-1, 2):
            rects.append((pos[0] , pos[1] + (37* i), ancho, alto))
        
        # Creo la explosion, el offset es para que quede centrado el png
        
        offset = 40
        pos[0] = pos[0] - offset
        pos[1] = pos[1] - offset
        
        self.game.addExplosion((pos, id_bomba, rects))


      
        rectsExplosion = []

        for rect in rects:
            rectsExplosion.append(pygame.Rect(rect[0], rect[1], rect[2], rect[3]))

        # Tengo que verificar las colisiones que tuvo la explosion
        # Ya sea con el bomberman, enemigos o bloques rompibles
        

        # Reviso colision de explosion con cajas rompibles
            
        for rect in rectsExplosion:
            
            if rect.collidelistall(self.game.getLaListaDeRectsCajas()):
            
                caja = rect.collidelistall(self.game.getLaListaDeRectsCajas())
                self.game.romperCaja(caja[0])
                
                numerorandom = self.game.getListaRandom()
                
                posCajaRota = self.game.getCajaRota()

                if numerorandom == 0:
                    self.game.createPowerUpSpeedUp(posCajaRota, pygame.Rect(posCajaRota[0], posCajaRota[1], ancho, alto))                             
                    threadVelocidad = threadPowerUp('velocidad')
                    threadVelocidad.start()
                elif numerorandom == 1:
                    self.game.createPowerUpBombUp(posCajaRota, pygame.Rect(posCajaRota[0], posCajaRota[1], ancho, alto))
                    threadBomba = threadPowerUp('bomba')
                    threadBomba.start()
                elif numerorandom == 2:
                    self.game.createPowerUpVida(posCajaRota, pygame.Rect(posCajaRota[0], posCajaRota[1], ancho, alto))
                    threadVida = threadPowerUp('vida')
                    threadVida.start()
                elif numerorandom > 0:
                    pass


        # Enemigos
                 
        enemiesRects = self.game.getEnemyRect()
        enemigosABorrar = []

        offsetPostPop = 0

        for i in range(0, len(enemiesRects)):
            if enemiesRects[i].collidelistall(rectsExplosion):
                # print("El indice del enemigo que colisiono es: " + str(i))

                indice = i - offsetPostPop
                enemigosABorrar.append(indice)
                offsetPostPop = offsetPostPop + 1
                


        
        for indice in enemigosABorrar:
            self.game.borrarEnemigo(indice)


        # Bomberman
            
        if self.game.getPlayerRect().collidelistall(rectsExplosion):
            self.killBomberman()


        


        thread = threadExplosion((pos, id_bomba, rects))
        thread.start()
 
        
    def crearCajasRompibles(self, diccCajas):
        Size = 37
        for z in range(1, 24):
            for i in range(1, 14):
                for x in range(0, len(diccCajas[str(z)])):
                    if diccCajas[str(z)][x] == i:
                        self.game.setLaListaDeCajas(Size * z, i * Size)

    def mainLoop(self):
        clock = pygame.time.Clock()
        contadorAnimacionBomberman = 0
        contadorAnimacionEnemigo = 0
        
        while True:
            while self.menu:
                self.intro()
            if self.menu == False:
                    

                    if self.gameOverScreen :
                        self.gameOver()

                    if self.winScreen:
                        self.win()
                    
                    # Verifico si termino el sleep de alguno de mis threads y ejecuto la funcion que corresponda
                    dispatcher.connect(self.exploto, signal= 'explotoBomba', sender = 'threadBomba')
                    dispatcher.connect(self.borrarExplosion, signal = 'borrarExplosion', sender = 'threadExplosion')
                    dispatcher.connect(self.borrarPowerUp, signal = 'borrarPowerUp', sender= 'threadPowerUp')
                    dispatcher.connect(self.resetearSpeed, signal = 'resetearSpeed', sender = 'threadSpeed')

                    # Muestro la imagen de fondo
                    self.background.reloadBackgroundImage()
                    # Muestro los power-ups y la salida (si alguno esta disponible)
                    # Se muestran antes que lo demas ya que tanto los enemigos como
                    # el bomberman deben poder pasarles por encima (visualmente)
                    self.background.reloadSpeedPowerUp()
                    self.background.reloadLifePowerUp()
                    self.background.reloadBombPowerUp()
                    self.background.reloadSalida()

                    # Muestro el sprite del bomberman y su rect
                    self.background.reloadBomberman(self.game.getBombermanDirection(), contadorAnimacionBomberman)
                    self.background.reloadBombermanRect()
                    
                    # Bombas explosiones y obstaculos
                    # Este orden es importante para que se muestre
                    # el sprite de la explosion por debajo de los pilares grises
                    # pero por encima de las cajas rompibles.
                    
                    
                    # 1 - Muestro las cajas rompibles
                    self.background.reloadBoxes() 
                    
                    # 2 - Muestro las explosiones que hayan
                    self.background.reloadExplosiones(self.game.getExplosiones())
                    
                    # 3 - Muestro las cajas no rompibles
                    self.background.reloadBackground()
                
                    # 4 - Muestro las bombas activas       
                    self.background.reloadBombas()
                    
                    # Movimiento y muestreo de los enemigos                    
                    
                    self.game.moverEnemigo()
                    
                    self.background.reloadEnemyRect()
                    
                    velocidadAnimacionEnemigo = 0.16 # Cuanto menor sea mas lenta y mas se notara la animacion
                    contadorAnimacionEnemigo = (contadorAnimacionEnemigo + velocidadAnimacionEnemigo) % 4 
                    
                    for i, enemy in enumerate(self.game.getListaDeEnemigos()):
                        # Enumerate me permite obtener tanto el indice del objeto en la lista como el objeto
                        
                        # Uso math.floor ya que por ej 3.2 necesito rendondearlo para abajo para obtener la animacion
                        # numero 3
                        
                        
                        self.background.reloadEnemy(enemy.getAnimacion(), math.floor(contadorAnimacionEnemigo), i)


                    # Colisiones de los enemigos con cajas
                    
                    enemiesRects = self.game.getEnemyRect()
                    enemigos = self.game.getListaDeEnemigos()

                    # print(str(self.game.getBombRects()))

                    for i in range(0, len(enemiesRects)):
                        if enemiesRects[i].collidelistall(self.game.getListaDeRects()) or enemiesRects[i].collidelistall(self.game.getLaListaDeRectsCajas()) or enemiesRects[i].collidelistall(self.game.getBombRects()): 
                            
                            # Cambio la direccion a la que apunta, la direccion vale 1 o -1
                            self.game.setDireccionEnemigo(self.game.getDireccionEnemigo(i) * -1, i)
                            
                            # Cambio su posicion para que no se choque
                            self.game.setPositionAnterior(i)
                            
                            # Cambio su animacion
                            self.game.setAnimacionEnemigo(i)

                            enemigos[i].setCambioDireccion(False)

                    # Posible cambio de direccion de los enemigos

                    probabilidadDeDoblar = 15 # Cuanto menor sea mas probabilidad hay de doblen
                    probabilidadCambioDireccion = 50 # Cuanto menor sea mas probabilidad hay de que los enemigos se den vuelta
                    

                    for enemy in enemigos:
                        # if enemy.getEnemyPosition() == self.game.obtenerPosicionCentrada(enemy.getEnemyPosition()):
                        if enemy.getCambioDireccion() != True:   
                            if random.randrange(0, probabilidadDeDoblar) == 1:
                                    # Toca cambiar de direccion (si es que puede)
                                    posiblesMovimientos = []

                                    rectDerecha, rectIzquierda, rectArriba, rectAbajo = self.game.getRectsCercanosEnemy(enemy)
                                    # self.background.printearRects(rectDerecha, rectIzquierda, rectArriba, rectAbajo)

                                    animacionActual = enemy.getAnimacion()

                                    if not rectDerecha.collidelistall(self.game.getListaDeRects()) and not rectDerecha.collidelistall(self.game.getLaListaDeRectsCajas()):
                                        if animacionActual == "horizontal2":
                                            if random.randrange(0, probabilidadCambioDireccion) == 1:
                                                posiblesMovimientos.append(("horizontal", 1, 1))
                                        else:
                                            if animacionActual != "horizontal1":
                                                posiblesMovimientos.append(("horizontal", 1, 1))
                                    
                                    if not rectIzquierda.collidelistall(self.game.getListaDeRects()) and not rectIzquierda.collidelistall(self.game.getLaListaDeRectsCajas()):
                                        if animacionActual == "horizontal1":
                                            if random.randrange(0, probabilidadCambioDireccion) == 1:
                                                posiblesMovimientos.append(("horizontal", 2, -1))
                                        else:    
                                            if animacionActual != "horizontal2":
                                                posiblesMovimientos.append(("horizontal", 2, -1))
                                    
                                    if not rectArriba.collidelistall(self.game.getListaDeRects()) and not rectArriba.collidelistall(self.game.getLaListaDeRectsCajas()):
                                        if animacionActual == "vertical1":
                                            if random.randrange(0, probabilidadCambioDireccion) == 1:
                                                posiblesMovimientos.append(("vertical", 2, -1))
                                        else:
                                            if animacionActual != "vertical2":                                        
                                                posiblesMovimientos.append(("vertical", 2, -1))
                                    
                                    if not rectAbajo.collidelistall(self.game.getListaDeRects()) and not rectAbajo.collidelistall(self.game.getLaListaDeRectsCajas()):
                                        if animacionActual == "vertical2":
                                            if random.randrange(0, probabilidadCambioDireccion) == 1:
                                                posiblesMovimientos.append(("vertical", 1, 1))
                                        else:      
                                            if animacionActual != "vertical1":                                  
                                                posiblesMovimientos.append(("vertical", 1, 1))

                                    

                                    if posiblesMovimientos != []:
                                        indiceElegido = random.randrange(0, len(posiblesMovimientos))
                                        movimiento = posiblesMovimientos[indiceElegido]

                                        enemy.setEnemyTipoDeMovimiento(movimiento[0])
                                        enemy.setEnemyAnimacion(movimiento[1])
                                        enemy.setEnemyDireccion(movimiento[2])
                                        enemy.setCambioDireccion(True)
                                        

                    # Colision de bomberman con enemigos
                    
                    playerrect = self.game.getPlayerRect()

                    if len(playerrect.collidelistall(self.game.getlalisaderectsenemigos())) > 0:
                        # pygame.time.wait(2000)
                        self.killBomberman()
                            
                       

                            
                    



                   
                    


                        
            


                   
                                

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN: # Cuando se presiona una tecla

                    if event.key== 1073741906 or event.key== 1073741905 or event.key== 1073741903 or event.key== 1073741904: # Si se presionaron las flechitas
                        
                        # contadorAnimacionBomberman es usado para saber que sprite del bomberman mostrar
                        if self.game.getBombermanPositionAnterior() != self.game.getBombermanPosition():
                            contadorAnimacionBomberman += 1
                        
                        
                        if contadorAnimacionBomberman > 3:
                            contadorAnimacionBomberman = 0
                        
                        
                        # Manejo de colisiones con cajas

                        playerRectFuturo = playerrect
                        direccion = None

                        if event.key == 1073741906:
                            #Arriba
                            playerRectFuturo[1] = playerRectFuturo[1] - self.game.getBombermanSpeed()
                            direccion = 'up'
                        elif event.key == 1073741905:
                            #Abajo
                            playerRectFuturo[1] = playerRectFuturo[1] + self.game.getBombermanSpeed()
                            direccion = 'down'
                        elif event.key == 1073741904:
                            #Izquierda
                            playerRectFuturo[0] = playerRectFuturo[0] - self.game.getBombermanSpeed()
                            direccion = 'left'
                        elif event.key == 1073741903:
                            #Derecha
                            playerRectFuturo[0] = playerRectFuturo[0] + self.game.getBombermanSpeed()
                            direccion = 'right'
                        
                        if len(playerRectFuturo.collidelistall(self.game.getListaDeRects())) > 0 or len(playerRectFuturo.collidelistall(self.game.getLaListaDeRectsCajas())) > 0:
                            # Si hay colision

                            if len(playerRectFuturo.collidelistall(self.game.getRectsBordes())) > 0 or len(playerRectFuturo.collidelistall(self.game.getLaListaDeRectsCajas())) > 0 :
                                # Si la colision es con el borde del mapa, no se cheque la colision
                                # con esquinas para movimiento predictivo
                                self.game.setBombermanPosition(direccion, True)
                            else:
                                # Si la colision es con los bloques del medio si se chequea si es con una
                                # esquina
                                self.game.setBombermanPosition(direccion, False)
                        else:
                            # No hay colision
                            rectsBombas = self.game.getBombRects()
                            
                            # Si la bomba que acabo de poner esta colisionando
                            if self.byPassRectBomba != None:
                                if self.byPassRectBomba.colliderect(playerrect):

                                    # Movelo igual porque sino me quedo bug
                                    
                                    self.game.givePosition((CONTROLES[str(event.key)]))
                                else: 
                                    # Si dejo de colisionar borrame el rectActual de bypass
                                    self.byPassRectBomba = None
                            else:
                                if rectsBombas != [] and playerRectFuturo.collidelistall(rectsBombas):
                                    pass
                                else:

                                    self.game.givePosition((CONTROLES[str(event.key)]))
                                
                    
                    

                            

                    

                    


                    # Verificacion de colisiones con powerUps
                    if self.game.agarroVida():
                        self.game.setBombermanVidas(1)
                        print("AMIGO SOS UN PICANTE TE GANASTE UNA VIDA, AHORA TENES " + str(self.game.getBombermanVidas()) + " VIDAS")
                    elif self.game.agarroBomba():
                        if self.bombas < 4:
                            self.bombas = self.bombas + 1

                            self.BOMBAS_DISPONIBLES.append(self.bombas)
                            
                            print("AMIGO AHORA TENES " + str(self.bombas) + " BOMBAS TOTALES")
                        else:
                            print("Maximo de 4 bombas alcanzado")    
                    elif self.game.agarroVelocidad():
                        
                        self.game.setBombermanSpeed(8)
                        
                        print("AMIGO SOS UN PICANTE AHORA CORRES MAS ")
                        thread = threadSpeed()
                        thread.start()

                    # Verifico colision con salida y a su vez que no quede ningun enemigo en el nivel
                    if len(self.game.getlalisaderectsenemigos()) == 0:
                        if self.game.getSalidaRect() != None:
                            if self.game.getSalidaRect().colliderect(playerrect):
                                # self.winScreen = True
                                self.siguienteNivel()
                                
                
                # Si presiono el espacio (poner bomba)
                
                
                if event.type == pygame.KEYUP:
                    if str(event.key) == '32':            

                        
                        # Si la cantidad de bombas en uso es menor a las disponibles
                        if len(self.BOMBAS_USANDO) < self.bombas:
                            
                            # Esto significa que saliste de arriba de la bomba que pusiste
                            # Implica que no se pueden poner dos bombas en el mismo lugar
                            if self.byPassRectBomba == None:
                            
                                numero_bomba = self.BOMBAS_DISPONIBLES[0] #1
                                self.BOMBAS_DISPONIBLES.remove(numero_bomba)
                                self.BOMBAS_USANDO.append(numero_bomba)
                                

                                bomba = self.game.poner_bomba(numero_bomba)
                                rectBomba = pygame.Rect(bomba.getHitbox())
                                
                                bomba.setRect(rectBomba)
                                self.game.addBombRect(rectBomba)
                                
                                self.byPassRectBomba = rectBomba
                                
                                self.lista_threads.append(threadBomba(numero_bomba, self.game))
                                self.lista_threads[-1].start()
                            
                                    
            pygame.display.update()
            clock.tick(60)
                
if __name__ == "__main__":
    controlador = GameEngine()
