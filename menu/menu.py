import pygame
from opciones.menuOpciones import *

def manejo_tecla_menu(pantalla, teclado, url):
    """
    Se encarga de los input para el menu, para redirigir
    """
    pantalla.input_texto = pantalla.manejo_texto(teclado, pantalla.input_texto)
    if teclado == pygame.K_RETURN:
        if pantalla.input_texto == "0":
            pantalla.etapa = "login"
            pantalla.input_texto = ""
        else:
            opciones(pantalla.input_texto, url, pantalla)
            pantalla.input_texto = ""

def menu(pantalla, color):
    menu_options = [
        "1) Ver archivo json",
        "2) Ver categorías",
        "3) Buscar premio",
        "4) Agregar premio",
        "5) Actualizar laureate",
        "6) Actualizar categoría",
        "7) Eliminar Premio",
        "0) Salir"
    ]
    
    y = 10
    
    for texto in menu_options:
        text = pantalla.myFont.render(texto, True, color)
        pantalla.screen.blit(text, (10, y))
        y += 40
    
    input_text_surface = pantalla.myFont.render(pantalla.input_texto, True, color)
    pantalla.screen.blit(input_text_surface, (10, y))