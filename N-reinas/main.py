import sys
from problema import juego

def main():
    print('Selecciona el tamaño de tu tablero:')
    tablero = int(input('>>'))
    if len(sys.argv) > 1:
        tablero = int(sys.argv[1])
    juego(tablero)