import random
from typing import Generator, List, Tuple

def bingo(n: int) -> Generator[Tuple[int, List[int], int], None, None]:
    """
    Generador de números para un juego de Bingo usando pop().

    Cada vez que se obtiene un número, se devuelve:
    - La bola que ha salido.
    - La lista acumulada de todas las bolas que han salido.
    - La cantidad de bolas que quedan en el bombo.

    Parameters
    ----------
    n : int
        Número de bolas en el bombo (ej: 75 o 90).

    Yields
    ------
    Tuple[int, List[int], int]
        - Número de la bola extraída.
        - Lista de todas las bolas que han salido hasta el momento.
        - Cantidad de bolas que quedan en el bombo.
    """
    bolas = list(range(1, n + 1))
    extraidas: List[int] = []

    while bolas:
        bola = bolas.pop(random.randrange(len(bolas)))  # elimina y devuelve una al azar
        extraidas.append(bola)
        yield bola, extraidas.copy(), len(bolas)
