import pygame
import requests
from opciones.resetear_variables import *
from opciones.texto import *

def opcion6(pantalla,color):
    render_text(pantalla.screen,"Ingrese el anio",(10,10),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.anio,(10,40),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese la categoria que quieres cambiar",(10,70),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.categorias_anterior,(10,100),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese la categoria",(10,130),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.categoria,(10,160),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.respuesta,(10,190),pantalla.myFont,color)

def op6(pantalla,url):
    try:
        respuesta = requests.put(f"{url}/Actualizar_Categoria",headers=pantalla.token, params={"year": pantalla.anio, "categoria_Anterior": pantalla.categorias_anterior, "categoria_Nueva": pantalla.categoria})
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
    elif pantalla.momentos_opciones == "categoria anterior":
        pantalla.categorias_anterior = pantalla.manejo_texto(teclado, pantalla.categorias_anterior)
        if teclado == pygame.K_RETURN:
            pantalla.momentos_opciones = "categoria"
    else:
        pantalla.categoria = pantalla.manejo_texto(teclado, pantalla.categoria)
        if teclado == pygame.K_RETURN:
            op6(pantalla,url)