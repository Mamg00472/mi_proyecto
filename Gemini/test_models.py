#!/usr/bin/env python3
"""
Prueba varios modelos de Gemini para encontrar cuál tiene cuota disponible
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from config import GEMINI_API_KEY
import google.genai as genai

MODELOS_A_PROBAR = [
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b",
    "gemini-1.5-pro",
]

def probar_modelo(modelo: str) -> bool:
    """Intenta conectar con un modelo específico"""
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        print(f"  ⏳ Probando {modelo}...", end=" ", flush=True)

        response = client.models.generate_content(
            model=modelo,
            contents="OK"
        )

        print(f"✅ FUNCIONA")
        return True

    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            print(f"❌ Cuota agotada")
        elif "404" in error_msg or "not found" in error_msg.lower():
            print(f"❌ No disponible")
        elif "permission" in error_msg.lower():
            print(f"❌ Sin permiso")
        else:
            print(f"❌ Error: {error_msg[:50]}")
        return False

if __name__ == "__main__":
    if not GEMINI_API_KEY:
        print("❌ ERROR: GEMINI_API_KEY no configurada")
        sys.exit(1)

    print("\n" + "="*60)
    print("🧪 PROBANDO MODELOS DE GEMINI")
    print("="*60 + "\n")

    modelo_funcionando = None

    for modelo in MODELOS_A_PROBAR:
        if probar_modelo(modelo):
            modelo_funcionando = modelo
            break

    print("\n" + "="*60)
    if modelo_funcionando:
        print(f"✅ MODELO FUNCIONANDO: {modelo_funcionando}")
        print("\nActualiza config.py con:")
        print(f'   MODEL_NAME = "{modelo_funcionando}"')
    else:
        print("❌ Ningún modelo tiene cuota disponible en este momento")
        print("\nOpciones:")
        print("  1. Espera a que se reinicie la cuota")
        print("  2. Agrega un método de pago en Google AI Studio")
        print("  3. Prueba más tarde")
    print("="*60 + "\n")
