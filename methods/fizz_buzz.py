from typing import List, Union

def fizzbuzz(n: int = 100) -> List[Union[int, str]]:
    """
    Genera la secuencia FizzBuzz desde 1 hasta n.

    La secuencia sigue las reglas:
    - Si el número es múltiplo de 3: se escribe "Fizz".
    - Si el número es múltiplo de 5: se escribe "Buzz".
    - Si el número es múltiplo de 3 y 5: se escribe "FizzBuzz".
    - En caso contrario: se escribe el número original.

    Parameters
    ----------
    n : int, optional
        Número máximo hasta el cual generar la secuencia (por defecto 100).

    Returns
    -------
    List[Union[int, str]]
        Lista con los valores de la secuencia FizzBuzz.

    Examples
    --------
    >>> fizzbuzz(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
    """
    result: List[Union[int, str]] = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result
