import pygame
import requests
import sys
from login.login import *
from menu.menu import *
from opciones import *

url = "http://localhost:8000"

class Pantalla():
    def __init__(self, ancho, alto) -> None:
        self.screen = pygame.display.set_mode((ancho, alto))
        self.ancho = ancho
        self.alto = alto
        self.fondo = ""
        self.dict_imagen = {1: "login/login.png", 2: "menu/menu.png", 3:"opciones/opciones.png"}
        self.color = (242, 250, 1)
        self.myFont = pygame.font.SysFont('Times New Roman', 25)
        self.token = ""
        self.input_texto = ""
        
        #login
        
        self.etapa = "login"
        self.usuario = ""
        self.password = ""
        self.momento_login = "usuario"
        
        self.momentos_opciones = "anio"
        self.momento_carga ="id"
        self.archivo_json = ""
        
        # variables utilizadas paras los put, post, delete y una para el get
        
        self.categoria = ""
        self.anio = ""
        self.categorias_anterior = ""
        self.share = ""
        self.id = ""
        self.firstname = ""
        self.surname = ""
        self.premio = ""
        self.motivation = ""
        self.overallMotivation = ""
        self.laureate = []
        
        self.respuesta = ""
        
        self.reemplazo = {
            "[0]": "0", "[1]": "1", "[2]": "2", "[3]": "3", "[4]": "4",
            "[5]": "5", "[6]": "6", "[7]": "7", "[8]": "8", "[9]": "9",
            "[+]": "+"
        }

    def fondo_imagen(self, opcion):
        self.fondo = pygame.image.load(self.dict_imagen[opcion])
        self.fondo = pygame.transform.scale(self.fondo, (self.ancho, self.alto))

    def manejo_texto(self, key, texto):
        key_name = pygame.key.name(key)
        if key == pygame.K_RETURN or key == pygame.K_KP_ENTER:
            return texto
        elif key == pygame.K_BACKSPACE:
            texto = texto[:-1]
        elif key == pygame.K_SPACE:
            texto += " "
        elif key_name in self.reemplazo:
            texto += self.reemplazo[key_name]
        else:
            texto += key_name
        return texto

    def manejar_tecla(self, key):
        if self.etapa == "login":
            manejo_tecla_login(self, key, url)
        elif self.etapa == "menu":
            manejo_tecla_menu(self, key, url)
        elif self.etapa == "menu 3":
            op3.manejo_tecla_opcion3(self,key, url)
        elif self.etapa in ["menu 4", "menu 5", "menu 7"]:
            op4_y_5.manejo_tecla_op4(self,key,url)
        elif self.etapa == "menu 6":
            op6.manejo_teclado_op6(self,key,url)
        else:
            manejo_teclado_opciones(self,key)

    def dibujar(self):
        if self.etapa == "login":
            self.fondo_imagen(1)
            self.screen.blit(self.fondo, (0, 0))
            login(self, self.color)
        elif self.etapa == "menu":
            self.fondo_imagen(2)
            self.screen.blit(self.fondo, (0, 0))
            menu(self, self.color)
        elif self.etapa in ["opcion 1", "opcion 2", "opcion 3", "opcion 4","opcion 5","opcion 6", "opcion 7", "menu 3", "menu 4", "menu 5", "menu 6", "menu 7"]:
            self.fondo_imagen(3)
            self.screen.blit(self.fondo, (0, 0))
            if self.etapa == "opcion 1":
                op1.verArchivo(self, self.color)
            if self.etapa == "opcion 2":
                op2.VerCategorias(self,self.color)
            if self.etapa == "menu 3":
                op3.opcion3(self,self.color)
            if self.etapa == "opcion 3":
                op3.BuscarPremio(self,self.color)
            if self.etapa in ["menu 4", "opcion 4", "menu 5", "opcion 5","menu 7", "opcion 7"]:
                op4_y_5.opcion4(self,self.color)
            if self.etapa in ["menu 6", "opcion 6"]:
                op6.opcion6(self,self.color)