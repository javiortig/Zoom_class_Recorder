import pyautogui as ui
import time
from datetime import datetime

MINIMIZE_POS = (1802, 13) 
START_OBS_TEMP = (1194, 520)
OPEN_CHROME = (612, 1058)
OPEN_OBS = (664, 1058)
JOIN_SESSION = (286, 810)
SALA_CURSO = (286, 859)


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

def unirse_sala():
    _clickPosition(JOIN_SESSION[0], JOIN_SESSION[1])
    _clickPosition(SALA_CURSO[0], SALA_CURSO[1])

def _clickPosition(x, y, mouseSpeed = 0.5, delay = 2):
    ui.moveTo(x, y, duration = mouseSpeed)
    ui.click(button='left')
    time.sleep(delay)

def grabar():
    abrir_obs()
    iniciar_temporizador_obs()
    abrir_chrome()
    unirse_sala()

def askAndWait():
    x = int(input("A que hora:"))
    date = datetime.now()
    date = date.replace(hour=x)

    while date > datetime.now():
        time.sleep(1)

def prueba():
    abrir_chrome()
    unirse_sala()
    minimizar()
    abrir_chrome()


# Main starts here
imprimir_recordatorio()
askAndWait()
grabar()


