import pygame
import requests

def manejo_tecla_login(pantalla,teclado,url):
    if pantalla.momento_login == "usuario":
        pantalla.usuario = pantalla.manejo_texto(teclado, pantalla.usuario)
        if teclado == pygame.K_RETURN:
            pantalla.momento_login = "password"
    else:
        pantalla.password = pantalla.manejo_texto(teclado, pantalla.password)
        if teclado == pygame.K_RETURN:
            try:
                respuesta = requests.post(f"{url}/token", data={"username": pantalla.usuario, "password": pantalla.password})
                respuesta.raise_for_status()
                pantalla.token = {"Authorization": f"Bearer {respuesta.json()["access_token"]}"}
                pantalla.momento_login = "usuario"
                pantalla.usuario = ""
                pantalla.password = ""
                pantalla.etapa = "menu"
            except requests.RequestException as e:
                print("Error de autenticación:", e)
                pantalla.usuario = ""
                pantalla.password = ""
                pantalla.momento_login = "usuario"

def login(screen,color):
    """
    Se encarga de tomar el usuario y la contraseña.
    """
    text = screen.myFont.render("Ingrese su usuario", True, color)
    screen.screen.blit(text, (10, 10))
    input_text_surface = screen.myFont.render(screen.usuario, True, color)
    screen.screen.blit(input_text_surface, (10, 50))
    text2 = screen.myFont.render("Ingrese su contraseña", True, color)
    screen.screen.blit(text2, (10, 90))
    input_text_surface = screen.myFont.render(screen.password, True, color)
    screen.screen.blit(input_text_surface, (10, 130))