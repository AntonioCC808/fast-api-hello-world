from typing import Literal

def cleanemail(email: str) -> str:
    """
    Normaliza direcciones de email con reglas específicas para Gmail.

    Reglas aplicadas:
    - En direcciones de Gmail, los puntos en el nombre de usuario se ignoran.
    - En direcciones de Gmail, si aparece un '+', todo lo que esté entre el '+' y el '@' se elimina.
    - En otros dominios (ej: hotmail, yahoo, etc.), no se aplica ninguna regla especial.
    - Todas las direcciones se devuelven en minúsculas.

    Parameters
    ----------
    email : str
        Dirección de correo a normalizar.

    Returns
    -------
    str
        Dirección de correo normalizada.

    Examples
    --------
    >>> cleanemail('the.A.team@hotmail.com')
    'the.a.team@hotmail.com'

    >>> cleanemail('the.A.team@gmail.com')
    'theateam@gmail.com'

    >>> cleanemail('the.A.team+anibal.smith@gmail.com')
    'theateam@gmail.com'

    >>> cleanemail('theateam@yahoo.es')
    'theateam@yahoo.es'
    """
    email = email.strip().lower()
    local, _, domain = email.partition("@")

    if domain == "gmail.com":
        # Ignorar todo lo que esté después de '+'
        if "+" in local:
            local = local.split("+", 1)[0]
        # Eliminar puntos
        local = local.replace(".", "")

    return f"{local}@{domain}"