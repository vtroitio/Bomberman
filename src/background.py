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

        # Setear tamaño de la pantalla
        self.screen = pygame.display.set_mode(dimensions)
        self.dimensions = dimensions

        self.time = 0
        self.game = game        # self.game = game.Game()
        self.blue = (0, 0, 255)
        self.contadordepasos = 0
# Reload
    def recargar_imagenes_bombas(self):
        for bomba in self.game.get_todas_las_bombas():
            self.screen.blit(self.bomba, bomba.getposicion())

    def reloadBackground(self, dimensions):  # Crea las filas y columnas
        for obstaculo in self.game.getListaDeObstaculos():

            self.screen.blit(self.obstacle, obstaculo.getPosition())
            obstaculo.setObstacleRect(pygame.draw.rect(self.screen, (255, 0, 0), obstaculo.getHitbox(), 1))

    def reloadBomberman(self, direction, contador):
        self.screen.blit(self.bomberman[direction][contador],
                         self.game.getBombermanPosition())
# RELOADS
# Design

    def reloadBackgroundImage(self):  # Pone la imagen del fondo
        self.screen.blit(self.background, (0, 0))

    def reloadBombermanRect(self):
        rect = pygame.draw.rect(self.screen, (0, 0, 0),
                                self.game.getPlayerHitbox(), 2)
        self.game.setPlayerRect(rect)

    def reloadMenu(self):
        self.screen.blit(self.imagenmenu, (0, 0))

    def reloadEnemy(self, direction, contador, numeroenemigo):
        listadeenemigos = self.game.getListaDeEnemigos()
        enemy = listadeenemigos[numeroenemigo]
        self.screen.blit(self.enemigobomberman[direction][contador], enemy.getEnemyPosition())
        enemy.setEnemyRect(pygame.draw.rect(self.screen, (255, 0, 0),
                           enemy.getEnemyHitbox(), 1))

# Personajes

    def reloadBomberman(self, direction, contador):
        self.screen.blit(self.bomberman[direction][contador], self.game.getBombermanPosition())

# Rects

    def reloadBombermanRect(self):
        rect = pygame.draw.rect(self.screen, (255, 0, 0), self.game.getPlayerHitbox(), 2)
        self.game.setPlayerRect(rect)

    def reloadEnemyRect(self):
        for enemy in self.game.getListaDeEnemigos():
            cosa = pygame.draw.rect(self.screen, (255, 0, 0), enemy.getEnemyHitbox(), 1)
            enemy.setEnemyRect(cosa)
            self.game.setlalistaderectsenemigos(cosa)
# Obstaculos

    def reloadBackground(self, dimensions):  # Crea las filas y columnas
        for obstaculo in self.game.getListaDeObstaculos():

            self.screen.blit(self.obstacle, obstaculo.getPosition())
            obstaculo.setObstacleRect(pygame.draw.rect(self.screen, (255, 0, 0), obstaculo.getHitbox(), 1))

    def reloadBoxes(self):
        for cajas in self.game.getListaDeCajas():
            self.screen.blit(self.caja, cajas.getPosition())
            cajas.setObstacleRect(pygame.draw.rect(self.screen, (255, 0, 0), cajas.getHitbox(), 1))

# Bomba y explosiones

    def reloadBomba(self):
        self.screen.blit(self.bomba, self.game.getBombermanPosition())

    def reloadExplosiones(self, explosiones):
        
        # Explosiones es una tupla que contiene (pos, id)
        if len(explosiones) == 0:
            pass
        else:
            for explosion in explosiones:
                # Offset para centrar la explosion
                pos = explosion[0]
                self.screen.blit(self.explosion, pos)
       
        

# Power Ups

    def reloadSpeedPowerUp(self):
        for speed in self.game.getListaDeSpeedPowerUp():
            self.screen.blit(self.speedPowerUp, speed.getPosition())
            rect = pygame.draw.rect(self.screen, (255, 255, 0), speed.getHitbox(), 1)
            speed.setRect(rect)
            self.game.setRectSpeedUp(rect)

    def reloadBombPowerUp(self):
        for bomb in self.game.getListaDeBombPowerUp():
            self.screen.blit(self.bombPowerUp, bomb.getPosition())
            rect = pygame.draw.rect(self.screen, (255, 255, 0), bomb.getHitbox(), 1)
            bomb.setRect(rect)
            self.game.setRectBombUp(rect)

    def reloadLifePowerUp(self):
        for life in self.game.getListaDeLifePowerUp():
            self.screen.blit(self.lifePowerUp, life.getPosition())
            rect = pygame.draw.rect(self.screen, (255, 255, 0), life.getHitbox(), 1)
            life.setRect(rect)
            self.game.setRectLifeUp(rect)

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
        self.enemigobomberman = pygame.image.load(path)
        self.enemigobomberman = pygame.transform.scale(self.enemigobomberman, [30, 30])

# Obstaculos

    def loadCaja(self, path):
        self.caja = pygame.image.load(path)

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
