import pygame
import game
import obstacles
from spritesheet import SpriteSheet


class Background():
    def __init__(self, dimensions, game):
        pygame.init()
        pygame.display.set_caption("Bomberman")
        pygame.key.set_repeat(50)

        # Loads
        self.background = None
        self.imagenmenu = None
        self.bomberman = None
        self.bombermanDeath = None
        self.actualDeathSprite = 0
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
            
            bombaSprites = SpriteSheet(self.bomba, 16, 16, 2).getSprites()
            bomba.setImage(bombaSprites)
            
            # Lo corro visualmente para que el png se vea centrado
            x, y = bomba.getposicion()
            xOffset, yOffset = x + 2.5, y + 2.5
            posOffset = [xOffset, yOffset]
            
            self.screen.blit(bomba.image, posOffset)
            rect = pygame.Rect(bomba.getHitbox())
            # pygame.draw.rect(self.screen, "Red", rect, 1)
            bomba.update()




# RELOADS
# Design

    def reloadBackgroundImage(self):  # Pone la imagen del fondo
        self.screen.blit(self.background, (0, 0))

    def reloadMenu(self):
        self.screen.blit(self.imagenmenu, (0, 0))

    def reloadEnemy(self, direction, contador, numeroenemigo):
        
        listadeenemigos = self.game.getListaDeEnemigos()
        
        enemy = listadeenemigos[numeroenemigo]

        self.screen.blit(self.enemigobomberman[direction][contador], enemy.getEnemyPosition())
        
        
        enemyRect = pygame.Rect(enemy.getEnemyRect())
        # _, _, w, h = enemy.getEnemyHitbox()
        # w -= 16
        # h -= 16
        # enemyHitbox = pygame.Rect(0, 0, w, h)
        # enemyHitbox.center = enemyRect.center
        # pygame.draw.rect(self.screen, "Red", enemyRect, 1)
        enemy.setEnemyRect(enemyRect)

# Personajes

    def reloadBomberman(self, direction, contador):
        if not self.game.bombermanIsDead():
            self.actualDeathSprite = 0
            self.screen.blit(self.bomberman[direction][contador], self.game.getBombermanPosition())
        else:
            self.actualDeathSprite += 0.1
            if self.actualDeathSprite > len(self.bombermanDeath): self.actualDeathSprite = 0
            bombermanDeath = self.bombermanDeath[int(self.actualDeathSprite)]
            self.screen.blit(bombermanDeath, self.game.getBombermanPosition())


# Rects

    def debugBombermanRect(self):
        pygame.draw.rect(self.screen, "Green", self.game.getPlayerRect(), 1)

    
    def debugBombermanHitbox(self):
        pygame.draw.rect(self.screen, "Red", self.game.getPlayerHitbox(), 1)
    
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


    def reloadExplosiones(self, explosiones):
        
        # Explosiones es una tupla que contiene (pos, id)
        if len(explosiones) != 0:
            for explosion in explosiones:
                # Offset para que visualmente se vea bien la explosion
                x, y = explosion.getPosition()
                xOffset, yOffset = x + 3, y + 2
                posOffset = [xOffset, yOffset]
                self.screen.blit(self.explosion, posOffset)
                explosion.update()

# Power Ups

    def reloadSpeedPowerUp(self):
        for speed in self.game.getListaDeSpeedPowerUp():
            self.screen.blit(speed.image, speed.getPosition())
            speed.update()

    def reloadBombPowerUp(self):
        for bomb in self.game.getListaDeBombPowerUp():
            self.screen.blit(self.bombPowerUp, bomb.getPosition())
            bomb.update()


    def reloadLifePowerUp(self):
        for life in self.game.getListaDeLifePowerUp():
            self.screen.blit(self.lifePowerUp, life.getPosition())
            life.update()


# LOADS
# Design

    def reloadGameOverScreen(self):
        self.screen.blit(self.gameOverScreen, (0, 0))

# Loads
    def loadImagenMenu(self, path):
        self.imagenmenu = pygame.image.load(path).convert()
        self.imagenmenu = pygame.transform.scale(self.imagenmenu, [925, 555])

# Personajes

    def loadBombermanImage(self, path, pos):

        # size = (, )

        # bombermanImage = pygame.transform.scale(pygame.image.load(path), size).convert_alpha()
        bombermanImage = pygame.image.load(path).convert_alpha()
        bombermanSprites = SpriteSheet(bombermanImage, 30, 30).getSprites()

        self.bomberman = {
            "up": bombermanSprites[0],
            "down": bombermanSprites[1],
            "left": [pygame.transform.flip(leftSprites, 1, 0) for leftSprites in bombermanSprites[2]],
            "right": bombermanSprites[2]
        }

        # self.screen.blit(self.bomberman["down"][0], pos)

    def loadBombermanDeathImage(self, path):
        bombermanDeathImage = pygame.image.load(path).convert_alpha()
        bombermanDeathSprites = SpriteSheet(bombermanDeathImage, 30,30).getSprites()
        self.bombermanDeath = bombermanDeathSprites

    def loadEnemigoBomberman(self, path):
        
        enemigoImage = pygame.image.load(path).convert_alpha()
        enemigoSprites = SpriteSheet(enemigoImage, 30, 30).getSprites()
        
        self.enemigobomberman = {
            "vertical2": enemigoSprites[0],
            "vertical1": enemigoSprites[1],
            "horizontal2": [pygame.transform.flip(leftSprites, 1, 0) for leftSprites in enemigoSprites[2]],
            "horizontal1": enemigoSprites[2]
        }

# Obstaculos

    def loadCaja(self, path):
        self.caja = pygame.image.load(path).convert()


    def loadObstacle(self, path):
        self.obstacle = pygame.image.load(path).convert()

# Bomba y explosiones

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path).convert()
    
    def loadBomba(self, path):
        self.bomba = pygame.image.load(path).convert_alpha()

    def loadExplosion(self, path):
        self.explosion = pygame.image.load(path).convert_alpha()

# Power Ups

    def loadSpeedPowerUp(self, path):
        self.speedPowerUp = pygame.image.load(path)
        self.speedPowerUp = pygame.transform.scale(self.speedPowerUp, [37, 37])

    def loadLifePowerUp(self, path):
        self.lifePowerUp = pygame.image.load(path)
        self.lifePowerUp = pygame.transform.scale(self.lifePowerUp, [37, 37])

    def loadGameOverScreen(self, path):
        self.gameOverScreen = pygame.image.load(path)

    def loadBombPowerUp(self, path):
        self.bombPowerUp = pygame.image.load(path)
        self.bombPowerUp = pygame.transform.scale(self.bombPowerUp, [37, 37])

# Salida
        

    def loadSalida(self, path):
        self.salida = pygame.image.load(path).convert()

    def reloadSalida(self):
        salida = self.game.getSalida()
        self.screen.blit(self.salida, salida.getPosition())
        # pygame.draw.rect(self.screen, (0, 255, 0), salida.getHitbox(), 1)

    def loadWinScreen(self, path):
        self.winScreen = pygame.image.load(path).convert()
        self.winScreen = pygame.transform.scale(self.winScreen, [925, 555])
    
    def reloadWinScreen(self):
        self.screen.blit(self.winScreen, (0, 0))

    def getScreen(self):
        return self.screen

# Getters

    def getSpeedUpImage(self):
        return self.speedPowerUp

    def getBombUpImage(self):
        return self.bombPowerUp

    def getLifeUpImage(self):
        return self.lifePowerUp