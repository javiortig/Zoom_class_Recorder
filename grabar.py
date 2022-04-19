from enum import Enum
import pyautogui as ui
import time
from datetime import datetime


MINIMIZE_POS = (1802, 13) 
START_OBS_TEMP = (1194, 520)
OPEN_CHROME = (612, 1058)
OPEN_OBS = (664, 1058)
JOIN_SESSION_MAIS = (286, 810)
SALA_CURSO_MAIS = (286, 859)
JOIN_SESSION_DB = (276, 886)
SALA_CURSO_DB = (261, 941)

class Clases(Enum):
    ANALISIS = 1
    DB = 2



def imprimir_recordatorio():
    print("Asegurate que tienes el zoom del Chrome a 150%, abierto en el BB con scroll arriba")
    print("El obs esta abierto con la ventana del temporizador")

def minimizar():
    _clickPosition(MINIMIZE_POS[0], MINIMIZE_POS[1])

def iniciar_temporizador_obs():
    _clickPosition(START_OBS_TEMP[0], START_OBS_TEMP[1])

def abrir_chrome():
    _clickPosition(OPEN_CHROME[0], OPEN_CHROME[1])

def abrir_obs():
    _clickPosition(OPEN_OBS[0], OPEN_OBS[1])

def unirse_sala(clase):
    if(clase == 1):
        _clickPosition(JOIN_SESSION_MAIS[0], JOIN_SESSION_MAIS[1])
        _clickPosition(SALA_CURSO_MAIS[0], SALA_CURSO_MAIS[1])
    elif(clase == 2):
        _clickPosition(JOIN_SESSION_DB[0], JOIN_SESSION_DB[1])
        _clickPosition(SALA_CURSO_DB[0], SALA_CURSO_DB[1])
    else:
        print("Error eligiendo la clase")
        quit()

def _clickPosition(x, y, mouseSpeed = 0.5, delay = 2):
    ui.moveTo(x, y, duration = mouseSpeed)
    ui.click(button='left')
    time.sleep(delay)

def grabar(clase):
    abrir_obs()
    iniciar_temporizador_obs()
    abrir_chrome()
    unirse_sala(clase)

def askAndWait()-> int:
    x = int(input("A que hora:"))
    clase = int(input("Elige clase: 1)analisis, 2) Bases de Datos "))
    date = datetime.now()
    date = date.replace(minute=0).replace(hour=x)
    print("Se iniciara a las: ", end='')
    print(date)
    while date > datetime.now():
        time.sleep(60)

    return clase

def _askPrueba()-> int:
    print("PROBANDO")
    x = int(input("A que minuto:"))
    clase = int(input("Elige clase: 1)analisis, 2) Bases de Datos "))
    date = datetime.now()
    date = date.replace(minute=x).replace(second=0)
    print("Se iniciara a las: ", end='')
    print(date)
    while date > datetime.now():
        time.sleep(10)

    return clase

def _imprimirPosRaton(delay = 4):
    while True:
        time.sleep(delay)
        print(ui.position())

def prueba():
    imprimir_recordatorio()
    clase = _askPrueba()
    grabar(clase)
    quit()

def rutina():
    imprimir_recordatorio()
    clase = askAndWait()
    grabar(clase)
    quit()

# Main starts here
rutina()

