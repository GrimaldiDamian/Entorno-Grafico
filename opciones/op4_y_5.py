import pygame
import requests
from clase.clases import *
from opciones.texto import *
from opciones.resetear_variables import *

def opcion4(pantalla,color):
    """
    Se encarga de mostrar tanto el resultado, como el texto en pantalla.
    """
    render_text(pantalla.screen,"Ingrese el anio",(10,10),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.anio,(10,40),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese la categoria",(10,70),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.categoria,(10,100),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese la cantidad de share",(10,130),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.share,(10,160),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese la id",(10,190),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.id,(10,210),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese su nombre",(10,240),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.firstname,(10,270),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese su apellido",(10,300),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.surname,(10,330),pantalla.myFont, color)
    render_text(pantalla.screen,"Ingrese su motivacion",(10,360),pantalla.myFont, color)
    render_text(pantalla.screen,pantalla.motivation,(10,390),pantalla.myFont, color)
    
    if pantalla.etapa in ["menu 4", "opcion 4"]:
        render_text(pantalla.screen,"Si posee alguna otra motivacion ingreselo, sino presione enter",(10,420),pantalla.myFont, color)
        render_text(pantalla.screen,pantalla.overallMotivation,(10,450),pantalla.myFont, color)
    if isinstance(pantalla.respuesta, dict):
        render_text(pantalla.screen,pantalla.respuesta["mensaje"],(pantalla.ancho/2 - 100,480),pantalla.myFont,color)
    else:
        render_text(pantalla.screen,pantalla.respuesta,(10,480),pantalla.myFont,color)

def agregarLaureate(pantalla,teclado):
    """
    Se encarga de cargar los datos para laureate, que es utilizar tanto la opcion 4 y 5
    """
    if pantalla.momento_carga == "id":
        pantalla.id = pantalla.manejo_texto(teclado, pantalla.id)
        if teclado == pygame.K_RETURN:
            pantalla.momento_carga = "firstname"
    elif pantalla.momento_carga == "firstname":
        pantalla.firstname = pantalla.manejo_texto(teclado, pantalla.firstname)
        if teclado == pygame.K_RETURN:
            pantalla.momento_carga = "surname"
    elif pantalla.momento_carga == "surname":
        pantalla.surname = pantalla.manejo_texto(teclado, pantalla.surname)
        if teclado == pygame.K_RETURN:
            pantalla.momento_carga = "motivation"
    elif pantalla.momento_carga == "motivation":
        pantalla.motivation = pantalla.manejo_texto(teclado, pantalla.motivation)
        if teclado == pygame.K_RETURN:
            laureates = Laureate(id=int(pantalla.id), firstname=pantalla.firstname, surname=pantalla.surname, motivation=pantalla.motivation, share=int(pantalla.share))
            pantalla.laureate.append(laureates)
            if len(pantalla.laureate) == int(pantalla.share):
                pantalla.momentos_opciones = "overallMotivation" if pantalla.etapa == "menu 4" else "opcion_5"
            pantalla.id, pantalla.firstname, pantalla.surname, pantalla.motivation = "", "", "", ""
            pantalla.momento_carga = "id"

    return pantalla.laureate

def manejo_tecla_op4 (pantalla,teclado,url):
    """
    Se encarga de manejar el teclado, para la opcion 4 y 5
    """
    if pantalla.momentos_opciones == "anio":
        pantalla.anio = pantalla.manejo_texto(teclado, pantalla.anio)
        if teclado == pygame.K_RETURN:
            pantalla.momentos_opciones = "categoria"
    elif pantalla.momentos_opciones == "categoria":
        pantalla.categoria = pantalla.manejo_texto(teclado, pantalla.categoria)
        if teclado == pygame.K_RETURN:
            pantalla.momentos_opciones = "share"
    elif pantalla.momentos_opciones == "share":
        pantalla.share = pantalla.manejo_texto(teclado, pantalla.share)
        if teclado == pygame.K_RETURN:
            pantalla.momentos_opciones = "laureates"
    elif pantalla.momentos_opciones == "laureates":
        pantalla.laureate = agregarLaureate(pantalla,teclado)
    elif pantalla.momentos_opciones == "overallMotivation":
        pantalla.overallMotivation = pantalla.manejo_texto(teclado,pantalla.overallMotivation)
        if teclado == pygame.K_RETURN:
            pantalla.overallMotivation = pantalla.overallMotivation if pantalla.overallMotivation != "none" else None
            try:
                premio = Premio(anio = int(pantalla.anio),categoria = pantalla.categoria,laureate = pantalla.laureate,overallMotivation = pantalla.overallMotivation)
                pantalla.premio = premio.convertirDict()
                respuesta = requests.post(f"{url}/Agregar_Premio",headers=pantalla.token, json = pantalla.premio)
                respuesta.raise_for_status()
                pantalla.respuesta = respuesta.json()
                pantalla.etapa = "opcion 4"
            except requests.RequestException as e:
                resetear_variables(pantalla)
                pantalla.momentos_opciones = "anio"
                print ("Error en la opcion 4")
    elif pantalla.momentos_opciones == "opcion_5":
        try:
            premio = Premio(anio = int(pantalla.anio),categoria = pantalla.categoria,laureate = pantalla.laureate,overallMotivation = pantalla.overallMotivation)
            pantalla.premio = premio.convertirDict()
            respuesta = requests.put(f"{url}/Actualizar_Laureate",headers=pantalla.token, json = pantalla.premio)
            respuesta.raise_for_status()
            pantalla.respuesta = respuesta.json()
            pantalla.etapa = "opcion 5"
        except requests.RequestException as e:
            resetear_variables(pantalla)
            pantalla.momentos_opciones = "anio"
            print ("Error en la opcion 5")