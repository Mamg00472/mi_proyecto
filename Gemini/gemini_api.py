import google.genai as genai
from config import GEMINI_API_KEY, MODEL_NAME
import json
import os
from typing import Optional

class GeminiAPI:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.conversation_history = []

    def analyze_screenshot(self, image_path: str, instruction: str) -> str:
        """Analiza una captura de pantalla con una instrucción usando visión"""
        try:
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=[
                    instruction,
                    {"type": "image", "data": image_data}
                ]
            )

            return response.text
        except Exception as e:
            return f"Error analizando imagen: {str(e)}"

    def execute_command(self, instruction: str, screenshot: Optional[str] = None) -> str:
        """Envía una instrucción a Gemini para ejecutar una acción"""
        try:
            if screenshot and os.path.exists(screenshot):
                with open(screenshot, "rb") as image_file:
                    image_data = image_file.read()

                prompt = f"""Eres un asistente de IA experto en automatizar acciones en computadoras.

INSTRUCCIÓN DEL USUARIO: {instruction}

Analizando la captura de pantalla adjunta, debes proporcionar la SIGUIENTE ACCIÓN que debes ejecutar.

IMPORTANTE: Siempre responde en FORMATO JSON válido, sin texto adicional.

Responde ÚNICAMENTE con este JSON:
{{
    "action": "click|type|press_key|command|scroll|move_mouse",
    "description": "Descripción clara de qué hará esta acción",
    "coordinates": [x, y],
    "text": "texto a escribir (si aplica)",
    "key": "nombre de tecla o combinación (ctrl+c, enter, etc)",
    "command": "comando del sistema (si aplica)",
    "direction": "up|down|left|right"
}}

EJEMPLOS:
- Para hacer clic: {{"action": "click", "description": "Clic en el botón crear", "coordinates": [145, 320]}}
- Para escribir: {{"action": "type", "description": "Escribir nombre", "text": "Nueva Carpeta"}}
- Para presionar tecla: {{"action": "press_key", "description": "Enter para confirmar", "key": "enter"}}
- Para comando: {{"action": "command", "description": "Crear carpeta prueba", "command": "mkdir ~/Desktop/prueba"}}
- Para mover mouse: {{"action": "move_mouse", "description": "Mover ratón a icono", "coordinates": [500, 300]}}

Responde SOLO el JSON, nada más."""

                response = self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=[
                        prompt,
                        {"type": "image", "data": image_data}
                    ]
                )
            else:
                prompt = f"""Eres un asistente de IA experto en automatizar acciones en computadoras.

INSTRUCCIÓN DEL USUARIO: {instruction}

Sin captura de pantalla disponible, debes proporcionar una ACCIÓN inicial para comenzar.

IMPORTANTE: Siempre responde en FORMATO JSON válido, sin texto adicional.

Responde ÚNICAMENTE con este JSON:
{{
    "action": "click|type|press_key|command|scroll|move_mouse",
    "description": "Descripción clara de qué hará esta acción",
    "coordinates": [x, y],
    "text": "texto a escribir (si aplica)",
    "key": "nombre de tecla o combinación",
    "command": "comando del sistema (si aplica)"
}}

Responde SOLO el JSON, nada más."""

                response = self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

            self.conversation_history.append({
                "role": "user",
                "content": instruction
            })
            self.conversation_history.append({
                "role": "assistant",
                "content": response.text
            })

            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

    def clear_history(self):
        self.conversation_history = []
