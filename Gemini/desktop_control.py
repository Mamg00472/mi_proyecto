import pyautogui
from PIL import ImageGrab
import subprocess
import time
import json
import os
from config import SCREENSHOT_DIR
from datetime import datetime

class DesktopControl:
    def __init__(self):
        pyautogui.FAILSAFE = True
        self.last_screenshot = None

    def take_screenshot(self) -> str:
        """Captura la pantalla y la guarda"""
        try:
            screenshot = ImageGrab.grab()
            filename = f"{SCREENSHOT_DIR}/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(filename)
            self.last_screenshot = filename
            return filename
        except Exception as e:
            print(f"Error tomando screenshot: {e}")
            return None

    def click(self, x: int, y: int, button: str = "left") -> bool:
        """Hace clic en las coordenadas especificadas"""
        try:
            pyautogui.click(x, y, button=button)
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error haciendo clic: {e}")
            return False

    def type_text(self, text: str, interval: float = 0.05) -> bool:
        """Escribe el texto especificado"""
        try:
            pyautogui.typewrite(text, interval=interval)
            time.sleep(0.3)
            return True
        except Exception as e:
            print(f"Error escribiendo: {e}")
            return False

    def write(self, text: str) -> bool:
        """Escribe usando el clipboard (mejor para texto complejo)"""
        try:
            import pyperclip
            pyperclip.copy(text)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            return True
        except:
            return self.type_text(text)

    def press_key(self, key: str) -> bool:
        """Presiona una tecla o combinación"""
        try:
            if '+' in key:
                keys = key.split('+')
                pyautogui.hotkey(*keys)
            else:
                pyautogui.press(key)
            time.sleep(0.3)
            return True
        except Exception as e:
            print(f"Error presionando tecla: {e}")
            return False

    def scroll(self, x: int, y: int, clicks: int = 5, direction: str = "down") -> bool:
        """Desplaza la página en la dirección especificada"""
        try:
            pyautogui.moveTo(x, y)
            if direction == "up":
                clicks = -clicks
            pyautogui.scroll(clicks)
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error haciendo scroll: {e}")
            return False

    def execute_command(self, command: str) -> str:
        """Ejecuta un comando del sistema"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            return f"Output: {result.stdout}\nErrors: {result.stderr}"
        except subprocess.TimeoutExpired:
            return "Comando agotó el tiempo de espera"
        except Exception as e:
            return f"Error ejecutando comando: {str(e)}"

    def parse_and_execute_action(self, action_json: str) -> dict:
        """Parsea una acción JSON y la ejecuta"""
        try:
            action = json.loads(action_json)

            action_type = action.get("action", "").lower()
            result = {"success": False, "message": ""}

            if action_type == "click":
                coords = action.get("coordinates", [])
                if coords and len(coords) == 2:
                    success = self.click(int(coords[0]), int(coords[1]))
                    result["success"] = success
                    result["message"] = "Clic ejecutado" if success else "Error en clic"

            elif action_type == "type":
                text = action.get("text", "")
                if text:
                    success = self.write(text)
                    result["success"] = success
                    result["message"] = "Texto escrito" if success else "Error escribiendo"

            elif action_type == "command":
                command = action.get("command", "")
                if command:
                    output = self.execute_command(command)
                    result["success"] = True
                    result["message"] = output

            elif action_type == "scroll":
                coords = action.get("coordinates", [])
                direction = action.get("direction", "down")
                if coords and len(coords) == 2:
                    success = self.scroll(int(coords[0]), int(coords[1]), direction=direction)
                    result["success"] = success
                    result["message"] = "Scroll ejecutado" if success else "Error en scroll"

            elif action_type == "key":
                key = action.get("key", "")
                if key:
                    success = self.press_key(key)
                    result["success"] = success
                    result["message"] = "Tecla presionada" if success else "Error presionando tecla"

            return result

        except json.JSONDecodeError:
            return {"success": False, "message": f"JSON inválido: {action_json}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}
