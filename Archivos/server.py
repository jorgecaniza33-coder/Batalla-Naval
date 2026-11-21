import socket
from game_logic import Conexion
PUERTO_POR_DEFECTO = 5000
def obtener_ip_local():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8",80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()
def iniciar_servidor(puerto=PUERTO_POR_DEFECTO, host="0.0.0.0"):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((host,puerto))
    servidor.listen(1)
    print (f"Servidor listo, envia al jugador 2 esta IP: {obtener_ip_local()} puerto: {puerto}")
    print ("ESPERANDO AL JUGADOR 2... Ctrl+C para cancelar")
    try:
        sock, direccion = servidor.accept()
    finally:
        servidor.close()
    print (f"Jugador 2 conectado desde: {direccion[0]}")
    return Conexion(sock)
