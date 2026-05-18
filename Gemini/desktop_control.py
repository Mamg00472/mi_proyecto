import subprocess
import time
import json
import os
from config import SCREENSHOT_DIR, HAS_DISPLAY, USE_VIRTUAL_DISPLAY
from datetime import datetime

try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except Exception as e:
    PYAUTOGUI_AVAILABLE = False

try:
    from PIL import ImageGrab
except Exception:
    ImageGrab = None

if USE_VIRTUAL_DISPLAY:
    try:
        from pyvirtualdisplay import Display
        display = Display(visible=False, size=(1920, 1080))
        display.start()
    except:
        pass

class DesktopControl:
    def __init__(self):
        if PYAUTOGUI_AVAILABLE:
            pyautogui.FAILSAFE = True
        self.last_screenshot = None
        self.has_display = HAS_DISPLAY

    def take_screenshot(self) -> str:
        """Captura la pantalla y la guarda"""
        try:
            if not ImageGrab:
                return None
            screenshot = ImageGrab.grab()
            filename = f"{SCREENSHOT_DIR}/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(filename)
            self.last_screenshot = filename
            return filename
        except Exception as e:
            print(f"Error tomando screenshot con PIL: {e}")
            # Intentar con xdotool como alternativa
            try:
                filename = f"{SCREENSHOT_DIR}/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                subprocess.run(
                    f"import -window root {filename}",
                    shell=True,
                    capture_output=True,
                    timeout=5
                )
                if os.path.exists(filename):
                    self.last_screenshot = filename
                    return filename
            except:
                pass
            return None

    def click(self, x: int, y: int, button: str = "left") -> bool:
        """Hace clic en las coordenadas especificadas"""
        try:
            if not PYAUTOGUI_AVAILABLE:
                return False
            pyautogui.click(x, y, button=button)
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Error haciendo clic: {e}")
            return False

    def type_text(self, text: str, interval: float = 0.05) -> bool:
        """Escribe el texto especificado"""
        try:
            if not PYAUTOGUI_AVAILABLE:
                return False
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
            if PYAUTOGUI_AVAILABLE:
                pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            return True
        except:
            return self.type_text(text)

    def press_key(self, key: str) -> bool:
        """Presiona una tecla o combinación"""
        try:
            if not PYAUTOGUI_AVAILABLE:
                return False
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

    def move_mouse(self, x: int, y: int) -> bool:
        """Mueve el ratón a las coordenadas especificadas"""
        try:
            if not PYAUTOGUI_AVAILABLE:
                return False
            pyautogui.moveTo(x, y, duration=0.5)
            return True
        except Exception as e:
            print(f"Error moviendo ratón: {e}")
            return False
        """Desplaza la página en la dirección especificada"""
        try:
            if not PYAUTOGUI_AVAILABLE:
                return False
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
            result = {"success": False, "message": "", "action": action_type}

            if action_type == "click":
                coords = action.get("coordinates", [])
                if coords and len(coords) == 2:
                    success = self.click(int(coords[0]), int(coords[1]))
                    result["success"] = success
                    result["message"] = f"Clic en ({coords[0]}, {coords[1]})" if success else "Error en clic"

            elif action_type == "move_mouse":
                coords = action.get("coordinates", [])
                if coords and len(coords) == 2:
                    success = self.move_mouse(int(coords[0]), int(coords[1]))
                    result["success"] = success
                    result["message"] = f"Ratón movido a ({coords[0]}, {coords[1]})" if success else "Error moviendo ratón"

            elif action_type == "type":
                text = action.get("text", "")
                if text:
                    success = self.write(text)
                    result["success"] = success
                    result["message"] = f"Texto escrito: {text[:30]}" if success else "Error escribiendo"

            elif action_type == "command":
                command = action.get("command", "")
                if command:
                    output = self.execute_command(command)
                    result["success"] = True
                    result["message"] = output[:100]

            elif action_type == "scroll":
                coords = action.get("coordinates", [])
                direction = action.get("direction", "down")
                clicks = action.get("clicks", 5)
                if coords and len(coords) == 2:
                    success = self.scroll(int(coords[0]), int(coords[1]), clicks=clicks, direction=direction)
                    result["success"] = success
                    result["message"] = f"Scroll {direction}" if success else "Error en scroll"

            elif action_type == "press_key":
                key = action.get("key", "")
                if key:
                    success = self.press_key(key)
                    result["success"] = success
                    result["message"] = f"Tecla presionada: {key}" if success else "Error presionando tecla"

            else:
                result["message"] = f"Acción desconocida: {action_type}"

            return result

        except json.JSONDecodeError as e:
            return {"success": False, "message": f"JSON inválido: {str(e)}", "action": "unknown"}
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}", "action": "unknown"}
