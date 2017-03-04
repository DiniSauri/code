import pygame
import random
# grandezza area gioco
x_max = 600 
y_max = 500

# variabili per palla
p_x = 300
p_y = 300
p_raggio = 30
p_r = 200 # red
p_g = 200 # green 
p_b = 200 # blue
p_velx = 3
p_vely = 3
# variabili per barra
b_x = 300       # coordinata x della barra
b_y = 450       # coordinata y della barra
b2_x = 300      # coordinata x della barra g2
b2_y = 50 - 20       # coordinata y della barra g2
b_l = 80        # lunghezza della barra
b_spessore = 20 # spessore della barra 

pygame.init()
area = pygame.display.set_mode((x_max, y_max))

# per generare più eventi KEYDOWM (delay, interval)
pygame.key.set_repeat(1, 10)

perso = False 
while not perso:
    
    area.fill((0,0,0))
    palla = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x, p_y), p_raggio, 0)
    barra = pygame.draw.rect(area, (255, 255, 255), (b_x, b_y,b_l,b_spessore))
    barra2 = pygame.draw.rect(area, (255, 255, 255), (b2_x, b2_y,b_l,b_spessore))
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit() # usciamo dal gioco
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT: #pressione freccia SX
                b_x -= 10
            if evento.key == pygame.K_RIGHT:# pression freccia DX
                b_x += 10
            if evento.key == pygame.K_a: #pressione A
                b2_x -= 10
            if evento.key == pygame.K_s:# pressione S
                b2_x += 10
             
    if p_x > x_max - p_raggio:  # tocca bordo DX
        p_velx = -5 
    elif p_x < p_raggio :       # tocca bordo SX
        p_velx = 5 
    elif p_y < p_raggio:        # tocca bordo SUPERIORE
        perso = True
    elif p_y > y_max - p_raggio:# tocca bordo INFERIORE
        perso = True
    
    # collisione della palla con la barra 
    if palla.colliderect(barra) or palla.colliderect(barra2):
        p_vely = - p_vely
        
    p_x += p_velx
    p_y += p_vely
        
    pygame.display.update()
    pygame.time.wait(20)

print("Hai perso !!")
pygame.quit()


