# Batalla Naval (Python)

Juego de Batalla Naval en tablero de 10x10. El menú y la conexión de red (IP y puerto) se manejan por **terminal**, y la partida se juega en una **ventana gráfica** (tkinter) donde cada jugador coloca sus barcos con el mouse y dispara haciendo clic.

Modos de juego: **local** (contra la CPU) y **en red** (Jugador 1 vs Jugador 2 por TCP).

## Equipo
 | Victor Páez |
 | Cesar Alcocer |
 | José Cañizares |

## Estructura del proyecto
|- juego.py        #Punto de entrada: menú por terminal (modo local o en red)
|- server.py       #Socket servidor TCP del Jugador 1
|- client.py       #Conexión del Jugador 2 mediante IP y puerto
|- game_logic.py   #Tableros 10x10, validación de barcos/disparos, CPU y protocolo de red
|- interfaz.py     #Ventana gráfica (tkinter): colocación de barcos y batalla
|- Diagramas/           #Diagramas actualizados (UML, flujo, etc.)
|- BITACORA_CONFLICTOS.md
|- LICENSE
|- README.md

## Requisitos y ejecución

- Python 3.8 o superior con `tkinter` (viene incluido en Python para Windows y Mac).
- En Linux (Debian/Ubuntu) puede faltar: `sudo apt install python3-tk`.
- No hay que instalar librerías externas.

```bash
python juego.py
```

**Modo en red (dos computadoras en la misma red):**

1. El Jugador 1 elige la opción 2 en la terminal. El programa muestra su IP y el puerto (por defecto 5000).
2. El Jugador 2 elige la opción 3 e ingresa esa IP y el puerto.
3. Al conectarse, se abre la ventana del juego en ambas computadoras.

Para probar en una sola computadora, usa dos terminales y la IP por ejemplo`127.0.0.1`. Si el firewall bloquea la conexión, hay que permitir Python en el puerto elegido.

## Cómo se juega

1. **Colocar barcos:** haz clic en tu tablero para colocar cada barco (Portaaviones 5, Acorazado 4, Crucero 3, Submarino 3, Destructor 2). Con `R` o clic derecho lo rotas; "Deshacer" quita el último y "Al azar" coloca toda la flota. Al terminar, pulsa "¡Listo!".
2. **Batalla:** cuando ambos jugadores están listos, se dispara haciendo clic en el tablero de la derecha. El Jugador 1 empieza y los turnos se alternan.
3. **Símbolos:** casilla roja con X = tocado, punto blanco = agua.
4. Gana quien hunda primero toda la flota rival.

## Declaración de Autoría

Este proyecto fue diseñado y desarrollado como parte de la asignatura Logica de Programación, en la UIDE (Universidad Internacional del Ecuador). El código fuente es de autoría propia del equipo. Cuando se utilice material de terceros (ideas, fragmentos de código, documentación, herramientas de IA), se indicará aquí con su fuente y alcance:

Se usó un asistente de IA como apoyo para la estructura del código; el equipo revisó, probó y adaptó el resultado.

## Licenciamiento Open Source

El código de este repositorio se distribuye bajo la **licencia MIT** (ver archivo [LICENSE](LICENSE)). Esto permite usar, copiar, modificar y distribuir el software, siempre que se conserve el aviso de copyright y la licencia.

### Librerías utilizadas y sus licencias

Todas son parte de la biblioteca estándar de Python.

| Librería | Uso en el proyecto | Licencia |
|---|---|---|
| `tkinter` | Ventana gráfica y clics del mouse (`interfaz.py`) | PSF License |
| `socket` | Comunicación TCP entre jugadores (`server.py`, `client.py`) | PSF License |
| `threading`, `queue` | Escuchar la red sin congelar la ventana (`interfaz.py`) | PSF License |
| `json` | Formato de los mensajes de red | PSF License |
| `random` | Colocación aleatoria de barcos de la CPU | PSF License |
| `string` | Letras de las filas del tablero | PSF License |
| `Claude` | Ayuda en la estructuración del código y solución de problemas generales, se usó Claude (Anthropic) para entender y explicar el código de game_logic.py.

Python se distribuye bajo la [PSF License](https://docs.python.org/3/license.html), una licencia permisiva compatible con la licencia MIT. El proyecto no depende de librerías externas.
