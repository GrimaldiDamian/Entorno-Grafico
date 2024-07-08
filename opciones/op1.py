from opciones.texto import *

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