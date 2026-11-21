import random
import json
import socket
# Se importan herramientas necesarias para la funcion y conexion del juego

TAMANO = 10 # Tamñaño del tablero
FLOTA = [
    ("Portaaviones",5),("Acorazado",4),
    ("Crucero",3), ("Submarino",3), ("Destructor",2),
]
LETRAS = "ABCDEFGHIJ"
AGUA = "~"
BARCO = "B"
TOCADO = "X"
FALLO = "O" 
R_AGUA = "agua"
R_TOCADO = "tocado"
R_HUNDIDO = "hundido"
R_REPETIDO = "repetido"
R_INVALIDO = "invalido"
# Los valores que se usaran dentro del juego

def dentro_del_tablero(fila, col):
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
    if not dentro_del_tablero(fila, col):
        return None
    return fila, col

def nombre_coordenada(fila, col):
    return LETRAS[fila] + str(col + 1)
# Ayuda a que el codigo no se rompa con entradas ambiguas como: "Hola" o "H89"

class Tablero:
    def __init__(self):
        self.celdas = []
        for f in range(TAMANO):
            fila = []
            for c in range(TAMANO):
                fila.append(AGUA)
            self.celdas.append(fila)
        self.barcos = {}
        self.disparos_recibidos = set()
# Las listas, diccionarios que guardaran las posiciones de los barcos
    
    def _coordenadas(self, fila, col, largo, horizontal):
        coords = []
        for i in range(largo):
            if horizontal:
                coords.append((fila, col + i))
            else:
                coords.append((fila + i, col))
        return coords
    # Calcula todas las casillas que va a ocupar el barco
    
    def puede_colocar(self, fila, col, largo, horizontal):
        coords = self._coordenadas(fila, col, largo, horizontal)
        for f, c in coords:
            if not dentro_del_tablero(f, c):
                return False
            if self.celdas[f][c] != AGUA:
                return False
        return True
    # Verifica todas las casillas si estan vacias devuelve True si falla una no se podra
    
    def colocar_barco(self, nombre, fila, col, largo, horizontal):
        if nombre in self.barcos:
            return False
        if not self.puede_colocar(fila, col, largo, horizontal):
            return False
        coords = self._coordenadas(fila, col, largo, horizontal)
        for f, c in coords:
            self.celdas[f][c] = BARCO
        self.barcos[nombre] = set(coords)
        return True
    # Pone todo el barco si es que devuelve True
    
    def colocar_flota_aleatoria(self):
        self.__init__()
        for nombre, largo in FLOTA:
            while True:
                fila = random.randrange(TAMANO)
                col = random.randrange(TAMANO)
                horizontal = random.choice([True, False])
                if self.colocar_barco(nombre, fila, col, largo, horizontal):
                    break
    # Aleatorizacion para poner los barcos
    
    def flota_completa(self):
        return len(self.barcos) == len(FLOTA)
    # Verifica si todos los barcos han sido puestos
    
    def quitar_barco(self, nombre):
        coords = self.barcos.pop(nombre, None)
        if coords is None:
            return False
        for f, c in coords:
            self.celdas[f][c] = AGUA
        return True
    # Quita el barco del tablero y devuelve True si se pudo quitar
    
    def recibir_disparo(self, fila, col):
        if not dentro_del_tablero(fila, col):
            return R_INVALIDO, None
        if (fila, col) in self.disparos_recibidos:
            return R_REPETIDO, None
        self.disparos_recibidos.add((fila, col))
        if self.celdas[fila][col] == BARCO:
            self.celdas[fila][col] = TOCADO
            for nombre, restantes in self.barcos.items():
                if (fila, col) in restantes:
                    restantes.discard((fila, col))
                    if len(restantes) == 0:
                        return R_HUNDIDO, nombre
                    return R_TOCADO, nombre    
    # Devuelve el estado del disparo y el barco si fue tocado o hundido
        
        self.celdas[fila][col] = FALLO
        return R_AGUA, None
    
    def flota_hundida(self):
        for restantes in self.barcos.values():
            if len(restantes) > 0:
                return False
        return len(self.barcos) > 0
    # Verifica si todos los barcos se han hundido y devuelve True si es asi

class Seguimiento:
    def __init__(self):
        self.celdas = []
        for f in range(TAMANO):
            fila = []
            for c in range(TAMANO):
                fila.append(AGUA)
            self.celdas.append(fila)
    
    def ya_disparado(self, fila, col):
        return self.celdas[fila][col] != AGUA
    
    def registrar(self, fila, col, resultado):
        if resultado == R_AGUA:
            self.celdas[fila][col] = FALLO
        else:
            self.celdas[fila][col] = TOCADO
# Ayuda a ver las casillas usadas

class CPU:
    def __init__(self):
        self.disponibles = []
        for f in range(TAMANO):
            for c in range(TAMANO):
                self.disponibles.append((f, c))
        random.shuffle(self.disponibles)
        self.objetivos = []
    
    def elegir(self):
        while len(self.objetivos) > 0:
            f, c = self.objetivos.pop()
            if (f, c) in self.disponibles:
                self.disponibles.remove((f, c))
                return f, c
        return self.disponibles.pop()
    
    def informar(self, fila, col, resultado):
        if resultado == R_TOCADO:
            for df, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                vecino = (fila + df, col + dc)
                if vecino in self.disponibles:
                    self.objetivos.append(vecino)

mi_tablero = Tablero()
rival_tablero  = Tablero()
# Ayuda a crear la tabla individual para cada jugador

def mostrar_tableros(propio, seguimiento):
    cabecera = "   "
    
    for i in range(1, TAMANO + 1):
        cabecera = cabecera + f"{i:>2} "
    print()
    print("TU FLOTA".ljust(35) + "TUS DISPAROS")
    print(cabecera + "  " + cabecera)
    
    for f in range(TAMANO):
        izq = ""
        der = ""
        for c in range(TAMANO):
            izq = izq + f"{propio.celdas[f][c]:>2} "
            der = der + f"{seguimiento.celdas[f][c]:>2} "
        lado_izq = f" {LETRAS[f]} " + izq
        lado_der = f" {LETRAS[f]} " + der
        print(lado_izq + "  " + lado_der)
    print()

class Conexion:
    
    def __init__(self, sock):
        self.sock = sock
        self._lector = sock.makefile("r", encoding="utf-8")
    
    def enviar(self, mensaje):
        datos = json.dumps(mensaje) + "\n"
        self.sock.sendall(datos.encode("utf-8"))
    
    def recibir(self):
        try:
            linea = self._lector.readline()
        except (OSError, ValueError):
            return None
        if not linea:
            return None
        return json.loads(linea)
    
    def cerrar(self):
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        try:
            self._lector.close()
            self.sock.close()
        except OSError:
            pass

def jugar_local():
    tu_flota = Tablero()
    tu_flota.colocar_flota_aleatoria()
    rival = Tablero()
    rival.colocar_flota_aleatoria()
    mis_disparos = Seguimiento()
    cpu = CPU()
