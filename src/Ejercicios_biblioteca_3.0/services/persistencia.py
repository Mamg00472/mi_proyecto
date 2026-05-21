import json
import os

# Calculamos de forma dinámica dónde está la raíz del ejercicio (la carpeta Ejercicio_biblioteca_3.0)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def obtener_ruta_absoluta(ruta_relativa: str) -> str:
    """Convierte una ruta relativa tipo 'data/archivo.json' en una ruta absoluta dentro del ejercicio."""
    return os.path.join(BASE_DIR, ruta_relativa)

def cargar_json(ruta: str) -> list:
    ruta_absoluta = obtener_ruta_absoluta(ruta)
    if not os.path.exists(ruta_absoluta):
        return []
    
    with open(ruta_absoluta, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def guardar_json(ruta: str, datos: list):
    ruta_absoluta = obtener_ruta_absoluta(ruta)
    # Nos aseguramos de que la carpeta interna 'data/' exista
    os.makedirs(os.path.dirname(ruta_absoluta), exist_ok=True)
    
    with open(ruta_absoluta, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)