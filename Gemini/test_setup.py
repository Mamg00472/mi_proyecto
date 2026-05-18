#!/usr/bin/env python3
"""
Script de prueba para verificar la configuración de Gemini
Ejecuta antes de usar el agente completo
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from config import GEMINI_API_KEY, HAS_DISPLAY
import google.genai as genai

def test_gemini_connection():
    print("\n" + "="*60)
    print("🧪 PRUEBA DE CONEXIÓN CON GEMINI")
    print("="*60 + "\n")

    if not GEMINI_API_KEY:
        print("❌ ERROR: GEMINI_API_KEY no configurada")
        print("   Asegúrate de crear .env con tu clave API")
        return False

    try:
        print("⏳ Conectando con Gemini...")
        genai.configure(api_key=GEMINI_API_KEY)
        client = genai.Client()

        print("⏳ Enviando prueba de mensaje...")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Eres un asistente de desktop automation. Responde solo 'OK' para confirmar que funcionas correctamente."
        )

        if response.text:
            print(f"\n✓ Conexión exitosa!")
            print(f"✓ Respuesta de Gemini: {response.text}\n")
            return True
        else:
            print("❌ Respuesta vacía de Gemini")
            return False

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\nPosibles problemas:")
        print("  - API Key inválida")
        print("  - Sin conexión a Internet")
        print("  - Límite de cuota alcanzado")
        return False

def test_display():
    print("\n" + "="*60)
    print("🖥️  VERIFICANDO DISPLAY")
    print("="*60 + "\n")

    if HAS_DISPLAY:
        print("✓ Display gráfico disponible")
        return True
    else:
        print("⚠️  Sin display gráfico (headless)")
        print("   Se usará display virtual para screenshots")
        return True

def test_imports():
    print("\n" + "="*60)
    print("📦 VERIFICANDO DEPENDENCIAS")
    print("="*60 + "\n")

    modules = {
        "google.genai": "Google Generative AI",
        "pyautogui": "PyAutoGUI",
        "PIL": "Pillow",
        "speech_recognition": "Speech Recognition",
        "pyttsx3": "pyttsx3",
    }

    all_ok = True
    for module, name in modules.items():
        try:
            __import__(module)
            print(f"✓ {name}")
        except ImportError:
            print(f"❌ {name} (falta instalar)")
            all_ok = False

    return all_ok

if __name__ == "__main__":
    print("\n🚀 Iniciando pruebas del agente Gemini...\n")

    deps_ok = test_imports()
    display_ok = test_display()
    gemini_ok = test_gemini_connection()

    print("="*60)
    print("RESULTADO")
    print("="*60)

    if deps_ok and gemini_ok:
        print("✓ ¡Todo está configurado correctamente!")
        print("  Puedes ejecutar: python main.py")
    elif deps_ok:
        print("⚠️  Faltan instalar algunas dependencias")
        print("   Ejecuta: pip install -r requirements.txt")
    else:
        print("❌ Hay problemas que resolver antes de usar el agente")

    print("="*60 + "\n")

    sys.exit(0 if (deps_ok and gemini_ok) else 1)
