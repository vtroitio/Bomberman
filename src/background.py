import pygame
import game
import obstacles


class Background():
    def __init__(self, dimensions, game):
        pygame.init()
        pygame.display.set_caption("Bomberman")
        pygame.key.set_repeat(50)

        # Loads
        self.background = None
        self.imagenmenu = None
        self.bomberman = None
        self.obstacle = None
        self.startmenu = None
        self.caja = None
        self.movimientoizquierda = None
        self.enemigobomberman = None
        self.gameOverScreen = None
        self.explosion = None
        self.salida = None
        self.winScreen = None

        # Setear tamaño de la pantalla
        self.screen = pygame.display.set_mode(dimensions)
        self.dimensions = dimensions

        self.time = 0
        self.game = game        # self.game = game.Game()
        self.blue = (0, 0, 255)
        self.contadordepasos = 0
# Reload
    def reloadBombas(self):
        for bomba in self.game.get_todas_las_bombas():
            
            # Lo corro visualmente para que el png se vea centrado
            x, y = bomba.getposicion()
            xOffset, yOffset = x + 8, y + 8
            posOffset = [xOffset, yOffset]
            
            self.screen.blit(self.bomba, posOffset)




# RELOADS
# Design

    def reloadBackgroundImage(self):  # Pone la imagen del fondo
        self.screen.blit(self.background, (0, 0))

    def reloadBombermanRect(self):
        rect = pygame.Rect(self.game.getPlayerHitbox())
        self.game.setPlayerRect(rect)

    def reloadMenu(self):
        self.screen.blit(self.imagenmenu, (0, 0))

    def reloadEnemy(self, direction, contador, numeroenemigo):
        
        listadeenemigos = self.game.getListaDeEnemigos()
        
        enemy = listadeenemigos[numeroenemigo]
        
        self.screen.blit(self.enemigobomberman[direction][contador], enemy.getEnemyPosition())
        
        enemy.setEnemyRect(pygame.Rect(enemy.getEnemyHitbox()))

# Personajes

    def reloadBomberman(self, direction, contador):
        self.screen.blit(self.bomberman[direction][contador], self.game.getBombermanPosition())


# Rects

    def reloadBombermanRect(self):
        rect = pygame.Rect(self.game.getPlayerHitbox())
        # pygame.draw.rect(self.screen, (255, 0, 0), self.game.getPlayerHitbox(), 1)
        self.game.setPlayerRect(rect)

    def reloadEnemyRect(self):
        for enemy in self.game.getListaDeEnemigos():
            rect = pygame.Rect(enemy.getEnemyHitbox())
            enemy.setEnemyRect(rect)
            self.game.setlalistaderectsenemigos(rect)

    def printearRects(self, rect1, rect2, rect3, rect4):
        pygame.draw.rect(self.screen, (255, 0, 0), rect1, 1)
        pygame.draw.rect(self.screen, (255, 0, 0), rect2, 1)
        pygame.draw.rect(self.screen, (255, 0, 0), rect3, 1)
        pygame.draw.rect(self.screen, (255, 0, 0), rect4, 1)

# Obstaculos

    def reloadBackground(self):  # Muestra los pilares en pantalla y les asigna su rect
        for obstaculo in self.game.getListaDeObstaculos():
            self.screen.blit(self.obstacle, obstaculo.getPosition())
            obstaculo.setObstacleRect(pygame.draw.rect(self.screen, (0, 0, 0, 0), obstaculo.getHitbox(), 1))
        

    def reloadBoxes(self):
        for cajas in self.game.getListaDeCajas():
            self.screen.blit(self.caja, cajas.getPosition())
            cajas.setObstacleRect(pygame.Rect(cajas.getHitbox()))

# Bomba y explosiones

    def reloadBomba(self):
        self.screen.blit(self.bomba, self.game.getBombermanPosition())

    def reloadExplosiones(self, explosiones):
        
        
        
        # Explosiones es una tupla que contiene (pos, id)
        if len(explosiones) == 0:
            pass
        else:
            

            for rect in explosiones[0][2]:
                pass
                # pygame.draw.rect(self.screen, (0, 0, 255), rect, 1)


            for explosion in explosiones:
                # Offset para que visualmente se vea bien la explosion
                x, y = explosion[0]
                xOffset, yOffset = x + 3, y + 2
                posOffset = [xOffset, yOffset]
                self.screen.blit(self.explosion, posOffset)


                
                       
        

# Power Ups

    def reloadSpeedPowerUp(self):
        for speed in self.game.getListaDeSpeedPowerUp():
            self.screen.blit(self.speedPowerUp, speed.getPosition())
            # pygame.draw.rect(self.screen, (0, 255, 0), speed.getHitbox(), 1)

    def reloadBombPowerUp(self):
        for bomb in self.game.getListaDeBombPowerUp():
            self.screen.blit(self.bombPowerUp, bomb.getPosition())
            # pygame.draw.rect(self.screen, (0, 255, 0), bomb.getHitbox(), 1)


    def reloadLifePowerUp(self):
        for life in self.game.getListaDeLifePowerUp():
            self.screen.blit(self.lifePowerUp, life.getPosition())
            # pygame.draw.rect(self.screen, (0, 255, 0), life.getHitbox(), 1)


# LOADS
# Design

    def reloadGameOverScreen(self):
        self.screen.blit(self.gameOverScreen, (0, 0))

# Loads
    def loadImagenMenu(self, path):
        self.imagenmenu = pygame.image.load(path)
        self.imagenmenu = pygame.transform.scale(self.imagenmenu, [925, 555])

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)


# Personajes

    def loadBombermanImage(self, path, pos):
        self.bomberman = {
            "up": [pygame.image.load(path + "b1.png"),
                   pygame.image.load(path + "b2.png"),
                   pygame.image.load(path + "b1.png"),
                   pygame.image.load(path + "b3.png")],
            "down": [pygame.image.load(path + "f1.png"),
                     pygame.image.load(path + "f2.png"),
                     pygame.image.load(path + "f1.png"),
                     pygame.image.load(path + "f3.png")],
            "left": [pygame.image.load(path + "l1.png"),
                     pygame.image.load(path + "l2.png"),
                     pygame.image.load(path + "l1.png"),
                     pygame.image.load(path + "l3.png")],
            "right": [pygame.image.load(path + "r1.png"),
                      pygame.image.load(path + "r2.png"),
                      pygame.image.load(path + "r1.png"),
                      pygame.image.load(path + "r3.png")]
        }
        self.screen.blit(self.bomberman["down"][0], pos)

    def loadEnemigoBomberman(self, path):
        self.enemigobomberman = {
            "vertical2": [pygame.image.load(path + "b1.png"),
                        pygame.image.load(path + "b2.png"),
                        pygame.image.load(path + "b1.png"),
                        pygame.image.load(path + "b3.png")],
            "vertical1": [pygame.image.load(path + "f1.png"),
                        pygame.image.load(path + "f2.png"),
                        pygame.image.load(path + "f1.png"),
                        pygame.image.load(path + "f3.png")],
            "horizontal2": [pygame.image.load(path + "l1.png"),
                            pygame.image.load(path + "l2.png"),
                            pygame.image.load(path + "l1.png"),
                            pygame.image.load(path + "l3.png")],
            "horizontal1": [pygame.image.load(path + "r1.png"),
                            pygame.image.load(path + "r2.png"),
                            pygame.image.load(path + "r1.png"),
                            pygame.image.load(path + "r3.png")]
        }


# Obstaculos

    def loadCaja(self, path):
        self.caja = pygame.image.load(path)


    def loadObstacle(self, path):
        self.obstacle = pygame.image.load(path)

# Bomba y explosiones

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)
    
    def cargar_imagen_bomba(self, sprite, pos):
        self.bomba = pygame.image.load(sprite)
    
    def loadBomba(self, path):
        self.bomba = pygame.image.load(path)

    def loadExplosion(self, path):
        self.explosion = pygame.image.load(path)

# Power Ups

    def loadSpeedPowerUp(self, path):
        self.speedPowerUp = pygame.image.load(path)
        self.speedPowerUp = pygame.transform.scale(self.speedPowerUp, [36, 36])

    def loadLifePowerUp(self, path):
        self.lifePowerUp = pygame.image.load(path)
        self.lifePowerUp = pygame.transform.scale(self.lifePowerUp, [36, 36])

    def loadGameOverScreen(self, path):
        self.gameOverScreen = pygame.image.load(path)

    def loadBombPowerUp(self, path):
        self.bombPowerUp = pygame.image.load(path)
        self.bombPowerUp = pygame.transform.scale(self.bombPowerUp, [36, 36])

# Salida
        

    def loadSalida(self, path):
        self.salida = pygame.image.load(path)

    def reloadSalida(self):
        salida = self.game.getSalida()
        self.screen.blit(self.salida, salida.getPosition())
        # pygame.draw.rect(self.screen, (0, 255, 0), salida.getHitbox(), 1)

    def loadWinScreen(self, path):
        self.winScreen = pygame.image.load(path)
        self.winScreen = pygame.transform.scale(self.winScreen, [925, 555])
    
    def reloadWinScreen(self):
        self.screen.blit(self.winScreen, (0, 0))