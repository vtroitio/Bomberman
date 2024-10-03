# Índice

1. [Descripción del Juego](#bomberman)
2. [Ejecución del Juego](#ejecución-del-juego)
3. [Controles](#controles)
4. [Requisitos del Sistema](#requisitos-del-sistema)
5. [Configuración](#configuración)
   - [Clonar el Repositorio](#clonar-el-repositorio)
   - [Configurar el Entorno Virtual](#configurar-el-entorno-virtual)
   - [Instalar Dependencias](#instalar-dependencias)
6. [Ejecutar el Juego](#ejecutar-el-juego)

# Bomberman


![Bomberman](src/sprites/MenuBomberman.png)

Recreación del famoso videojuego bomberman en python. Con features como:

- Deteccion de esquinas (para un movimiento mas fluido)

- Generacion aleatoria de enemigos y obstaculos

- Power-Ups

- Sprites animados

- Deteccion de colisiones

- Enemigos con deteccion de posibles rutas 

Los controles son las flechas de dirección para moverse y la barra espaciadora para poner las bombas

## Ejecución del Juego

Para iniciar el juego, sigue estos pasos:

1. Navega a la carpeta `src`.
2. Localiza el archivo ejecutable llamado `Bomberman.exe`.
3. Haz doble clic en el archivo para ejecutarlo.

## Controles

- **↑**: Mover hacia arriba
- **←**: Mover hacia la izquierda
- **↓**: Mover hacia abajo
- **→**: Mover hacia la derecha
- **Espacio**: Poner bomba
- **Enter**: Inicia el juego
- **R**: Salir de Game Over

## Requisitos del sistema

- Python 3.10.12
- pip (gestor de paquetes de Python)

## Configuración

### Clonar el repositorio

Para obtener una copia del repositorio, puedes clonarlo utilizando Git:

```
git clone git@github.com:dTaba/Bomberman.git
cd Bomberman
```
### Configurar el entorno virtual (opcional pero recomendado)

Se recomienda utilizar un entorno virtual para evitar conflictos con otras dependencias. Puedes crear uno utilizando venv:


# Linux/macOS

```
python3 -m venv .venv
source venv/bin/activate
```


# Windows

```
python -m venv .venv
venv\Scripts\activate
```

### Instalar dependencias

Una vez configurado el entorno virtual, hay que instalar las dependencias del proyecto utilizando pip y el archivo requirements.txt:

```
pip install -r requirements.txt
```


## Ejecutar el juego

Una vez completados los pasos anteriores, podes ejecutar el juego:

```
python3 ./src/init.py
```
