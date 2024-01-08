import pygame
import game
import background
import sys
import bomba
import time
from threading import Thread
import threading
from pydispatch import dispatcher
import math


# Son las flechitas, se usan para el movimiento del bomberman

CONTROLES = {'1073741906': [0, -1], '1073741905': [0, 1], '1073741903': [1, 0], '1073741904': [-1, 0]}



# Uso los threads principalmente para poder ejecutar eventos luego de un tiempo gracias al sleep

class threadExplosion(Thread):
    def __init__(self, explosion):
        super().__init__()
        self.explosion = explosion

    def run(self):
        time.sleep(0.5)
        dispatcher.send(message = self.explosion, signal= 'borrarExplosion', sender = 'threadExplosion')
        
        

class threadBomba(Thread):
    def __init__(self, idbomba, game):
        super().__init__()
        self.id = idbomba
        self.game = game

    def run(self):
        time.sleep(3.0)
        if(self.game.getBombas() != []):
            dispatcher.send(message = self.id, signal= 'explotoBomba', sender = 'threadBomba')



class GameEngine():
    def __init__(self):
        self.dimensions = [925, 555]
        self.game = game.Game()
        self.background = background.Background(self.dimensions, self.game)
        self.cargar_imagen_bomba_controlador()
        self.loadImages()
        self.diccionarioposicionesobstaculos = {'1': [5, 9, 10, 11],
                                                '2': [3, 5, 7, 9, 11],
                                                '3': [1, 4, 6, 7, 10, 11, 13],
                                                '4': [0],
                                                '5': [4, 6, 8, 10, 12],
                                                '6': [1, 9],
                                                '7': [1, 3, 4, 5, 10, 11, 13],
                                                '8': [0],
                                                '9': [2, 3, 4, 10],
                                                '10': [3],
                                                '11': [2, 5, 10],
                                                '12': [3, 5, 7, 9, 11],
                                                '13': [2, 13],
                                                '14': [1, 3, 5, 7, 9, 11],
                                                '15': [1, 2, 4],
                                                '16': [1, 7, 9, 11],
                                                '17': [1, 2, 4, 6, 7, 13],
                                                '18': [1, 9, 11],
                                                '19': [1, 2, 3, 6, 8, 9, 10, 12],
                                                '20': [1, 3, 9],
                                                '21': [1, 2, 3, 6, 8, 12],
                                                '22': [1, 3, 9, 11],
                                                '23': [1, 2, 3, 7, 13]
                                                }
        self.game.createObstacles(self.dimensions)   # Creo obstaculos para despues en reload background dibujarlos y alli setear el rect de cada uno
        self.crearCajasRompibles()
        self.game.placeEnemies()
        self.background.reloadEnemyRect()
        self.background.reloadBackground(self.dimensions)
        self.background.reloadBoxes()
        self.game.createRects()
        self.menu = True
        
        self.gameOverScreen = False
        self.winScreen = False

        self.lista_threads = []
        self.BOMBAS_USANDO = []
        self.BOMBAS_DISPONIBLES = [1]
        self.bombas = 1


        self.game.crearSalida()

        self.mainLoop()

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
                    clock.tick(30)
        

    def gameOver(self):
        clock = pygame.time.Clock()
        while self.gameOverScreen:
            self.background.reloadGameOverScreen()
            pygame.display.update()
            clock.tick(30)
            
    def win(self):
        clock = pygame.time.Clock()
        while self.winScreen:
            self.background.reloadWinScreen()
            pygame.display.update()
            clock.tick(30)


    def goMenu():
        pass

    def goOption():
        pass

    def exit():
        pass

    def killBomberman(self):
        self.game.setBombermanVidas(-1)
        print("EU FIERA MAKINON TE CHOCASTE CONTRA UN WACHIN TE RE MORISTE, TE QUEDAN " + str(self.game.getBombermanVidas())+" VIDAS")
        
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

        self.crearCajasRompibles()

        # Necesito hacer este reload que ya que asigna los rects a caja cada
        
        self.background.reloadBoxes()
        
        self.game.createBoxesRects()

        self.game.placeEnemies()
        self.game.createEnemiesRects()

        if self.game.getBombermanVidas() == -1:
            self.gameOverScreen = True



    def cargar_imagen_bomba_controlador(self):
        posicion_bomba = self.game.getBombermanPosition()
        self.background.cargar_imagen_bomba('sprites/Bomba.png', posicion_bomba)
   
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

    def borrarExplosion(self, message):
        # A la hora de borrar la explosion tengo que verificar si el rect de la misma
        # rompio un bloque, mato un enemigo, o nos hiteo a nosotros.

        # message = [pos, idbomba, listaDeRectsExplosion]



        self.game.borrarExplosion(message[1])



    def exploto(self, message):
        id_bomba = message

        
        # Logica 
        self.BOMBAS_USANDO.remove(id_bomba)
        pos = self.game.getBombPos(id_bomba)
        
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
                elif numerorandom == 1:
                    self.game.createPowerUpBombUp(posCajaRota, pygame.Rect(posCajaRota[0], posCajaRota[1], ancho, alto))
                elif numerorandom == 2:
                    self.game.createPowerUpVida(posCajaRota, pygame.Rect(posCajaRota[0], posCajaRota[1], ancho, alto))
                elif numerorandom > 0:
                    pass


        # Enemigos
                 
        enemiesRects = self.game.getEnemyRect()
        enemigosABorrar = []

        for i in range(0, len(enemiesRects)):
            if enemiesRects[i].collidelistall(rectsExplosion):
                enemigosABorrar.append(i)
                
        
        for i in range(0, len(enemigosABorrar)):
            self.game.borrarEnemigo(enemigosABorrar[i])


        # Bomberman
            
        if self.game.getPlayerRect().collidelistall(rectsExplosion):
            self.killBomberman()





        thread = threadExplosion((pos, id_bomba, rects))
        thread.start()
 
        
    def crearCajasRompibles(self):
        Size = 37
        for z in range(1, 24):
            for i in range(1, 14):
                for x in range(0, len(self.diccionarioposicionesobstaculos[str(z)])):
                    if self.diccionarioposicionesobstaculos[str(z)][x] == i:
                        self.game.setLaListaDeCajas(Size * z, i * Size)

    def mainLoop(self):
        clock = pygame.time.Clock()
        contadorAnimacionBomberman = 0
        contadorAnimacionEnemigo = 0
        
        while True:
            while self.menu:
                self.intro()
            if self.menu == False:
                    

                    if self.gameOverScreen == True :
                        self.gameOver()

                    if self.winScreen == True :
                        self.win()
                    
                    # Verifico si termino el sleep de alguno de mis threads y ejecuto la funcion que corresponda
                    dispatcher.connect(self.exploto, signal= 'explotoBomba', sender = 'threadBomba')
                    dispatcher.connect(self.borrarExplosion, signal = 'borrarExplosion', sender = 'threadExplosion')
                    
                    # Muestro la imagen de fondo
                    self.background.reloadBackgroundImage()
                    
                    # Muestro el sprite del bomberman y su rect
                    self.background.reloadBomberman(self.game.getBombermanDirection(), contadorAnimacionBomberman)
                    self.background.reloadBombermanRect()
                    
                    # Bombas explosiones y obstaculos
                    # Este orden es importante para que se muestre
                    # el sprite de la explosion por debajo de los pilares grises
                    # pero por encima de las cajas rompibles.
                    
                    
                    self.background.reloadSalida()

                    # 1 - Muestro las cajas rompibles
                    self.background.reloadBoxes() 
                    
                    # 2 - Muestro las explosiones que hayan
                    self.background.reloadExplosiones(self.game.getExplosiones())
                    
                    # 3 - Muestro las cajas no rompibles
                    self.background.reloadBackground(self.dimensions)
                
                    # 4 - Muestro las bombas activas       
                    self.background.reloadBombas()
                    
                    # Movimiento y muestreo de los enemigos                    
                    
                    self.game.moverEnemigo()
                    
                    self.background.reloadEnemyRect()
                    
                    velocidadAnimacionEnemigo = 0.1 # Cuanto menor sea mas lenta y mas se notara la animacion
                    contadorAnimacionEnemigo = (contadorAnimacionEnemigo + velocidadAnimacionEnemigo) % 4 
                    
                    for i, enemy in enumerate(self.game.getListaDeEnemigos()):
                        # Enumerate me permite obtener tanto el indice del objeto en la lista como el objeto
                        
                        # Uso math.floor ya que por ej 3.2 necesito rendondearlo para abajo para obtener la animacion
                        # numero 3
                        
                        self.background.reloadEnemy(enemy.getAnimacion(), math.floor(contadorAnimacionEnemigo), i)
                    

                    # Colisiones de los enemigos con cajas
                    
                    enemiesRects = self.game.getEnemyRect()

                    for i in range(0, len(enemiesRects)):
                        if enemiesRects[i].collidelistall(self.game.getListaDeRects()) or enemiesRects[i].collidelistall(self.game.getLaListaDeRectsCajas()): 
                         
                            # Cambio la direccion a la que apunta, la direccion vale 1 o -1
                            self.game.setDireccionEnemigo(self.game.getDireccionEnemigo(i) * -1, i)
                            
                            # Cambio su posicion para que no se choque
                            self.game.setPositionAnterior(i)
                            
                            # Cambio su animacion
                            self.game.setAnimacionEnemigo(i)
                            

                            
                       

                            
                    
                    # Muestro los power-ups que esten disponibles
    
                    self.background.reloadSpeedPowerUp()
                    self.background.reloadLifePowerUp()
                    self.background.reloadBombPowerUp()
        


                   
                    

                    playerrect = self.game.getPlayerRect()
                    
                    if len(playerrect.collidelistall(self.game.getlalisaderectsenemigos())) > 0:
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
                            
                        if len(playerrect.collidelistall(self.game.getListaDeRects())) > 0 or len(playerrect.collidelistall(self.game.getLaListaDeRectsCajas())) > 0:
                            # Si hay colision 
                            self.game.setBombermanPosition()
                        else:
                            # No hay colision
                            self.game.givePosition((CONTROLES[str(event.key)]), self.background.screen)
                    
                    

                            

                    

                    


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


                    # Verifico colision con salida y a su vez que no quede ningun enemigo en el nivel
                    
                    if len(self.game.getlalisaderectsenemigos()) == 0:
                        if self.game.getSalidaRect() != None:
                            if self.game.getSalidaRect().colliderect(playerrect):
                                self.winScreen = True
                                
                if event.type == pygame.KEYUP:
                    if str(event.key) == '32':            

                        
                        if len(self.BOMBAS_USANDO) < self.bombas:
                            

                            
                            numero_bomba = self.BOMBAS_DISPONIBLES[0] #1
                            self.BOMBAS_DISPONIBLES.remove(numero_bomba)
                            self.BOMBAS_USANDO.append(numero_bomba)
                            self.game.poner_bomba(numero_bomba)
                            
                            self.lista_threads.append(threadBomba(numero_bomba, self.game))
                            
                            self.lista_threads[-1].start()
                            
                            break
                                    
            pygame.display.update()
            clock.tick(30)
                
if __name__ == "__main__":
    controlador = GameEngine()
