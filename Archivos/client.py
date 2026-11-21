import socket
from game_logic import Conexion

PUERTO_POR_DEFECTO = 5000

def conectar(ip, puerto=PUERTO_POR_DEFECTO, tiempo_espera=10):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(tiempo_espera) #Espera 10 segundos, si no hay conexion cuelga.
    try:
        sock.connect((ip, puerto))
    except (OSError, socket.timeout) as error: #Si hay un error guarda que salio mal.
        print(f"No se pudo conectar a {ip}:{puerto} ({error})")
        sock.close() #Cuelga la conexion para no dejarlo abierto sin usar
        return 
    #Se ejecutan estas lineas de codigo, si es q la conexion fue exitosa
    sock.settimeout(None)  #Modo bloqueante durante la partida
    print(f"Conectado a {ip}:{puerto}")
    return Conexion(sock)
