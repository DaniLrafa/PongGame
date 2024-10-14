import pygame
pygame.init()
import sys

x = 230

#colores
#
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREY = (65,65,65)

#player size
PH = 140
PW = 20
#pantalla 
#
sw = 800
sh = 600
screen_size = (sw,sh)

#cordenadas del jugador y velocidad
#
P1X = 40
P1Y = 250
SP1Y = 0

P2X = 720
P2Y = 250
SP2Y = 0

#pelota pocision y velocidad
#
BALLX = 400
BALLY = 300
SBALLX = float(3)
SBALLY = float(3)

#definir los fps
#
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #P1
            #
            if event.key == pygame.K_w:
                SP1Y = -5
            if event.key == pygame.K_s:
                SP1Y = 5
            #P2
            #
            if event.key == pygame.K_UP:
                SP2Y = -5
            if event.key == pygame.K_DOWN:
                SP2Y = 5
            #reinicio
            #
            if event.key == pygame.K_r:
                BALLX = 400
                BALLY = 300
                P1X = 40
                P1Y = 250
                P2X = 720
                P2Y = 250
                SBALLX = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                SP1Y = 0
            if event.key == pygame.K_s:
                SP1Y = 0
            if event.key == pygame.K_UP:
                SP2Y = 0
            if event.key == pygame.K_DOWN:
                SP2Y = 0

    #Limitamos movimiento
    #P1
    #
    if P1Y < 0:  
        P1Y = 0
    if P1Y + PH > sh: 
        P1Y = sh - PH

    #P2
    #
    if P2Y < 0:  
        P2Y = 0
    if P2Y + PH > sh: 
        P2Y = sh - PH

    #Rebote
    #
    if BALLY > 580 or BALLY < 0:
        SBALLY *= -1
    P1Y += SP1Y
    P2Y += SP2Y
    BALLX += SBALLX
    BALLY += SBALLY

    #Texto
    #
    txt = pygame.font.Font(None, 100)
    S1 = 0
    S2 = 0
    if BALLX > 800:
        S1 += 1
    if BALLX < 0:
        S2 += 1
    screen.fill(BLACK)  
    p1score = txt.render(f"{S1}", True, GREY)
    screen.blit(p1score, (300, 100))  
    p2score = txt.render(f"{S2}", True, GREY)
    screen.blit(p2score, (500, 100)) 
    if BALLX > 800 or BALLX < 0:
        txtr = pygame.font.Font(None, 25)
        rematch = txtr.render("PRESS (R) TO PLAY AGAIN", True, WHITE)
        screen.blit(rematch, (300,300))

    #------------Dibujito
    BALL = pygame.draw.rect(screen,WHITE,(BALLX,BALLY,20,20))
    P1 = pygame.draw.rect(screen,WHITE,(P1X,P1Y,PW,PH))
    P2 = pygame.draw.rect(screen,WHITE,(P2X,P2Y,PW,PH))
    pygame.draw.rect(screen,GREY,(390,120,60,10))
    #------------Dibujito
    
    #colision
    #
    if BALL.colliderect(P1) or BALL.colliderect(P2):
        SBALLX *= -1.2
        if abs(SBALLX) >= 15:
            SBALLX *= 0.8
    

    #actualizar
    #
    pygame.display.flip()
    clock.tick(60)
    pass

