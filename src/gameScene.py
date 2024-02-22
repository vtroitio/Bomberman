import pygame
import math
import random
import gameOverScene

# Eventos en la partida
BOMBA = pygame.USEREVENT + 1
EXPLOSION = pygame.USEREVENT + 2
POWER_UP = pygame.USEREVENT + 3
SPEED = pygame.USEREVENT + 4
GAME_OVER = pygame.USEREVENT + 5

class GameScene():
    def __init__(self):
        self.dimensions = (925, 555)
        self.background = None
        self.game = None
        self.contadorAnimacionBomberman = 0
        self.contadorAnimacionEnemigo = 0
        self.playerrect = pygame.Rect(0,0,0,0)
        
        self.CONTROLES = {
            str(pygame.K_UP): [0, -1], 
            str(pygame.K_DOWN): [0, 1],
            str(pygame.K_RIGHT): [1, 0],
            str(pygame.K_LEFT): [-1, 0]
        }

        self.probabilidadObstaculos = 13
        self.probabilidadEnemigos = 13

        self.BOMBAS_USANDO = []
        self.BOMBAS_DISPONIBLES = [1]
        self.numero_bomba = 0
        self.bombas = 1
        self.byPassRectBomba = None

    def crearCajasRompibles(self, diccCajas):
        Size = 37
        for z in range(1, 24):
            for i in range(1, 14):
                for x in range(0, len(diccCajas[str(z)])):
                    if diccCajas[str(z)][x] == i:
                        self.game.setLaListaDeCajas(Size * z, i * Size)
    
    
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
            pygame.event.post(pygame.event.Event(GAME_OVER)) 
        
        self.limpiarNivelActual()
        self.crearNivel()
        self.game.limpiarExplosiones()

    
    def render(self, background):       
        self.background = background
        # Muestro la imagen de fondo
        background.reloadBackgroundImage()

        # 3 - Muestro las cajas no rompibles
        background.reloadBackground()

    def update(self, background, game):
        self.game = game
        # Muestro los power-ups y la salida (si alguno esta disponible)
        # Se muestran antes que lo demas ya que tanto los enemigos como
        # el bomberman deben poder pasarles por encima (visualmente)
        background.reloadSpeedPowerUp()
        background.reloadLifePowerUp()
        background.reloadBombPowerUp()
        background.reloadSalida()

        # Muestro el sprite del bomberman y su rect
        background.reloadBomberman(game.getBombermanDirection(), self.contadorAnimacionBomberman)
        background.reloadBombermanRect()

        # Bombas explosiones y obstaculos
        # Este orden es importante para que se muestre
        # el sprite de la explosion por debajo de los pilares grises
        # pero por encima de las cajas rompibles.

        # 1 - Muestro las cajas rompibles
        background.reloadBoxes() 
            
        # 2 - Muestro las explosiones que hayan
        background.reloadExplosiones(game.getExplosiones())
            
        # 3 - Muestro las cajas no rompibles
        background.reloadBackground()
        
        # 4 - Muestro las bombas activas       
        background.reloadBombas()

        # Movimiento y muestreo de los enemigos 
        game.moverEnemigo()
            
        background.reloadEnemyRect()

        velocidadAnimacionEnemigo = 0.16 # Cuanto menor sea mas lenta y mas se notara la animacion
        self.contadorAnimacionEnemigo = (self.contadorAnimacionEnemigo + velocidadAnimacionEnemigo) % 3
            
        for i, enemy in enumerate(game.getListaDeEnemigos()):
            # Enumerate me permite obtener tanto el indice del objeto en la lista como el objeto
                
            # Uso math.floor ya que por ej 3.2 necesito rendondearlo para abajo para obtener la animacion
            # numero 3
                
                
            background.reloadEnemy(enemy.getAnimacion(), math.floor(self.contadorAnimacionEnemigo), i)

        # Colisiones de los enemigos con cajas
            
        enemiesRects = game.getEnemyRect()
        enemigos = game.getListaDeEnemigos()

        # print(str(game.getBombRects()))

        for i in range(0, len(enemiesRects)):
            if enemiesRects[i].collidelistall(game.getListaDeRects()) or enemiesRects[i].collidelistall(game.getLaListaDeRectsCajas()) or enemiesRects[i].collidelistall(game.getBombRects()): 
                    
                # Cambio la direccion a la que apunta, la direccion vale 1 o -1
                game.setDireccionEnemigo(game.getDireccionEnemigo(i) * -1, i)
                    
                # Cambio su posicion para que no se choque
                game.setPositionAnterior(i)
                    
                # Cambio su animacion
                game.setAnimacionEnemigo(i)

                enemigos[i].setCambioDireccion(False)

        # Posible cambio de direccion de los enemigos

        probabilidadDeDoblar = 15 # Cuanto menor sea mas probabilidad hay de doblen
        probabilidadCambioDireccion = 50 # Cuanto menor sea mas probabilidad hay de que los enemigos se den vuelta
            

        for enemy in enemigos:
            # if enemy.getEnemyPosition() == game.obtenerPosicionCentrada(enemy.getEnemyPosition()):
            if enemy.getCambioDireccion() != True:   
                if random.randrange(0, probabilidadDeDoblar) == 1:
                    # Toca cambiar de direccion (si es que puede)
                    posiblesMovimientos = []

                    rectDerecha, rectIzquierda, rectArriba, rectAbajo = game.getRectsCercanosEnemy(enemy)
                    # self.background.printearRects(rectDerecha, rectIzquierda, rectArriba, rectAbajo)

                    animacionActual = enemy.getAnimacion()

                    if not rectDerecha.collidelistall(game.getListaDeRects()) and not rectDerecha.collidelistall(game.getLaListaDeRectsCajas()):
                        if animacionActual == "horizontal2":
                            if random.randrange(0, probabilidadCambioDireccion) == 1:
                                posiblesMovimientos.append(("horizontal", 1, 1))
                        else:
                            if animacionActual != "horizontal1":
                                posiblesMovimientos.append(("horizontal", 1, 1))
                            
                    if not rectIzquierda.collidelistall(game.getListaDeRects()) and not rectIzquierda.collidelistall(game.getLaListaDeRectsCajas()):
                        if animacionActual == "horizontal1":
                            if random.randrange(0, probabilidadCambioDireccion) == 1:
                                posiblesMovimientos.append(("horizontal", 2, -1))
                        else:    
                            if animacionActual != "horizontal2":
                                posiblesMovimientos.append(("horizontal", 2, -1))
                            
                    if not rectArriba.collidelistall(game.getListaDeRects()) and not rectArriba.collidelistall(game.getLaListaDeRectsCajas()):
                        if animacionActual == "vertical1":
                            if random.randrange(0, probabilidadCambioDireccion) == 1:
                                posiblesMovimientos.append(("vertical", 2, -1))
                        else:
                            if animacionActual != "vertical2":                                        
                                posiblesMovimientos.append(("vertical", 2, -1))
                            
                    if not rectAbajo.collidelistall(game.getListaDeRects()) and not rectAbajo.collidelistall(game.getLaListaDeRectsCajas()):
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
        
        # self.playerrect = game.getPlayerRect()
        
        # if len(playerrect.collidelistall(game.getlalisaderectsenemigos())) > 0:
        #     # pygame.time.wait(2000)
        #     self.killBomberman()

    def handleEvents(self, events, game):
        for event in events:
            if event.type == GAME_OVER:
                self.manager.goTo(gameOverScene.GameOverScene())
            if event.type == BOMBA:
                id_bomba = self.numero_bomba

                # Logica 
                if len(self.BOMBAS_USANDO) > 0:
                    self.BOMBAS_USANDO.remove(id_bomba)
                    
                    x,y = game.getBombPos(id_bomba)
                    offset = 1
                    pos = [x , y + offset]
                    
                    self.BOMBAS_DISPONIBLES.append(id_bomba)
                    game.sacar_bomba(id_bomba)    

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
                
                game.addExplosion((pos, id_bomba, rects))

                rectsExplosion = []

                for rect in rects:
                    rectsExplosion.append(pygame.Rect(rect[0], rect[1], rect[2], rect[3]))

                # Tengo que verificar las colisiones que tuvo la explosion
                # Ya sea con el bomberman, enemigos o bloques rompibles
                

                # Reviso colision de explosion con cajas rompibles
                    
                for rect in rectsExplosion:
                    
                    if rect.collidelistall(game.getLaListaDeRectsCajas()):
                    
                        caja = rect.collidelistall(game.getLaListaDeRectsCajas())
                        game.romperCaja(caja[0])
                        
                        # numerorandom = game.getListaRandom()
                        
                        # posCajaRota = game.getCajaRota()

                        # if numerorandom == 0:
                        #     game.createPowerUpSpeedUp(posCajaRota, pygame.Rect(posCajaRota[0], posCajaRota[1], ancho, alto))                             
                        #     threadVelocidad = threadPowerUp('velocidad')
                        #     threadVelocidad.start()
                        # elif numerorandom == 1:
                        #     game.createPowerUpBombUp(posCajaRota, pygame.Rect(posCajaRota[0], posCajaRota[1], ancho, alto))
                        #     threadBomba = threadPowerUp('bomba')
                        #     threadBomba.start()
                        # elif numerorandom == 2:
                        #     game.createPowerUpVida(posCajaRota, pygame.Rect(posCajaRota[0], posCajaRota[1], ancho, alto))
                        #     threadVida = threadPowerUp('vida')
                        #     threadVida.start()
                        # elif numerorandom > 0:
                        #     pass

                # Enemigos
                        
                enemiesRects = game.getEnemyRect()
                enemigosABorrar = []

                offsetPostPop = 0

                for i in range(0, len(enemiesRects)):
                    if enemiesRects[i].collidelistall(rectsExplosion):
                        # print("El indice del enemigo que colisiono es: " + str(i))

                        indice = i - offsetPostPop
                        enemigosABorrar.append(indice)
                        offsetPostPop = offsetPostPop + 1
                
                for indice in enemigosABorrar:
                    game.borrarEnemigo(indice)

                # Bomberman
                if game.getPlayerRect().collidelistall(rectsExplosion):
                    self.killBomberman()
                pygame.time.set_timer(EXPLOSION, 300, 1)
            if event.type == EXPLOSION:
                game.borrarExplosion(self.numero_bomba)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.contadorAnimacionBomberman = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT: # Si se presionaron las flechitas
                    
                    # contadorAnimacionBomberman es usado para saber que sprite del bomberman mostrar
                    if game.getBombermanPositionAnterior() != game.getBombermanPosition():
                        self.contadorAnimacionBomberman += 1

                    if self.contadorAnimacionBomberman > 2:
                        self.contadorAnimacionBomberman = 0

                    # Manejo de colisiones con cajas
                    playerRectFuturo = game.getPlayerRect()
                    direccion = None

                    if event.key == pygame.K_UP:
                        #Arriba
                        playerRectFuturo[1] = playerRectFuturo[1] -game.getBombermanSpeed()
                        direccion = 'up'
                    elif event.key == pygame.K_DOWN:
                        #Abajo
                        playerRectFuturo[1] = playerRectFuturo[1] + game.getBombermanSpeed()
                        direccion = 'down'
                    elif event.key == pygame.K_LEFT:
                        #Izquierda
                        playerRectFuturo[0] = playerRectFuturo[0] - game.getBombermanSpeed()
                        direccion = 'left'
                    elif event.key == pygame.K_RIGHT:
                        #Derecha
                        playerRectFuturo[0] = playerRectFuturo[0] + game.getBombermanSpeed()
                        direccion = 'right'


                    if len(playerRectFuturo.collidelistall(game.getListaDeRects())) > 0 or len(playerRectFuturo.collidelistall(game.getLaListaDeRectsCajas())) > 0:
                        # Si hay colision

                        if len(playerRectFuturo.collidelistall(game.getRectsBordes())) > 0 or len(playerRectFuturo.collidelistall(game.getLaListaDeRectsCajas())) > 0 :
                            # Si la colision es con el borde del mapa, no se cheque la colision
                            # con esquinas para movimiento predictivo
                            game.setBombermanPosition(direccion, True)
                        else:
                            # Si la colision es con los bloques del medio si se chequea si es con una
                            # esquina
                            game.setBombermanPosition(direccion, False)
                    else:
                        # No hay colision
                        rectsBombas = game.getBombRects()
                        
                        # Si la bomba que acabo de poner esta colisionando
                        if self.byPassRectBomba != None:
                            if self.byPassRectBomba.colliderect(self.playerrect):

                                # Movelo igual porque sino me quedo bug
                                
                                game.givePosition((self.CONTROLES[str(event.key)]))
                            else: 
                                # Si dejo de colisionar borrame el rectActual de bypass
                                self.byPassRectBomba = None
                        else:
                            if rectsBombas != [] and playerRectFuturo.collidelistall(rectsBombas):
                                pass
                            else:

                                game.givePosition((self.CONTROLES[str(event.key)]))    
                
                # Si presiono el espacio (poner bomba)
                if event.key == pygame.K_SPACE:
                    
                    # Si la cantidad de bombas en uso es menor a las disponibles
                    if len(self.BOMBAS_USANDO) < self.bombas:
                        
                        # Esto significa que saliste de arriba de la bomba que pusiste
                        # Implica que no se pueden poner dos bombas en el mismo lugar
                        if self.byPassRectBomba == None:
                        
                            self.numero_bomba = self.BOMBAS_DISPONIBLES[0] #1
                            self.BOMBAS_DISPONIBLES.remove(self.numero_bomba)
                            self.BOMBAS_USANDO.append(self.numero_bomba)
 

                            bomba = game.poner_bomba(self.numero_bomba)
                            rectBomba = pygame.Rect(bomba.getHitbox())

                            bomba.setRect(rectBomba)
                            game.addBombRect(rectBomba)

                            self.byPassRectBomba = rectBomba
                            
                            pygame.time.set_timer(BOMBA, 2000, 1)
                            