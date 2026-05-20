import json
import os

def cargar_json(ruta : str) -> list:
    # Verificar si el archivo existe antes de intentar cargarlo
    if not os.path.exists(ruta):
        return []
    
    # Intentar cargar el archivo JSON, manejando posibles errores de formato
    with open(ruta, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def guardar_json(ruta : str, datos : list):
    # asegura que el directorio exista antes de intentar guardar el archivo
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)