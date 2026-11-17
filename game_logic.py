TAMAÑO = 10 
# Tamñaño del tablero

LETRAS = "ABCDEFGHIJ"
AGUA = "~"
BARCO = "B"
TOQUE= "X"
FALLO = "O" 
# Los valores que se usaran dentro del juego

# def se usa para definir una funcion que se usara cuando se desee
def tablero(fila, col):
    return 0 <= fila < TAMAÑO and 0 <= col < TAMAÑO
# Esta parte ayuda a ver si la casilla seleccionada existe
def coordenada_dada(texto):
    letra = texto[0]
    numero = texto[1:]
    fila = LETRAS.index(letra)
    col = int(numero) - 1
    return fila,col
#