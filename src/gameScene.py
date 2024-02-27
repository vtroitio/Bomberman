import pygame
import math
import random
import gameOverScene
import powerUp

# Eventos en la partida
WIN = pygame.USEREVENT + 1
GAME_OVER = pygame.USEREVENT + 2

class GameScene():
    def __init__(self, background, game):
        self.CONTROLES = {
            str(pygame.K_UP): [0, -1], 
            str(pygame.K_DOWN): [0, 1],
            str(pygame.K_RIGHT): [1, 0],
            str(pygame.K_LEFT): [-1, 0]
        }
        
        self.game = game
        self.background = background

        print("Vidas: " + str(self.game.getBombermanVidas()))

        self.contadorAnimacionBomberman = 0
        self.contadorAnimacionEnemigo = 0
        self.playerrect = pygame.Rect(0,0,0,0)

        # Cuanto mayor sea el numero, menos probabilidad
        # Si es < 6 en obstaculos pone obstaculo en todos lados
        # Si es < 2 en enemigos pone enemigos en todos lados
        # La probabilidad default es 13 en ambos 
        self.probabilidadObstaculos = 20
        self.probabilidadEnemigos = 25

        self.diccionarioposicionesobstaculo = None

        self.crearNivel()

        self.speedUpStart = 0
        self.BOMBAS_USANDO = []
        self.BOMBAS_DISPONIBLES = [1]
        self.numero_bomba = 0
        self.bombas = 1
        self.byPassRectBomba = None
        self.nivelActual = 1

        self.rectBomba = pygame.Rect(0,0,0,0)
    
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

        ancho, altura = self.background.getScreen().get_size()

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

        self.byPassRectBomba = None
        self.game.limpiarExplosiones()

    def siguienteNivel(self):
        self.nivelActual += 1
        self.limpiarNivelActual()
        self.crearNivel()
        print("Pasaste al siguiente nivel :D, estas en el nivel " + str(self.nivelActual))
    
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
    
    def exploto(self, id_bomba):
        # Logica 
        if len(self.game.bombas) > 0:
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
        
        self.game.addExplosion(pos, id_bomba, rects)

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
                posCajaRotaRect = pygame.Rect(posCajaRota[0], posCajaRota[1], ancho, alto)

                if numerorandom == 0:
                    self.game.createPowerUpSpeedUp(powerUp.PowerUp("velocidad", self.background.getSpeedUpImage(), posCajaRota), posCajaRotaRect)
                elif numerorandom == 1:
                    self.game.createPowerUpBombUp(powerUp.PowerUp("bomba", self.background.getBombUpImage(), posCajaRota), posCajaRotaRect)
                elif numerorandom == 2:
                    self.game.createPowerUpVida(powerUp.PowerUp("vida", self.background.getLifeUpImage(), posCajaRota), posCajaRotaRect)

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
        if self.playerHitbox.collidelistall(rectsExplosion):
            self.killBomberman()
    
    def killBomberman(self):
        self.game.setBombermanVidas(-1)
        self.game.borrarPlayerHitbox()
        self.game.setBombermanState()
        
        pygame.time.set_timer(GAME_OVER, 1000, 1)

    def render(self, background):       
        pass

    def update(self, background, game):
        # Muestro la imagen de fondo
        self.background.reloadBackgroundImage()

        # 3 - Muestro las cajas no rompibles
        self.background.reloadBackground()
        # Muestro los power-ups y la salida (si alguno esta disponible)
        # Se muestran antes que lo demas ya que tanto los enemigos como
        # el bomberman deben poder pasarles por encima (visualmente)
        self.background.reloadSpeedPowerUp()
        self.background.reloadLifePowerUp()
        self.background.reloadBombPowerUp()
        self.background.reloadSalida()

        # Muestro las bombas activas       
        self.background.reloadBombas()
        # Muestro las explosiones que hayan
        self.background.reloadExplosiones(self.game.getExplosiones())

        # Muestro el sprite del bomberman
        self.background.reloadBomberman(self.game.getBombermanDirection(), self.contadorAnimacionBomberman)
        self.bombermanPrevPos = self.game.getBombermanPosition()
        # self.background.debugBombermanRect()
        # self.background.debugBombermanHitbox()

        # Bombas explosiones y obstaculos
        # Este orden es importante para que se muestre
        # el sprite de la explosion por debajo de los pilares grises
        # pero por encima de las cajas rompibles.

        # Muestro las cajas rompibles
        self.background.reloadBoxes() 
            
            
        # Muestro las cajas no rompibles
        self.background.reloadBackground()
        

        # Movimiento y muestreo de los enemigos 
        self.game.moverEnemigo()
            
        self.background.reloadEnemyRect()

        velocidadAnimacionEnemigo = 0.16 # Cuanto menor sea mas lenta y mas se notara la animacion
        self.contadorAnimacionEnemigo = (self.contadorAnimacionEnemigo + velocidadAnimacionEnemigo) % 3
            
        for i, enemy in enumerate(self.game.getListaDeEnemigos()):
            # Enumerate me permite obtener tanto el indice del objeto en la lista como el objeto
                
            # Uso math.floor ya que por ej 3.2 necesito rendondearlo para abajo para obtener la animacion
            # numero 3
                
                
            self.background.reloadEnemy(enemy.getAnimacion(), math.floor(self.contadorAnimacionEnemigo), i)

        # Colisiones de los enemigos con cajas
            
        enemiesRects = self.game.getEnemyRect()
        enemigos = self.game.getListaDeEnemigos()

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
            # if enemy.getEnemyPosition() == game.obtenerPosicionCentrada(enemy.getEnemyPosition()):
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
        
        self.playerrect = self.game.getPlayerRect()
        self.playerHitbox = self.game.getPlayerHitbox()
        
        if len(self.playerHitbox.collidelistall(game.getlalisaderectsenemigos())) > 0:
            # pygame.time.wait(2000)
            self.killBomberman()

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
            
            self.speedUpStart = pygame.time.get_ticks()
            self.game.setBombermanSpeed(8)
            
            print("AMIGO SOS UN PICANTE AHORA CORRES MAS ")

        if self.speedUpStart != 0 and pygame.time.get_ticks() - self.speedUpStart >= 10000:
            self.game.setBombermanSpeed(5)
            print("Ya no corres rapido :( ")
            self.speedUpStart = 0
        
        # Verifico colision con salida y a su vez que no quede ningun enemigo en el nivel
        if len(self.game.getlalisaderectsenemigos()) == 0:
            if self.game.getSalidaRect() != None:
                if self.game.getSalidaRect().colliderect(self.playerrect):
                    # self.winScreen = True
                    self.siguienteNivel()

        # Verifico si explotaron las bombas
        for bomb in self.game.get_todas_las_bombas():
            id_bomba = bomb.getId()
            if bomb.explode(): self.exploto(id_bomba)

        # Verifico que hayan terminado la explosiones
        for explosion in self.game.getExplosiones():
            id_explosion = explosion.getId()
            if explosion.conclude(): self.game.borrarExplosion(id_explosion)

    def handleEvents(self, events, background, game):
        pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])
        for event in events:
            if event.type == WIN:
                pass
            if event.type == GAME_OVER:
                vidasRestantes = self.game.getBombermanVidas()
                self.game.setBombermanState()
                self.game.setPlayerHitbox()
                self.limpiarNivelActual()
                if vidasRestantes > 0:
                    print("Vidas: " + str(vidasRestantes))
                    self.crearNivel()
                elif vidasRestantes == 0:
                    print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ GAME OVER ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                    self.manager.goTo(gameOverScene.GameOverScene())
    
            if event.type == pygame.KEYUP:
                if not self.game.bombermanIsDead() and event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.contadorAnimacionBomberman = 0
            if event.type == pygame.KEYDOWN and not self.game.bombermanIsDead():
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT: # Si se presionaron las flechitas
                    
                    # contadorAnimacionBomberman es usado para saber que sprite del bomberman mostrar
                    if self.game.getBombermanPositionAnterior() != self.game.getBombermanPosition():
                        self.contadorAnimacionBomberman += 1

                    if self.contadorAnimacionBomberman > 2:
                        self.contadorAnimacionBomberman = 0

                    # Manejo de colisiones con cajas
                    playerRectFuturo = self.game.getPlayerRect()
                    bombermanSpeed = self.game.getBombermanSpeed()
                    direccion = None

                    if event.key == pygame.K_UP:
                        #Arriba
                        playerRectFuturo.y -= bombermanSpeed
                        direccion = 'up'
                    elif event.key == pygame.K_DOWN:
                        #Abajo
                        playerRectFuturo.y += bombermanSpeed
                        direccion = 'down'
                    elif event.key == pygame.K_LEFT:
                        #Izquierda
                        playerRectFuturo.x -= bombermanSpeed
                        direccion = 'left'
                    elif event.key == pygame.K_RIGHT:
                        #Derecha
                        playerRectFuturo.x += bombermanSpeed
                        direccion = 'right'

                    if len(playerRectFuturo.collidelistall(self.game.getListaDeRects())) > 0 or len(playerRectFuturo.collidelistall(self.game.getLaListaDeRectsCajas())) > 0:
                        # Si hay colision

                        if len(playerRectFuturo.collidelistall(self.game.getRectsBordes())) > 0 or len(playerRectFuturo.collidelistall(self.game.getLaListaDeRectsCajas())) > 0 :
                            # Si la colision es con el borde del mapa, no se cheque la colision
                            # con esquinas para movimiento predictivo
                            self.game.setBombermanPosition(self.bombermanPrevPos, direccion, True)
                        else:
                            # Si la colision es con los bloques del medio si se chequea si es con una
                            # esquina
                            self.game.setBombermanPosition(self.bombermanPrevPos, direccion, False)
                    else:
                        # No hay colision
                        rectsBombas = self.game.getBombRects()
                        
                        # Si la bomba que acabo de poner está colisionando
                        if self.byPassRectBomba != None:
                            if self.byPassRectBomba.colliderect(self.playerrect):
                                # Mover al jugador para evitar quedarse atascado
                                self.game.givePosition(self.CONTROLES[str(event.key)])
                            else: 
                                # Si deja de colisionar, eliminar el rectActual de bypass
                                self.byPassRectBomba = None
                        # Si no hay colisión con la bomba
                        elif not rectsBombas or not playerRectFuturo.collidelistall(rectsBombas):
                            self.game.givePosition(self.CONTROLES[str(event.key)])
                        # Si colisiona con la bomba sin bypass
                        else:
                            self.game.setBombermanPosition(self.bombermanPrevPos, direccion, False)
                
                # if event.key == pygame.K_p:
                #     self.paused = not self.paused
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
 

                            bomba = self.game.poner_bomba(self.numero_bomba)
                            self.rectBomba = pygame.Rect(bomba.getHitbox())

                            bomba.setRect(self.rectBomba)
                            self.game.addBombRect(self.rectBomba)

                            self.byPassRectBomba = self.rectBomba
