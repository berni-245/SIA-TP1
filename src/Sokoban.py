'''
Utilizamos una lista de carácteres para representar los diferentes elementos del juego.

1. Muro: #
2. Espacio: -
3. Jugador: @
4. Caja: $
5. Objetivo: .
6. Jugador en objetivo: +
7. Caja en objetivo: *

'''
import pygame, sys, os
from pygame.locals import *

from collections import deque

# Función para mover la caja
def move_box(level, index):
    if level[index] == "-" or level[index] == "@":
        level[index] = "$"
    else:
        level[index] = "*"

# Función para actualizar el jugador
def move_player(level, i):
    if level[i] == "-" or level[i] == "$":
        level[i] = "@"
    else:
        level[i] = "+"

# Función para actualizar el mapa
def move_floor(level, i):
    if level[i] == "@" or level[i] == "$":
        level[i] = "-"
    else:
        level[i] = "."

# Función para detectar la pared
def b_manto(level, width, b, m, t):
    maze = list(level)
    maze[b] = "#"
    if m == t:
        return 1
    queue = deque([])
    queue.append(m)
    d4 = [-1, -width, 1, width]
    m4 = ["l", "u", "r", "d"]
    while len(queue) > 0:
        pos = queue.popleft()
        for i in range(4):
            newpos = pos + d4[i]
            if maze[newpos] in ["-", "."]:
                if newpos == t:
                    return 1
                maze[newpos] = i
                queue.append(newpos)
    return 0


def b_manto_2(level, width, b, m, t):
    maze = list(level)
    maze[b] = "#"
    maze[m] = "@"
    if m == t:
        return 1
    queue = deque([])
    queue.append(m)
    d4 = [-1, -width, 1, width]
    m4 = ["l", "u", "r", "d"]
    while len(queue) > 0:
        pos = queue.popleft()
        for i in range(4):
            newpos = pos + d4[i]
            if maze[newpos] in ["-", "."]:
                maze[newpos] = i
                queue.append(newpos)
                if newpos == t:
                    path = []
                    while maze[t] != "@":
                        path.append(m4[maze[t]])
                        t -= d4[maze[t]]
                    return path
    return []


class Sokoban:

    # Inicializar el juego de Sokoban
    def __init__(self):
        # Establecer el mapa
        self.level = list(
            "#####  #####"
            "#   ####  #"
            "# $      $ #"
            "#  $@$  $ #"
            "# $      $ #"
            "#   ####  #"
            "#####  #####"
        )
    
        # Establecer ancho y alto del mapa y posición del jugador en el mapa (valor del índice en la lista del mapa)
        self.width = 12
        self.height = 7
        self.player = 41
        self.hint = list(self.level)
        self.solution = []
        self.push = 0
        self.todo = []
        self.auto = 0
        self.sbox = 0
        self.queue = []

    # Dibujar el mapa en la ventana de pygame basado en el nivel del mapa
    def draw(self, screen, skin):
        # Obtener el ancho de cada elemento de imagen
        width = skin.get_width() / 4
        offset = (width - 4) / 2

        # Iterar a través de cada elemento de carácter en el nivel del mapa
        for i in range(0, self.width):
            for j in range(0, self.height):
                
                # Obtener el carácter en la fija j y la columna i del mapa
                item = self.level[j*self.width + i]

                # Mostrar como un muro
                if item == '#':
                    # Utilizar el método blit de pygame para mostrar la imagen en la posición especificada,
                    # con las coordenadas de posición (i*width, j*width), y las coordenadas y el ancho-altura
                    # de la imagen en la skin como (0, 2*width, width, width)
                    screen.blit(skin, (i*width, j*width), (0, 2*width, width, width))
                
                # Mostrar como un espacio
                elif item == '-':
                    screen.blit(skin, (i*width, j*width), (0, 0, width, width))
                
                # Mostrar como un jugador
                elif item == '@':
                    screen.blit(skin, (i*width, j*width), (width, 0, width, width))

                # Mostrar como una caja
                elif item == '$':
                    screen.blit(skin, (i*width, j*width), (2*width, 0, width, width))

                # Mostrar como un objetivo
                elif item == '.':
                    screen.blit(skin, (i*width, j*width), (0, width, width, width))

                # Mostrar como el efecto del jugador en un objetivo
                elif item == '+':
                    screen.blit(skin, (i*width, j*width), (width, width, width, width))

                # Mostrar como el efecto de una caja en un objetivo
                elif item == '*':
                    screen.blit(skin, (i*width, j*width), (2*width, width, width, width))
                
                if self.sbox != 0 and self.hint[j * self.width + i] == "1":
                    screen.blit(skin, (i*width + offset, j*width + offset), (3*width, 3 * width, 4, 4))

    # Función para registrar movimiento del jugador
    def move(self, d):
        self._move(d)
        self.todo = []

    # Función interna de movimiento de jugador
    def _move(self, d):
        
        self.sbox = 0

        # Obtener el desplazamiento en el mapa para el movimiento
        h = get_offset(d, self.width)
        h2 = 2 * h


        # Si el área objetivo del movimiento es un espacio vacío o un punto objetivo, solo se moverá el jugador
        if self.level[self.player + h] == '-' or self.level[self.player + h] == '.':
            
            # Mover el jugador a la posición objetivo
            move_player(self.level, self.player + h)
            # Establecer la posición original del jugador después del movimiento
            move_floor(self.level, self.player)
            # Actualizar la posición del jugador
            self.player += h
            # La nueva posición del jugador
            self.player += d
            # Agregar la operación de movimiento a la solución
            self.solution += d

        # Si el área objetivo del movimiento es una caja, tanto la caja como el jugador deben moverse
        elif self.level[self.player + h] == '*' or self.level[self.player + h] == '$':

            # El desplazamiento de la caja y la posición del jugador
            h2 = h*2
            # La caja solo se puede mover si la siguiente posición es un espació vacío o un punto objetivo
            if self.level[self.player + h2] == '-' or self.level[self.player + h2] == '.':
                # Mover la caja al punto objetivo
                move_box(self.level, self.player + h2)
                # Mover el jugador a la posición objetivo
                move_player(self.level, self.player + h)
                # Establecer la posición original del jugador después del movimiento
                move_floor(self.level, self.player)
                # Actualizar la posición del jugador
                self.player += h
                # Marcar la operación de movimiento como un carácter en mayúscula para indicar que se empujó una caja en este paso
                self.solution += d.upper()
                # Incrementar el número de pasos para empujar la caja
                self.push += 1

    # Función para deshacer el movimiento del jugador
    def undo(self):
        
        # Verificar si hay un registro del movimiento
        if self.solution.__len__() > 0:

            # Almacenar el registro de movimiento en la lista 'todo' para la operación rehacer
            self.todo.append(self.solution[-1])
            # Eliminar el registro de movimiento
            self.solution.pop()

            # Obtener el desplazamiento que se debe mover para la operación de deshacer
            h = get_offset(self.todo[-1], self.width) * -1

            # Verificar si esta operación solo mueve el carácter sin empujar una caja
            if self.todo[-1].islower():
                # Mover el carácter de vuelta a su posición original
                move_player(self.level, self.player + h)
                # Establecer la posición actual del carácter en el mapa
                self.player += h
            else:
                # Si este paso empuja una caja, mover el carácter, la caja y realizar las operaciones relacionadas con _move
                move_floor(self.level, self.player - h)
                move_box(self.level, self.player)
                move_player(self.level, self.player + h)
                self.player += h
                self.push -= 1

    # Función para rehacer el movimiento del jugador
    def redo(self):

        # Verificar si hay una operación de deshacer registrada
        if self.todo.__len__() > 0:
            # Volver atrás los pasos deshechos
            self._move(self.todo[-1].lower())
            # Eliminar la operación del registro
            self.todo.pop()

    # Función
    def manto(self, x, y):
        maze = list(self.level)
        maze[self.player] = "@"
        queue = deque([])
        queue.append(self.player)
        d4 = [-1, -self.width, 1, self.width]
        m4 = ["l", "u", "r", "d"]
        while len(queue) > 0:
            pos = queue.popleft()
            for i in range(4):
                newpos = pos + d4[i]
                if maze[newpos] in ["-", "."]:
                    maze[newpos] = i
                    queue.append(newpos)
        t = y * self.width + x
        if maze[t] in range(4):
            self.todo = []
            while maze[t] != "@":
                self.todo.append(m4[maze[t]])
                t -= d4[maze[t]]
        self.auto = 1

# Start pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))

# Load skin
skinfilename = os.path.join('borgar.png')
try:
    skin = pygame.image.load(skinfilename)
except pygame.error as msg:
    print('No se puede cargar la imagen:')
    raise SystemExit(msg)
skin = skin.convert()

# Screen.fill((255,255,255))
screen.fill(skin.get_at((0, 0)))
pygame.dysplay.set_caption("sokoban.py")

# Create Sokoban object
skb = Sokoban()
skb.draw(screen, skin)

clock = pygame.time.Clock()
pygame.key.set_repeat(200, 50)

# Main game loop
while True:
    clock.tick(60)

    if skb.auto == 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    skb.move("l")
                elif event.key == K_UP:
                    skb.move("u")
                elif event.key == K_RIGHT:
                    skb.move("r")
                elif event.key == K_DOWN:
                    skb.move("d")
                elif event.key == K_BACKSPACE:
                    skb.undo()
                    skb.draw(screen, skin)
                elif event.key == K_SPACE:
                    skb.redo()
                    skb.draw(screen, skin)
    pygame.display.update()
    pygame.display.set_caption(
        skb.solution.__len__().__str__() + "/" + skb.push.__str__() + " - sokoban.py"
    )

if __name__ == '__main__':
    main()