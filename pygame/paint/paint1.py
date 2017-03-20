# Inizializzazione del motore grafico PyGame
import pygame
pygame.init()
clock = pygame.time.Clock()

# Definizione costanzi
NERO = (0, 0, 0)
VERDE = (0, 255, 0)
ROSSO = (255, 0, 0)
BIANCO = (255, 255, 255)
GRIGIO = (100, 100, 100)
SPESSORE_LINEA = 8
SPESSORE_PUNTO = 3
ALTEZZA = 600
LARGHEZZA = 800

# Creazione della finestra di pygame
pygame.display.set_caption("Pain Me")
area = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
area.fill(GRIGIO)

# Creazione della lavagna
lavagna = pygame.Surface((LARGHEZZA-30, ALTEZZA-30))
lavagna.fill(BIANCO)

# Inizializzazione cursore del mouse
mouse = pygame.mouse
mouse.set_visible(False)
colore_penna = NERO

# Ripeti fino a quando l'untente non esce e ad ogni iterazione
while True:
    # Gestore delle azioni dell'utente
    for evento in pygame.event.get():
        # Se l'utente clicca il bottone chiudi sulla finestra
        if evento.type == pygame.QUIT:
            exit()

    sinistro, centrale, destro = mouse.get_pressed()
    # Se l'utente clicca con il mouse all'interno della finestra di gioco
    if sinistro:
        # L'utente ha cliccato il bottone sinistro del mouse
        mouse_pos = mouse.get_pos()
        pygame.draw.circle(lavagna, colore_penna, mouse_pos, SPESSORE_PUNTO)

    area.fill(GRIGIO)
    # Disegno la lavagna all'interno dell'area
    area.blit(lavagna, (0, 0))
    # Disegno il puntatore del mouse con il colore selezionato
    pygame.draw.circle(area, colore_penna, (mouse.get_pos()), SPESSORE_PUNTO)

    # Aggiorna lo schermo con tutto quello che è stato disegnato
    pygame.display.flip()
    clock.tick(60)
