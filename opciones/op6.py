import pygame
import requests
from .resetear_variables import *
from .texto import *

def opcion6(pantalla,color):
    render_text(pantalla.screen,"Ingrese el anio",(10,10),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.anio,(10,40),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese la categoria que quieres cambiar",(10,70),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.categoria_anterior,(10,100),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese la categoria",(10,130),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.categoria,(10,160),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.respuesta,(10,190),pantalla.myFont,color)

def op6(pantalla,url):
    try:
        respuesta = requests.put(f"{url}/Actualizar_Laureate",headers=pantalla.token, params={"year": pantalla.year, "categoria_Anterior": pantalla.categoria, "categoria_Nueva": pantalla.categoriaNueva})
        respuesta.raise_for_status()
        pantalla.respuesta = respuesta.json()
        pantalla.etapa = "opcion 6"
    except requests.RequestException as e:
        resetear_variables(pantalla)
        pantalla.momentos_opciones = "anio"
        print ("Error en la opcion 6")

def manejo_teclado_op6(pantalla,teclado,url):
    """
    manejo de teclado, para ingresar las datos para la opcion 6
    """
    if pantalla.momentos_opciones == "anio":
        pantalla.anio = pantalla.manejo_texto(teclado, pantalla.anio)
        if teclado == pygame.K_RETURN:
            pantalla.momentos_opciones = "categoria anterior"
    elif pantalla.momentos_opciones == "categoria anterio":
        pantalla.categoria_anterio = pantalla.manejo_texto(teclado, pantalla.categoria_anterior)
        if teclado == pygame.K_RETURN:
            pantalla.momentos_opciones = "categoria"
    else:
        pantalla.categoria = pantalla.manejo_texto(teclado, pantalla.categoria)
        if teclado == pygame.K_RETURN:
            op6(pantalla,url)