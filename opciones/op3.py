import pygame
import requests
from opciones.texto import *

def BuscarPremio(pantalla,color):
    """
    Se encarga de mostrar el resultado correctos de la opcion 3.
    """
    y_inicial = 10
    for text in pantalla.premio:
        render_text(pantalla.screen, text, (20, y_inicial), pantalla.myFont,color)
        y_inicial += 30

def opcion3 (screen,color):
    """
    acompañada del manejo de teclas, para esta opcion, se encarga de mostrar en pantalla lo que se esta cargando
    """
    render_text(screen.screen,"Ingrese el anio",(10,10),screen.myFont, color)
    render_text(screen.screen,screen.anio,(10,50),screen.myFont, color)
    render_text(screen.screen,"Ingrese la categoria",(10,90),screen.myFont, color)
    render_text(screen.screen,screen.categoria,(10,130),screen.myFont, color)

def manejo_tecla_opcion3(pantalla,teclado,url):
    """
    En esta funcion se utiliza para el manejo la opcion 3, para la carga de los datos
    """
    if pantalla.momentos_opciones == "anio":
        pantalla.anio = pantalla.manejo_texto(teclado, pantalla.anio)
        if teclado == pygame.K_RETURN:
            pantalla.momentos_opciones = "categoria"
    else:
        pantalla.categoria = pantalla.manejo_texto(teclado, pantalla.categoria)
        if teclado == pygame.K_RETURN:
            try:
                respuesta = requests.get(f'{url}/Buscar_Premio',headers=pantalla.token, params={"year":pantalla.anio,"category":pantalla.categoria})
                respuesta.raise_for_status()
                pantalla.premio = respuesta.json()
                pantalla.anio = ""
                pantalla.categoria = ""
                pantalla.etapa = "opcion 3"
            except requests.RequestException as e:
                print("Error")
                pantalla.anio = ""
                pantalla.categoria = ""
                pantalla.momentos_opciones = "anio"