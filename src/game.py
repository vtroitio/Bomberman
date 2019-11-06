import wall
import box
import player
import obstacles
import player
import enemy
import copy
import bomba

class Game():

    def __init__(self):
        self.level = 1
        self.wall = wall.Wall()
        self.box = box.Box()
        self.player = player.Player()
        self.LaListaDeObstaculos = []
        self.lalistaderects = []
        self.lalistadeenemigos = []
        self.lalistaderectsenemigos = []
        self.positionAnteriorEnemy = []
        self.lalistadecajas = []
        self.lalistaderectscajas = []
        self.bombas = []

    def placePlayer(self, lifes, speed):
        pass

    def placeEnemies(self):
        self.lalistadeenemigos.append(enemy.Enemy([39, 259],"vertical"))
        self.lalistadeenemigos.append(enemy.Enemy([111, 187],"horizontal"))
        self.lalistadeenemigos.append(enemy.Enemy([187, 40],"vertical"))
        self.lalistadeenemigos.append(enemy.Enemy([185, 335],"horizontal"))
        self.lalistadeenemigos.append(enemy.Enemy([484, 37],"horizontal"))
        self.lalistadeenemigos.append(enemy.Enemy([407, 148],"vertical"))
        self.lalistadeenemigos.append(enemy.Enemy([484, 400],"vertical"))
        self.lalistadeenemigos.append(enemy.Enemy([632, 400],"vertical"))
        self.lalistadeenemigos.append(enemy.Enemy([669, 487],"horizontal"))
        self.lalistadeenemigos.append(enemy.Enemy([780, 333],"vertical"))
        self.lalistadeenemigos.append(enemy.Enemy([777, 260],"horizontal"))
        self.lalistadeenemigos.append(enemy.Enemy([851, 400],"vertical"))

    def createBackground(self):
        pass

    def createWall(position, sprite):
        self.wall.setPosition(position)
        self.wall.setSprite(sprite)

    def createBoxes(self):
        # Creo la primera columna
        for i in range(1,14):
            if i == 5 or i ==9 or i ==10 or i ==11:
                self.lalistadecajas.append(obstacles.Obstacle(37, i * 37))
            else:
                pass  
        # Creo la segunda columna
        for i in range(1,14):
            if i == 3 or i ==5 or i ==7 or i ==9 or i ==11:
                self.lalistadecajas.append(obstacles.Obstacle(74, i * 37))
            else:
                pass  
        # Creo la tercera columna
        for i in range(1,14):
            if i == 1 or i ==4 or i ==6 or i ==7 or i ==10 or i ==11 or i==13:
                self.lalistadecajas.append(obstacles.Obstacle(111, i * 37))
            else:
                pass  
        # Creo la quinta columna
        for i in range(1,14):
            if i == 4 or i ==6 or i ==8 or i ==10 or i ==12:
                self.lalistadecajas.append(obstacles.Obstacle(185, i * 37))
            else:
                pass  
        # Creo la sexta columna
        for i in range(1,14):
            if i == 1 or i == 9:
                self.lalistadecajas.append(obstacles.Obstacle(222, i * 37))
            else:
                pass
        # Creo la septima columna
        for i in range(1,14):
            if i == 1 or i == 3 or i == 4 or i == 5 or i ==10 or i ==11 or i ==13:
                self.lalistadecajas.append(obstacles.Obstacle(259, i * 37))
            else:
                pass
        # Creo la novena columna
        for i in range(1,14):
            if i == 2 or i == 3 or i == 4 or i == 10:
                self.lalistadecajas.append(obstacles.Obstacle(333, i * 37))
            else:
                pass
        # Creo la decima columna
        for i in range(1,14):
            if i == 3:
                self.lalistadecajas.append(obstacles.Obstacle(370, i * 37))
            else:
                pass
        # Creo la onceava columna
        for i in range(1,14):
            if i == 2 or i == 5 or i == 10:
                self.lalistadecajas.append(obstacles.Obstacle(407, i * 37))
            else:
                pass
        # Doceava
        for i in range(1,14):
            if i == 3 or i == 5 or i == 7 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(444, i * 37))
            else:
                pass
        # 13
        for i in range(1,14):
            if i == 2 or i == 13:
                self.lalistadecajas.append(obstacles.Obstacle(481, i * 37))
            else:
                pass
        # 14
        for i in range(1,14):
            if i== 1 or i == 3 or i == 5 or i == 7 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(518, i * 37))
            else:
                pass
        # 15
        for i in range(1,14):
            if i== 1 or i == 2 or i == 4:
                self.lalistadecajas.append(obstacles.Obstacle(555, i * 37))
            else:
                pass
       # 16
        for i in range(1,14):
            if i== 1 or i == 7 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(592, i * 37))
            else:
                pass
        # 17
        for i in range(1,14):
            if i== 1 or i == 2 or i == 4 or i == 6 or i == 7 or i == 13:
                self.lalistadecajas.append(obstacles.Obstacle(629, i * 37))
            else:
                pass
               # 18
        for i in range(1,14):
            if i== 1 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(666, i * 37))
            else:
                pass
               # 18
        for i in range(1,14):
            if i== 1 or i == 2 or i == 3 or i == 6 or i == 8 or i == 9 or i == 10 or i == 12:
                self.lalistadecajas.append(obstacles.Obstacle(703, i * 37))
            else:
                pass
        for i in range(1,14):
            if i== 1 or i == 3 or i == 9:
                self.lalistadecajas.append(obstacles.Obstacle(740, i * 37))
            else:
                pass
        for i in range(1,14):
            if i== 1 or i == 2 or i == 3 or i == 6 or i == 8 or i == 12:
                self.lalistadecajas.append(obstacles.Obstacle(777, i * 37))
            else:
                pass
        for i in range(1,14):
            if i== 1 or i == 3 or i == 9 or i == 11:
                self.lalistadecajas.append(obstacles.Obstacle(814, i * 37))
            else:
                pass
        for i in range(1,14):
            if i== 1 or i == 2 or i == 3 or i == 7 or i == 7 or i == 13:
                self.lalistadecajas.append(obstacles.Obstacle(851, i * 37))
            else:
                pass
        
    def poner_bomba(self, id):
        id_bomba = id
        pos = self.getBombermanPosition()
        self.bombas.append(bomba.Bomb(pos, id_bomba))

    def sacar_bomba(self, idbomba):
        for i in range(len(self.bombas)):
            for bomba in self.bombas:
                objeto = bomba
                print('cantidad de bombas en lista juego', len(self.bombas))
                print('id de la bomba que va a desaparecer.', bomba.getId())
                print('id recibido', idbomba)
                if bomba.getId() == idbomba:
                    self.bombas.remove(bomba)
                    print('cantidad de bombas en lista juego', len(self.bombas))

    def get_todas_las_bombas(self):
        return self.bombas                

    def createObstacles(self, dimensions):
        WidthHeightObstacle = 37  # Tamaño del bloque utilizado

        for i in range(0, int((dimensions[0] / WidthHeightObstacle)) + 1):  # De 0 a 26

            self.LaListaDeObstaculos.append(obstacles.Obstacle(i * WidthHeightObstacle, 0))  # Creo los bloques de la fila de arriba

            self.LaListaDeObstaculos.append(obstacles.Obstacle(i * WidthHeightObstacle, dimensions[1] - WidthHeightObstacle))  # Creo los bloques de la fila de abajo

        for i in range(0, int((dimensions[1] / WidthHeightObstacle)) + 1):  # De 0 a 16

            self.LaListaDeObstaculos.append(obstacles.Obstacle(0, i * WidthHeightObstacle))  # Creo los bloques de las columnas de la izquierda

            self.LaListaDeObstaculos.append(obstacles.Obstacle(dimensions[0] - WidthHeightObstacle, i * WidthHeightObstacle))  # Creo los bloques de las columnas de la derecha

        for x in range(1, int((dimensions[0] / (WidthHeightObstacle * 2))) + 1):  # De 1 a 13
            for y in range(1, int((dimensions[1]) / (WidthHeightObstacle * 2)) + 1):  # De 1 a 8
                self.LaListaDeObstaculos.append(obstacles.Obstacle(x * (WidthHeightObstacle * 2), y * (WidthHeightObstacle * 2)))

    def createRects(self):
        for obstaculo in self.LaListaDeObstaculos:
            self.lalistaderects.append(obstaculo.getObstacleRect())
        for enemy in self.lalistadeenemigos:
            self.lalistaderectsenemigos.append(enemy.getEnemyRect())
        for cajas in self.lalistadecajas:
            self.lalistaderectscajas.append(cajas.getObstacleRect())

# Movimiento

    def givePosition(self, position, ventana):
        self.player.move(position, ventana)

    def getBombermanPosition(self):
        return self.player.getBombermanPosition()

    def getBombermanPositionAnterior(self):
        return self.player.getBobmermanPositionAnterior()

    def getBombermanSpeed(self):
        return self.player.getBombermanSpeed()

    def getBombermanDirection(self):
        return self.player.getBombermanDirection()
        
    def setBombermanPosition(self):
        self.player.setBombermanPosition()

    def moverEnemigo(self):
        for enemy in self.lalistadeenemigos:
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

                
    def setPositionAnterior(self, enemigodeseado):
        # for enemy in self.lalistadeenemigos:
        #     enemy.setPosition(enemy.getEnemyPosicionAnterior())
        enemy = self.lalistadeenemigos[enemigodeseado]
        enemy.setPosition(enemy.getEnemyPosicionAnterior())
    

# Colisiones
    def getListaDeObstaculos(self):
        return self.LaListaDeObstaculos

    def getPlayerRect(self):
        return self.player.getPlayerRect()

    def getListaDeRects(self):
        return self.lalistaderects

    def getPlayerHitbox(self):
        return self.player.getPlayerHitbox()

    def setPlayerRect(self, rect):
        self.player.setPlayerRect(rect)

    def getListaDeEnemigos(self):
        return self.lalistadeenemigos

    def getEnemyRect(self):
        return self.lalistaderectsenemigos
    
    def setdireccionenemigo(self, direccion, numerodeenemigo):
        enemigodeseado = self.lalistadeenemigos[numerodeenemigo]
        enemigodeseado.setEnemyDireccion(direccion)

    def getdireccionenemigo(self, numerodeenemigo):
        enemigodeseado = self.lalistadeenemigos[numerodeenemigo]
        return enemigodeseado.getEnemyDireccion()

    def getListaDeCajas(self):
        return self.lalistadecajas

    def setlalistaderectsenemigos(self, cosa):
        self.lalistaderectsenemigos.append(cosa)
    
    def getlalisaderectsenemigos(self):
        return self.lalistaderectsenemigos
    
    def getLaListaDeRectsCajas(self):
        return self.lalistaderectscajas
    
    def setLalistaDeRectsCajas(self, rect):
        self.lalistaderectscajas.append(rect)

    def romperCaja(self, numerodecaja):
        self.lalistadecajas.pop(numerodecaja)
        self.lalistaderectscajas.pop(numerodecaja)
#bombas
    def get_todas_las_bombas(self):
        return self.bombas
    