import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME
import json
from typing import Optional

class GeminiAPI:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(MODEL_NAME)
        self.conversation_history = []

    def analyze_screenshot(self, image_path: str, instruction: str) -> str:
        """Analiza una captura de pantalla con una instrucción usando visión"""
        try:
            image_file = genai.upload_file(image_path)

            response = self.model.generate_content([
                instruction,
                image_file
            ])

            return response.text
        except Exception as e:
            return f"Error analizando imagen: {str(e)}"

    def execute_command(self, instruction: str, screenshot: Optional[str] = None) -> str:
        """Envía una instrucción a Gemini para ejecutar una acción"""
        try:
            if screenshot:
                image_file = genai.upload_file(screenshot)
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

                response = self.model.generate_content([
                    prompt,
                    image_file
                ])
            else:
                response = self.model.generate_content(instruction)

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
