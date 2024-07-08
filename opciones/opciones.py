import pygame
import requests
from clase.clases import *

def manejo_teclado_opciones(pantalla, teclado):
    """
    Esta funcion se encargar de volver al menu
    """
    if teclado == pygame.K_BACKSPACE:
        opciones.resetear_variables(pantalla)
        pantalla.etapa = "menu"

def opciones(texto, url, pantalla):
    """
    Dependiendo de la opcion, se encarga de llamar las correspondientes opciones.
    """
    if texto == "1":
        try:
            respuesta = requests.get(f'{url}/Leer_Archivo', headers=pantalla.token)
            respuesta.raise_for_status()
            pantalla.archivo_json = respuesta.json()
            pantalla.etapa = "opcion 1"
            print(pantalla.archivo_json)
        except requests.RequestException as e:
            print("Error al obtener el archivo:", e)
    elif texto == "2":
        try:
            respuesta  = requests.get(f'{url}/Categorias',headers=pantalla.token)
            respuesta.raise_for_status()
            pantalla.categoria = respuesta.json()
            pantalla.etapa = "opcion 2"
            print(pantalla.categoria)
        except requests.RequestException as e:
            print("Error al obtener las categorias:", e)
    elif texto == "3":
        pantalla.momentos_opciones = "anio"
        pantalla.etapa = "menu 3"
    elif texto == "4":
        pantalla.momentos_opciones = "anio"
        pantalla.etapa = "menu 4" 
    elif texto == "5":
        pantalla.momentos_opciones = "anio"
        pantalla.etapa = "menu 5"
    elif texto == "6":
        pantalla.etapa = "menu 6"
    elif texto == "7":
        pantalla.etapa = "menu 7"