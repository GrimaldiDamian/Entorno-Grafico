import pygame
import requests
from clase.clases import *

def render_text(surface, text, position, font, color=(255, 255, 255)):
    """
    En esta funcion se encarga, de transformar los texto, en un formato adecuado, y en una posicion (x,y)
    """
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

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
                respuesta = requests.get(f'{url}/Buscar_Premio',headers={"Authorization": f"Bearer {pantalla.token}"}, params={"year":pantalla.anio,"category":pantalla.categoria})
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

def resetear_variables(pantalla):
    """
    Se encarga de limpiar todas las variables que son utilizadas, para la hora de volver a entrar a una opcion, siempre esten limpias.
    """
    pantalla.anio = ""
    pantalla.categoria = ""
    pantalla.respuesta = ""
    pantalla.id = ""
    pantalla.laureate = []
    pantalla.firstname = ""
    pantalla.motivation = ""
    pantalla.overallMotivation = ""
    pantalla.share = ""
    pantalla.surname = ""

def verArchivo(pantalla, color):
    """
    Dibuja el contenido del archivo JSON en pantalla.
    """
    y_offset = 20
    for diccionario in pantalla.archivo_json["prizes"]:
        for key,values in diccionario.items():
            text = f"{key}: {values}"
            render_text(pantalla.screen, text, (20, y_offset), pantalla.myFont,color)
            y_offset += 40  # Incrementar el offset para la siguiente línea de texto

def VerCategorias(pantalla,color: tuple[int,int,int]):
    """
    Se encarga de mostrar la opcion 2.
    Se espera recibir como parametros, el objeto que se encarga de manejar la pantalla, y un color, RGB.
    """
    y_offset = 10
    for categorias in pantalla.categoria:
        render_text(pantalla.screen, categorias, (10, y_offset), pantalla.myFont,color)
        y_offset += 40  # Incrementar el offset para la siguiente línea de texto

def BuscarPremio(pantalla,color):
    """
    Se encarga de mostrar el resultado correctos de la opcion 3.
    """
    y_inicial = 10
    for text in pantalla.premio:
        render_text(pantalla.screen, text, (20, y_inicial), pantalla.myFont,color)
        y_inicial += 30

def manejo_teclado_opciones(pantalla, teclado):
    """
    Esta funcion se encargar de volver al menu
    """
    if teclado == pygame.K_BACKSPACE:
        resetear_variables(pantalla)
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