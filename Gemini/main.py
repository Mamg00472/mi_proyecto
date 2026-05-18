#!/usr/bin/env python3
"""
AGENTE GEMINI - Control de Computadora con IA
Replica la funcionalidad del video: "Le di un Cuerpo Virtual a Gemini"

Este agente puede:
- 📸 Capturar pantalla y analizar con visión
- 🖱️ Controlar mouse y teclado
- 🎤 Escuchar y procesar comandos de voz
- 💬 Recibir instrucciones por texto
- ⌨️ Ejecutar comandos del sistema
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from agent import GeminiAgent
from config import GEMINI_API_KEY
import warnings

warnings.filterwarnings("ignore")

def main():
    if not GEMINI_API_KEY:
        print("❌ ERROR: GEMINI_API_KEY no configurada")
        print("\n📝 Pasos para configurar:")
        print("1. Crea un archivo .env en la carpeta Gemini")
        print("2. Agrega: GEMINI_API_KEY=tu_clave_api")
        print("3. Obtén tu clave en: https://aistudio.google.com/app/apikeys")
        sys.exit(1)

    print("\n" + "="*60)
    print("🤖 INICIANDO AGENTE GEMINI")
    print("="*60)
    print("Módulos cargados:")
    print("  ✓ API Gemini")
    print("  ✓ Control de Desktop")
    print("  ✓ Procesamiento de Voz")
    print("  ✓ Procesamiento de Texto")
    print("="*60 + "\n")

    agent = GeminiAgent()
    agent.run()

if __name__ == "__main__":
    main()
