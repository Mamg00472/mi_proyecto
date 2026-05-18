#!/usr/bin/env python3
"""
Demostración del agente Gemini en modo simulación
Muestra cómo funcionaría en una máquina con GUI
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from gemini_api import GeminiAPI
from skills.learning_system import LearningSystem
import json
import time

class SimulatedAgent:
    def __init__(self):
        self.gemini = GeminiAPI()
        self.learning = LearningSystem()
        self.mouse_pos = (960, 540)  # Centro de pantalla
        self.screen_width = 1920
        self.screen_height = 1080

    def simulate_action(self, action: dict) -> dict:
        """Simula la ejecución de una acción sin tocar el sistema"""
        action_type = action.get("action", "").lower()
        result = {"success": True, "message": "", "action": action_type}

        if action_type == "click":
            coords = action.get("coordinates", [])
            if coords:
                self.mouse_pos = (coords[0], coords[1])
                result["message"] = f"[SIM] Clic en ({coords[0]}, {coords[1]})"

        elif action_type == "move_mouse":
            coords = action.get("coordinates", [])
            if coords:
                # Coords pueden ser relativas o absolutas
                if coords[0] < 0 or coords[1] < 0:
                    # Relativa
                    new_x = max(0, min(self.screen_width, self.mouse_pos[0] + coords[0]))
                    new_y = max(0, min(self.screen_height, self.mouse_pos[1] + coords[1]))
                else:
                    # Absoluta
                    new_x = coords[0]
                    new_y = coords[1]
                self.mouse_pos = (new_x, new_y)
                result["message"] = f"[SIM] Ratón movido a ({new_x}, {new_y})"

        elif action_type == "type":
            text = action.get("text", "")
            result["message"] = f"[SIM] Escribiendo: {text[:30]}"

        elif action_type == "command":
            command = action.get("command", "")
            result["message"] = f"[SIM] Ejecutando: {command[:50]}"

        elif action_type == "press_key":
            key = action.get("key", "")
            result["message"] = f"[SIM] Presionando: {key}"

        elif action_type == "scroll":
            direction = action.get("direction", "down")
            result["message"] = f"[SIM] Scroll {direction}"

        return result

    def demo_instruction(self, instruction: str):
        """Demuestra cómo el agente procesa una instrucción"""
        print(f"\n{'='*60}")
        print(f"📝 Instrucción: {instruction}")
        print(f"{'='*60}")

        self.learning.session_attempts += 1

        # Obtener respuesta de Gemini
        print(f"⏳ Procesando con Gemini...", end=" ", flush=True)
        response = self.gemini.execute_command(instruction, None)
        print("✅")

        try:
            json_str = response.strip()
            if json_str.startswith("```"):
                json_str = json_str.split("```")[1]
                if json_str.startswith("json"):
                    json_str = json_str[4:]

            action = json.loads(json_str)

            print(f"\n📋 Acción decidida:")
            print(f"   Tipo: {action.get('action')}")
            print(f"   Descripción: {action.get('description')}")

            # Simular ejecución
            print(f"\n⚡ Ejecutando simulación:")
            result = self.simulate_action(action)
            print(f"   {result['message']}")

            if result['success']:
                self.learning.record_success(instruction, action)
                print(f"\n✅ Acción completada (SIMULADA)")

        except json.JSONDecodeError:
            print(f"⚠️  Respuesta no JSON: {response[:100]}")
        except Exception as e:
            print(f"❌ Error: {e}")

        self.learning.log_stats()

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🎬 DEMOSTRACIÓN DEL AGENTE GEMINI")
    print("="*60)
    print("Modo SIMULACIÓN - sin tocar el sistema real")
    print("="*60 + "\n")

    agent = SimulatedAgent()

    # Ejemplos de demostración
    ejemplos = [
        "mueve el ratón a la izquierda",
        "haz clic en el botón crear carpeta",
        "escribe 'prueba' en el campo de texto",
        "presiona enter para confirmar",
    ]

    for ejemplo in ejemplos:
        agent.demo_instruction(ejemplo)
        time.sleep(1)

    print(f"\n{'='*60}")
    print("✨ Demostración completada")
    print("="*60)
    print("\nNOTA: En una máquina con GUI, el agente ejecutaría")
    print("estas acciones de verdad (mouse real, clics, etc)")
    print("="*60 + "\n")
