import socket
from game_logic import Conexion

PUERTO_POR_DEFECTO = 5000

def conectar(ip, puerto=PUERTO_POR_DEFECTO, tiempo_espera=10):
    """Devuelve una Conexion, o None si no se pudo conectar."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(tiempo_espera) #espera 10 segundos, si no hay conexion cuelga.
    try:
        sock.connect((ip, puerto))
    except (OSError, socket.timeout) as error: #si hay un error guarda que salio mal.
        print(f"No se pudo conectar a {ip}:{puerto} ({error})")
        sock.close() # Cuelga la conexion para no dejarlo abierto sin usar
        return 

#se ejecutan estas lineas de codigo, si es q la conexion fue exitosa

    sock.settimeout(None)  # modo bloqueante durante la partida
    print(f"Conectado a {ip}:{puerto}")
    return Conexion(sock)
