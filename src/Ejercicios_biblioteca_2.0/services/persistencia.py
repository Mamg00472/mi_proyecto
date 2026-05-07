import json
import os

def cargar_json(ruta):
    if not os.path.exists(ruta):
        return []
    
    with open(ruta, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def guardar_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)