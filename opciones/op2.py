from opciones.texto import *

def VerCategorias(pantalla,color: tuple[int,int,int]):
    """
    Se encarga de mostrar la opcion 2.
    Se espera recibir como parametros, el objeto que se encarga de manejar la pantalla, y un color, RGB.
    """
    y_offset = 10
    for categorias in pantalla.categoria:
        render_text(pantalla.screen, categorias, (10, y_offset), pantalla.myFont,color)
        y_offset += 40  # Incrementar el offset para la siguiente línea de texto