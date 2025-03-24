## 1. Pygame Initialization
import pygame, sys, os
from pygame.locals import *
from collections import deque

# VARIABLES
left = False
rigth = False
up = False
down = False
walkCount = 0
x = 0
v = 20
px = 0
py = 0
W, H = 750, 500

# Start Pygame
pygame.init()

## 2. Window setup
screen = pygame.display.set_mode((W, H))
icon = pygame.image.load("assets/Sokoban pack/PNG/Character4.png").convert()
pygame.display.set_icon(icon)

## 3. Load the skin
skinfilename = os.path.join('assets','Sokoban pack','Sample_Sokoban.png')

## CHARACTER
quieto = pygame.image.load("assets/Sokoban pack/PNG/Character4.png")

caminaDerecha = [pygame.image.load("assets/Sokoban pack/PNG/Character2.png"),
                    pygame.image.load("assets/Sokoban pack/PNG/Character3.png")]

caminaIzquierda = [pygame.image.load("assets/Sokoban pack/PNG/Character1.png"),
                    pygame.image.load("assets/Sokoban pack/PNG/Character10.png")]

caminaArriba = [pygame.image.load("assets/Sokoban pack/PNG/Character7.png"),
                pygame.image.load("assets/Sokoban pack/PNG/Character8.png"),
                pygame.image.load("assets/Sokoban pack/PNG/Character9.png")]

caminaAbajo = [pygame.image.load("assets/Sokoban pack/PNG/Character4.png"),
                pygame.image.load("assets/Sokoban pack/PNG/Character5.png"),
                pygame.image.load("assets/Sokoban pack/PNG/Character6.png")]

try:
    skin = pygame.image.load(skinfilename)
except pygame.error as msg:
    print('No se puede cargar la imagen')
    raise SystemExit(msg)

skin = skin.convert()

# Established the background color of the window as the element in the coordinates (0,0) of the skin file
screen.fill(skin.get_at((0, 0)))

## 4. Clock and keyboard setup
clock = pygame.time.Clock()
pygame.key.set_repeat(200, 50)  # set_repeat(delay in ms, interval in ms)


def update_screen():

    global walkCount
    global x

    # Clean the screen
    screen.fill(skin.get_at((0, 0)))

    # Contador de pasos
    if walkCount + 1 >= 3:
        walkCount = 0
    # Move to the left
    if left:
        screen.blit(caminaIzquierda[walkCount // 1], (int(px), int(py)))
        walkCount += 1
    # Move to the right
    elif rigth:
        screen.blit(caminaDerecha[walkCount // 1], (int(px), int(py)))
        walkCount += 1
    # Move up
    elif up:
        screen.blit(caminaArriba[walkCount // 1], (int(px), int(py)))
        walkCount += 1
    # Move down
    elif down:
        screen.blit(caminaAbajo[walkCount // 1], (int(px), int(py)))
        walkCount += 1
    else:
        screen.blit(quieto, (int(px), int(py)))        

## 5. MAIN GAME LOOP

while True:
    clock.tick(60)
    
    ## 6. Event handling
    for event in pygame.event.get():
        
        # Exit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard events
        elif event.type == KEYDOWN:

            # Move to the left
            if event.key == K_LEFT:
                left = True
                rigth = False
                up = False
                down = False
                px -= v

            # Move up
            elif event.key == K_UP:
                left = False
                rigth = False
                up = True
                down = False
                py -= v

            # Move to the rigth
            elif event.key == K_RIGHT:
                left = False
                rigth = True
                up = False
                down = False
                px += v

            # Move down
            elif event.key == K_DOWN:
                left = False
                rigth = False
                up = False
                down = True
                py += v

            # Undo operation
            elif event.key == K_BACKSPACE:
                pass

            # Redo operation
            elif event.key == K_SPACE:
                pass
            
            # No movement
            else:
                left = False
                rigth = False
                up = False
                down = False

    # 7. Update the screen
    pygame.display.update()
    update_screen()

    # 8. Window title
    pygame.display.set_caption('Sokoban')
