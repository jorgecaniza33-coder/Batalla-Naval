import server
import client
from game_logic import (
    Tablero, Seguimiento, CPU,
    parsear_coordenada, nombre_coordenada, mostrar_tableros,
)
print("juego.py cargó bien")
#Verifica que la comunicacion de archivos funcione

def pedir_disparo(seguimiento):
    while True:
        texto = input("Tu disparo (ej. B5): ")
        coord = parsear_coordenada(texto)
        if coord is None:
            print("Coordenada inválida, intenta otra vez")
            continue
        fila, col = coord
        if seguimiento.ya_disparado(fila, col):
            print("Ya disparaste ahí, elige otra casilla")
            continue
        return fila, col
#Pide en donde realizar el disparo

def jugar_local():
    tu_flota = Tablero()
    tu_flota.colocar_flota_aleatoria()
    rival = Tablero()
    rival.colocar_flota_aleatoria()
    mis_disparos = Seguimiento()
    cpu = CPU()
#Prepara la partida (Tableros, y barcos de manera aleatoria)

    while True:
        mostrar_tableros(tu_flota, mis_disparos)
        #Tu Turno
        fila, col = pedir_disparo(mis_disparos)
        resultado, barco = rival.recibir_disparo(fila, col)
        mis_disparos.registrar(fila, col, resultado)
        print("Resultado:", resultado)
        if rival.flota_hundida():
            print("¡Ganaste!")
            break
        #Turno de la CPU
        f, c = cpu.elegir()
        resultado, barco = tu_flota.recibir_disparo(f, c)
        cpu.informar(f, c, resultado)
        print("La CPU disparó a", nombre_coordenada(f, c), "->", resultado)
        if tu_flota.flota_hundida():
            print("Perdiste")
            break

if __name__ == "__main__":
    jugar_local()
#Corre el juego
