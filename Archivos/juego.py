from game_logic import (
    Tablero, Seguimiento, CPU,
    parsear_coordenada, nombre_coordenada, mostrar_tableros,
)

def pedir_disparo(seguimiento):
    # Pide en dónde realizar el disparo
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

def jugar_local():
    # Prepara la partida (tableros y barcos de manera aleatoria)
    tu_flota = Tablero()
    tu_flota.colocar_flota_aleatoria()
    rival = Tablero()
    rival.colocar_flota_aleatoria()
    mis_disparos = Seguimiento()
    cpu = CPU()

    while True:
        mostrar_tableros(tu_flota, mis_disparos)

        # Tu turno
        fila, col = pedir_disparo(mis_disparos)
        resultado, barco = rival.recibir_disparo(fila, col)
        mis_disparos.registrar(fila, col, resultado)
        print("Resultado:", resultado)
        if rival.flota_hundida():
            print("¡Ganaste!")
            break

        # Turno de la CPU
        f, c = cpu.elegir()
        resultado, barco = tu_flota.recibir_disparo(f, c)
        cpu.informar(f, c, resultado)
        print("La CPU disparó a", nombre_coordenada(f, c), "->", resultado)
        if tu_flota.flota_hundida():
            print("Perdiste")
            break

def menu():
    while True:
        print("""
1) Modo Local: Vs CPU
2) Modo Red: Vs Jugador
3) Salir
""")
        resp = input("Elige una opción: ").strip().lower()
        if resp in ("1", "1)", "uno"):
            print("=== MODO LOCAL ===")
            jugar_local()
        elif resp in ("2", "2)", "dos"):
            print("El modo en red estará disponible próximamente.")
        elif resp in ("3", "3)", "tres", "salir"):
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, elige 1, 2 o 3")


if __name__ == "__main__":
    menu()
