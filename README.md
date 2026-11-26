# Batalla Naval

Juego de Batalla Naval en Python que se juega en la terminal. Esta primera entrega (Fase 3) incluye el **modo local** (jugador contra la CPU). El modo en red (servidor y cliente por sockets TCP) y la interfaz gráfica están previstos para la siguiente etapa (1 de diciembre).

**Equipo:** César Alcocer, Víctor Páez y José Cañizares.

## Estado del proyecto

| Parte | Estado |
|---|---|
| Lógica del juego (`game_logic.py`) | Lista |
| Modo local contra la CPU (`juego.py`) | Lista |
| Modo en red (`server.py`, `client.py`) | Lista |
| Interfaz gráfica | Pendiente (1 de diciembre) |
| Emoji de fuego al dañar un barco | Pendiente (pedido de un profesor) |
| Sonidos: agua al fallar, explosión o golpe metálico al acertar | Pendiente (pedido de un profesor) |

## Cómo ejecutarlo

Requiere Python 3.6 o superior. No hay que instalar nada extra.

```
python Archivos/juego.py
```

## Cómo se juega

- Cada jugador tiene una flota de 5 barcos colocada al azar: Portaaviones (5 casillas), Acorazado (4), Crucero (3), Submarino (3) y Destructor (2).
- En tu turno escribes una coordenada: **letra de la fila (A a J) y número de la columna (1 a 10)**, por ejemplo `B5`.
- El tablero de la izquierda es tu flota y el de la derecha son tus disparos.
- Símbolos: `~` agua, `B` barco, `X` tocado, `O` disparo al agua.
- Gana quien hunda primero toda la flota del rival.

## Estructura del repositorio

```
ProyectoJuego/
| Archivos/
  | game_logic.py     Reglas del juego (tableros, disparos, CPU, conexión)
  | juego.py          Juego en la terminal (modo local)
  | server.py         Servidor del modo en red (pendiente)
  | client.py         Cliente del modo en red (pendiente)
| pruebas/          Pruebas de cada parte de game_logic.py
  | game_logic.py
  | pruebas_batalla_naval.zip (Contiene 13 pruebas del código)
| BITACORA_CONFLICTOS.md       Bitácora de gestión de conflictos
| LICENSE
| README.md
```

## Declaración de autoría

| Archivo | Autor(es) |
|---|---|
| `game_logic.py` | José Cañizares, con la ayuda de Claude |
| `juego.py` | José Cañizares, con la ayuda de Claude |
| `server.py` y `client.py` | César Alcocer |
| Diagrama arquitectónico | César Alcocer |
| `interfaz.py` | Víctor Paez |
| Diagramas funcionales | Víctor Paez |
| README, LICENSE, bitácora | Todos |

## Licencia

Este proyecto se distribuye bajo la licencia **MIT** (ver el archivo `LICENSE`).

## Librerías utilizadas y sus licencias

Por ahora solo se usa la biblioteca estándar de Python, distribuida bajo la licencia de la Python Software Foundation (PSF License).

| Librería | Para qué se usa |
|---|---|
| `random` | Colocar la flota al azar y barajar los disparos de la CPU |
| `json` | Convertir los mensajes de red a texto y de vuelta |
| `socket` | Conexión TCP del modo en red |

Si en la siguiente etapa se agrega alguna librería externa (por ejemplo, para los sonidos o la interfaz), se anotará aquí con su licencia.

## Créditos

**Código de terceros:** la versión de referencia de `game_logic.py` fue generada por partes con ayuda de Claude. El equipo decidió generarla con IA porque aún no se habían enseñado en clase las herramientas necesarias para hacerlo.

**Uso de inteligencia artificial:** se usó Claude (Anthropic) en este proyecto para:

- Explicar su funcionamiento y guiar su reescritura en lecciones paso a paso, en las que Claude propuso los fragmentos de código y José Cañizares los escribió, probó y ajustó.
- Uso de `sockets` para la creación de `server.py` y `client.py`

**Decisiones del equipo:** el equipo decidió usar IA para la creación del juego, y decidió incorporar los cambios pedidos por un profesor (emoji de fuego al dañar un barco y sonidos al disparar).
**Recursos visuales y de audio:** ninguno por ahora (el juego es de texto).

## Bitácora de gestión de conflictos

Ver `BITACORA_CONFLICTOS.md`.
