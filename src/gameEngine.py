import pygame
import game
import background
import sys
import bomba
import time
import threading

from pydispatch import dispatcher
thread_sender = 'thread_sender'
thread_señal = 'thread_señal'


CONTROLES = {'1073741906': [0, -1], '1073741905': [0, 1], '1073741903': [1, 0], '1073741904': [-1, 0]}


class myThread(threading.Thread):
    def __init__(self, idbomba):
        super().__init__()
        self.numerito = idbomba

    def run(self):
        time.sleep(3.0)
        dispatcher.send(message = self.numerito, signal= thread_señal, sender = thread_sender)

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

        self.lista_threads = []
        self.BOMBAS_USANDO = []
        self.BOMBAS_DISPONIBLES = [1, 2, 3]
        self.cantidad_bombas = 0



        self.mainLoop()

    def intro(self):
        clock = pygame.time.Clock()
        while self.menu:
            self.background.reloadMenu()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYUP:
                    clock.tick(30)
                    self.menu = False
                    pygame.display.update()

    def goMenu():
        pass

    def goOption():
        pass

    def exit():
        pass

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
        self.background.loadSpeedPowerUp("sprites/speedPowerUp.png")
        self.background.loadGameOverScreen("sprites/GameOver.jpg")
        self.background.loadBombPowerUp("sprites/PowerUps/BombUp.png")
        self.background.loadLifePowerUp("sprites/PowerUps/HealthUp.png")

    def Exploto(self, message):
        id_bomba = message
        print('id de la bomba: ', id_bomba)
        self.BOMBAS_USANDO.remove(id_bomba)
        self.BOMBAS_DISPONIBLES.append(id_bomba)
        self.game.sacar_bomba(id_bomba)    
        
    def crearCajasRompibles(self):
        Size = 37
        for z in range(1, 24):
            for i in range(1, 14):
                for x in range(
                     0, len(self.diccionarioposicionesobstaculos[str(z)])
                    ):
                    if self.diccionarioposicionesobstaculos[str(z)][x] == i:
                        self.game.setLaListaDeCajas(Size * z, i * Size)

    def mainLoop(self):
        clock = pygame.time.Clock()
        contador = 0
        eventomovimientoenemigos = pygame.USEREVENT
        while True:
            while self.menu:
                self.intro()
            if self.menu == False:
                    dispatcher.connect(self.Exploto, signal= thread_señal, sender = thread_sender) 
                    self.background.reloadBackgroundImage()
                    self.background.reloadBomberman(self.game.getBombermanDirection(), contador)
                    self.background.reloadBombermanRect()
                    self.background.reloadBackground(self.dimensions)
                    self.background.reloadBoxes()
                    self.background.recargar_imagenes_bombas()
                    self.game.moverEnemigo()


                    for i in range(len(self.game.getListaDeEnemigos())):
                        for enemy in self.game.getListaDeEnemigos():
                            self.background.reloadEnemy(enemy.getAnimacion(), contador,i)
                    # for i in range(len(self.game.getListaDeEnemigos())):
                    #     for enemy in self.game.getListaDeEnemigos():
                    #         self.background.reloadEnemy(enemy.getAnimacion(), contador,i)

                    self.background.reloadSpeedPowerUp()
                    self.background.reloadLifePowerUp()
                    self.background.reloadBombPowerUp()
                    self.game.moverEnemigo()
                    self.background.reloadEnemyRect()
                    pygame.display.update()

                    clock.tick(60)
                    enemyrect = self.game.getEnemyRect()

                    playerrect = self.game.getPlayerRect()
                    if len(playerrect.collidelistall(self.game.getlalisaderectsenemigos())) > 0:
                        self.game.setBombermanVidas(-1)
                        print("EU FIERA MAKINON TE CHOCASTE CONTRA UN WACHIN TE RE MORISTE, TE QUEDAN "+str(self.game.getBombermanVidas())+" VIDAS")
                        self.background.reloadBackgroundImage()

                        self.game.setBombermanPosicionDeInicio()
                        self.background.reloadBombermanRect()
                        self.game.setBombermanSpeed(5)

                        self.game.borarDatosCajas()
                        self.game.borrarDatosEnemigos()

                        self.crearCajasRompibles()
                        self.background.reloadBoxes()
                        self.game.createBoxesRects()

                        self.game.placeEnemies()
                        self.background.reloadEnemy()
                        self.background.reloadEnemyRect()
                        self.game.createEnemiesRects()
                        pygame.display.update()

                    for i in range(0, len(enemyrect)):
                        if len(enemyrect[i].collidelistall(self.game.getListaDeRects())) > 0 or len(enemyrect[i].collidelistall(self.game.getLaListaDeRectsCajas())) > 0: # Colision enemigos con cajas no rompibles
                            self.game.setdireccionenemigo(self.game.getdireccionenemigo(i) * -1, i) # Hago que sume o reste para cambiar direccion
                            self.game.setPositionAnterior(i)
                            pygame.display.update()
                            listadeenemigos = self.game.getListaDeEnemigos()
                            enemy = listadeenemigos[i]
                            if enemy.getAnimacion() == "vertical1":
                                enemy.setAnimacion("vertical2")
                            elif enemy.getAnimacion() == "horizontal1":
                                enemy.setAnimacion("horizontal2")
                            elif enemy.getAnimacion() == "horizontal2":
                                enemy.setAnimacion("horizontal1")
                            elif enemy.getAnimacion() == "vertical2":
                                enemy.setAnimacion("vertical1")
                            pygame.display.update()

                   
                                

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN: # Cuando se presiona una tecla

                    if event.key== 1073741906 or event.key== 1073741905 or event.key== 1073741903 or event.key== 1073741904: # Si se presionaron las flechitas
                        
                        # Contador es usado para saber que sprite del bomberman mostrar
                        if self.game.getBombermanPositionAnterior() != self.game.getBombermanPosition():
                            contador += 1
                        
                        
                        if contador > 3:
                            contador = 0
                        
                        
                        # Manejo de colisiones
                        if len(playerrect.collidelistall(self.game.getListaDeRects())) > 0 or len(playerrect.collidelistall(self.game.getLaListaDeRectsCajas())) > 0:
                            # Si hay colision 
                            self.game.setBombermanPosition()
                        else:
                            # No hay colision
                            self.game.givePosition((CONTROLES[str(event.key)]), self.background.screen)
                    
                    
                    if event.key== 32:
                        if len(playerrect.collidelistall(self.game.getLaListaDeRectsCajas())) > 0:
                            cajaquequieroromper = playerrect.collidelistall(self.game.getLaListaDeRectsCajas())
                            self.game.romperCaja(cajaquequieroromper[0])
                            numerorandom = self.game.getListaRandom()
                            if numerorandom == 0:
                                self.game.createPowerUpSpeedUp(self.game.getCajaRota())
                                self.background.reloadSpeedPowerUp()
                            elif numerorandom == 1:
                                self.game.createPowerUpBombUp(self.game.getCajaRota())
                                self.background.reloadBombPowerUp()
                            elif numerorandom == 2:
                                self.game.createPowerUpVida(self.game.getCajaRota())
                                self.background.reloadLifePowerUp()
                            elif numerorandom > 0:
                                pass
                            

                    playerrect = self.game.getPlayerRect()
                   
                    # if len(playerrect.collidelistall(self.game.getListaDeRects())) > 0 or len(playerrect.collidelistall(self.game.getLaListaDeRectsCajas())) > 0:  # Colision Bomberman//
                    #     self.game.setBombermanPosition()

                    # if len(playerrect.collidelistall(self.game.getLaListaDeRectsCajas())) > 0:  # Colision Bomberman//
                    #     self.game.setBombermanPosition()                        
                    
                    #self.background.reloadBomberman(self.game.getBombermanDirection(), contador)

                    
                     
                    # self.game.moverEnemigo()
                    # self.background.reloadEnemy()
                    # self.background.reloadEnemyRect() 


                    # self.background.reloadBomberman(self.game.getBombermanDirection(), contador)
                    
                    # self.game.moverEnemigo()
                    # self.background.reloadEnemyRect()

                    # enemyrect = self.game.getEnemyRect() 

                    # for i in range(0, len(enemyrect)):
                    #     if len(enemyrect[i].collidelistall(self.game.getListaDeRects())) > 0 or len(enemyrect[i].collidelistall(self.game.getLaListaDeRectsCajas())) > 0: # Colision enemigos con cajas no rompibles
                    #         print(len(enemyrect[i].collidelistall(self.game.getListaDeRects())))
                    #         self.game.setdireccionenemigo(self.game.getdireccionenemigo(i) * -1, i) # Hago que sume o reste para cambiar direccion
                    #         self.game.setPositionAnterior(i)
                            # self.background.reloadEnemy()
                            # self.background.reloadEnemyRect() 


                        # if len(enemyrect[i].collidelistall(self.game.getLaListaDeRectsCajas())) > 0:  # Colision enemigos con cajas rompibles
                        #     self.game.setdireccionenemigo(self.game.getdireccionenemigo(i) * -1, i) # Hago que sume o reste para cambiar direccion
                        #     self.game.setPositionAnterior(i)
                        #     self.background.reloadEnemy()
                        #     self.background.reloadEnemyRect() 

                        # if len(enemyrect[i].collidelistall(self.game.getLaListaDeRectsCajas())) <= 0 and len(enemyrect[i].collidelistall(self.game.getListaDeRects())) <= 0:
                        #     self.game.moverEnemigo()
                        #     self.background.reloadEnemy()
                        #     self.background.reloadEnemyRect() 
                    # for i in range(0, len(enemyrect)):
                    #      if len(enemyrect[i].collidelistall(self.game.getLaListaDeRectsCajas())) > 0:  # Colision enemigos con cajas rompibles
                    #         self.game.setdireccionenemigo(self.game.getdireccionenemigo(i) * -1, i) # Hago que sume o reste para cambiar direccion
                    #         self.game.setPositionAnterior()
                    # pygame.display.update()
                    if len(playerrect.collidelistall(self.game.getListaDeRects())) > 0 or len(playerrect.collidelistall(self.game.getLaListaDeRectsCajas())) > 0:  # Colision Bomberman//
                        self.game.setBombermanPosition()

                    self.background.reloadBomberman(
                        self.game.getBombermanDirection(), contador
                        )
                    self.game.moverEnemigo()
                    self.background.reloadEnemyRect()
                    pygame.display.update()


                    
                     
                    # self.game.moverEnemigo()
                    # self.background.reloadEnemy()
                    # self.background.reloadEnemyRect() 



                    # enemyrect = self.game.getEnemyRect() 

                    # for i in range(0, len(enemyrect)):
                    #     if len(enemyrect[i].collidelistall(self.game.getListaDeRects())) > 0 or len(enemyrect[i].collidelistall(self.game.getLaListaDeRectsCajas())) > 0: # Colision enemigos con cajas no rompibles
                    #         print(len(enemyrect[i].collidelistall(self.game.getListaDeRects())))
                    #         self.game.setdireccionenemigo(self.game.getdireccionenemigo(i) * -1, i) # Hago que sume o reste para cambiar direccion
                    #         self.game.setPositionAnterior(i)
                            # self.background.reloadEnemy()
                            # self.background.reloadEnemyRect() 


                        # if len(enemyrect[i].collidelistall(self.game.getLaListaDeRectsCajas())) > 0:  # Colision enemigos con cajas rompibles
                        #     self.game.setdireccionenemigo(self.game.getdireccionenemigo(i) * -1, i) # Hago que sume o reste para cambiar direccion
                        #     self.game.setPositionAnterior(i)
                        #     self.background.reloadEnemy()
                        #     self.background.reloadEnemyRect() 

                        # if len(enemyrect[i].collidelistall(self.game.getLaListaDeRectsCajas())) <= 0 and len(enemyrect[i].collidelistall(self.game.getListaDeRects())) <= 0:
                        #     self.game.moverEnemigo()
                        #     self.background.reloadEnemy()
                        #     self.background.reloadEnemyRect() 
                    # for i in range(0, len(enemyrect)):
                    #      if len(enemyrect[i].collidelistall(self.game.getLaListaDeRectsCajas())) > 0:  # Colision enemigos con cajas rompibles
                    #         self.game.setdireccionenemigo(self.game.getdireccionenemigo(i) * -1, i) # Hago que sume o reste para cambiar direccion
                    #         self.game.setPositionAnterior() 



                    
                
                # clock.tick(30)


                    listabombup = self.game.getBombUpRect()
                    listaspeedup = self.game.getLifeUpRect()
                    listalifeup = self.game.getSpeedUpRect()
                    
                    if listabombup is not None and len(listabombup) > 0:
                        for i in range(0, len(listabombup)):
                            if len(playerrect.collidelistall(listabombup)) > 0:
                                self.game.borarBombUp(i)

                    if listaspeedup is not None and len(listaspeedup) > 0:
                        for i in range(0, len(listaspeedup)):
                            if len(playerrect.collidelistall(listaspeedup)) > 0:
                                self.game.borarLifeUp(i)
                                self.game.setBombermanVidas(1)
                                print("AMIGO SOS UN PICANTE TE GANASTE UNA VIDA, AHORA TENES " +str(self.game.getBombermanVidas()) + " VIDAS")

                    if listalifeup is not None and len(listalifeup) > 0:
                        for i in range(0, len(listalifeup)):
                            if len(playerrect.collidelistall(listalifeup)) > 0:
                                self.game.borarSpeedUp(i)
                                self.game.setBombermanSpeed(10)
                                print("AMIGO SOS UN PICANTE AHORA CORRES MAS ")

                if event.type == pygame.KEYUP:
                    if str(event.key) == '32':                     
                        if len(self.BOMBAS_USANDO) <= 2:
                            print('len bombas usando', len(self.BOMBAS_USANDO))
                            i = 1
                            for i in range(1, 4):#[1,2,3]
                               numero_bomba = self.BOMBAS_DISPONIBLES.count(i) #1
                               print('numero bomba : ',numero_bomba)
                               if numero_bomba != 0:
                                    self.BOMBAS_DISPONIBLES.remove(i)
                                    self.BOMBAS_USANDO.append(i)
                                    self.game.poner_bomba(i)
                                    self.lista_threads.append(myThread(i))
                                    self.lista_threads[-1].start()
                                    break
                                    
                        if len(playerrect.collidelistall(self.game.getLaListaDeRectsCajas())) > 0:
                             cajaquequieroromper = playerrect.collidelistall(self.game.getLaListaDeRectsCajas())
                             self.game.romperCaja(cajaquequieroromper[0])
                             numerorandom = self.game.getListaRandom()
                             if numerorandom == 0:
                                 self.game.createPowerUpSpeedUp(self.game.getCajaRota())
                                 self.background.reloadSpeedPowerUp()
                             elif numerorandom == 1:
                                 self.game.createPowerUpBombUp(self.game.getCajaRota())
                                 self.background.reloadBombPowerUp()
                             elif numerorandom == 2:
                                 self.game.createPowerUpVida(self.game.getCajaRota())
                                 self.background.reloadLifePowerUp()
                             elif numerorandom > 0:
                                 pass
                pygame.display.flip()

if __name__ == "__main__":
    controlador = GameEngine()
