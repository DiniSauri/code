import pygame
import random

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
b_x = 300       # coordinata x della barra g1
b_y = 450       # coordinata y della barra g1
b2_x = 300       # coordinata x della barra g2
b2_y = 50       # coordinata y della barra g2
b_l = 80        # lunghezza della barra
b_spessore = 20 # spessore della barra 

pygame.init()

area = pygame.display.set_mode((x_max, y_max))
perso = False 
while not perso:
    
    area.fill((0,0,0))
    palla = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x, p_y), p_raggio, 0)
    barra = pygame.draw.line(area, (255, 255, 255), (b_x, b_y), (b_x+b_l, b_y), b_spessore)
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit() # usciamo dal gioco
             
    if p_x > x_max - p_raggio:
        p_velx = -5 #random.randrange(-5, 0)
    elif p_x < p_raggio :
        p_velx = 5 #random.randrange(3, 10)
    elif p_y < p_raggio:
        p_vely = 5 #random.randrange(3, 10)
    elif p_y > y_max - p_raggio:
        p_vely = - 5      
    
    p_x += p_velx
    p_y += p_vely
        
    pygame.display.update()
    pygame.time.wait(20)

print("Hai perso !!")
pygame.quit()


