import pygame
import math
import random
import time
from pydispatch import dispatcher
from threading import Thread

EXPLOSION = pygame.USEREVENT + 1

class GameScene():
    def __init__(self):
        self.contadorAnimacionBomberman = 0
        self.contadorAnimacionEnemigo = 0
        self.playerrect = pygame.Rect(0,0,0,0)
        self.CONTROLES = {str(pygame.K_UP): [0, -1], 
                          str(pygame.K_DOWN): [0, 1],
                          str(pygame.K_RIGHT): [1, 0],
                          str(pygame.K_LEFT): [-1, 0]}
        
        self.lista_threads = []
        self.BOMBAS_USANDO = []
        self.BOMBAS_DISPONIBLES = [1]
        self.bombas = 1
        self.byPassRectBomba = None

    def render(self, background):       
        # Muestro la imagen de fondo
        background.reloadBackgroundImage()

        # 3 - Muestro las cajas no rompibles
        background.reloadBackground()

    def update(self, background, game):

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
            # if event.type == EXPLOSION:
            
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
                        
                            numero_bomba = self.BOMBAS_DISPONIBLES[0] #1
                            self.BOMBAS_DISPONIBLES.remove(numero_bomba)
                            self.BOMBAS_USANDO.append(numero_bomba)
                            

                            bomba = game.poner_bomba(numero_bomba)
                            rectBomba = pygame.Rect(bomba.getHitbox())
                            
                            bomba.setRect(rectBomba)
                            game.addBombRect(rectBomba)
                            
                            self.byPassRectBomba = rectBomba
        
