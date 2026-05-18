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

                prompt = f"""Eres un asistente de IA que puede controlar una computadora.

Instrucción: {instruction}

Basándote en la captura de pantalla adjunta, proporciona:
1. El próximo paso a ejecutar (describiendo exactamente qué hacer)
2. Las coordenadas aproximadas si necesitas hacer clic (format: x,y)
3. Cualquier texto que necesites escribir

Responde en JSON con este formato:
{{
    "action": "click|type|command|scroll",
    "description": "descripción de la acción",
    "coordinates": [x, y],
    "text": "texto a escribir si aplica",
    "command": "comando a ejecutar si es comando del sistema"
}}"""

                response = self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=[
                        prompt,
                        {"type": "image", "data": image_data}
                    ]
                )
            else:
                response = self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=instruction
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
