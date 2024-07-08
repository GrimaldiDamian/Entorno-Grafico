def render_text(surface, text, position, font, color=(255, 255, 255)):
    """
    En esta funcion se encarga, de transformar los texto, en un formato adecuado, y en una posicion (x,y)
    """
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)