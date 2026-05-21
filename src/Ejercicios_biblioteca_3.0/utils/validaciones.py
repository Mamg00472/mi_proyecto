import re

def validar_longitud_texto(texto: str, campo_nombre: str, minimo: int = 2, maximo: int = 50):
    # verificar que el texto no sea demasiado corto ni demasiado largo, y eliminar espacios innecesarios
    texto_limpio = texto.strip()
    if len(texto_limpio) < minimo or len(texto_limpio) > maximo:
        raise ValueError(f"El campo '{campo_nombre}' no es válido (debe tener entre {minimo} y {maximo} caracteres).")
    return texto_limpio

def validar_correo(correo: str) -> str:
    # Valida si el correo electrónico tiene un formato correcto (ejemplo@dominio.com)
    correo_limpio = correo.strip().lower()
    # Patrón para validar estructuras de email
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if not re.match(patron, correo_limpio):
        raise ValueError(f"El correo electrónico '{correo_limpio}' no tiene un formato válido.")
    return correo_limpio

def validar_anyo(anyo: int) -> int:
    # Asegura que el año del recurso sea coherente (no sea negativo ni en el futuro)
    from datetime import datetime
    anyo_actual = datetime.now().year
    
    if anyo < 0 or anyo > anyo_actual:
        raise ValueError(f"Año no válido. Debe estar entre 0 y {anyo_actual}.")
    return anyo