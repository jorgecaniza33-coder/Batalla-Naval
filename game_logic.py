TAMANO = 10 
# Tamñaño del tablero
LETRAS = "ABCDEFGHIJ"
AGUA = "~"
BARCO = "B"
TOQUE= "X"
FALLO = "O" 
# Los valores que se usaran dentro del juego
# def se usa para definir una funcion que se usara cuando se desee
def dentro_tablero(fila, col):
    return 0 <= fila < TAMANO and 0 <= col < TAMANO
# Esta parte ayuda a ver si la casilla seleccionada existe
def parsear_coordenada(texto):
    texto = texto.strip().upper()

    if len(texto) < 2:
        return None

    letra = texto[0]
    numero = texto[1:]

    if letra not in LETRAS:
        return None
    if not numero.isdigit():
        return None

    fila = LETRAS.index(letra)
    col = int(numero) - 1

    if not dentro_tablero(fila, col):
        return None

    return fila, col
