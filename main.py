import pygame
import sys
from pantalla.pantalla import Pantalla

pygame.init()

ancho = 1280
alto = 720

running = True
screen = Pantalla(ancho,alto)
pygame.display.set_caption("Cliente Api")
reloj = pygame.time.Clock()

def manejar_eventos():
    """
    Manejo de eventos.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            screen.manejar_tecla(event.key)

def actualizar_pantalla():
    """
    Se encarga del funcionamiento de lo que se ve en pantalla
    """
    
    screen.dibujar()
    
    pygame.display.flip()

def interfaz_grafica():
    """
    Bucle principal de la interfaz grafica.
    """
    while running:
        
        manejar_eventos()
        
        reloj.tick(60)
        
        actualizar_pantalla()

interfaz_grafica()