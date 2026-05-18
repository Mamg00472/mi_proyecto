import json
import time
from gemini_api import GeminiAPI
from desktop_control import DesktopControl
from voice_handler import VoiceHandler
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GeminiAgent:
    def __init__(self):
        self.gemini = GeminiAPI()
        self.desktop = DesktopControl()
        self.voice = VoiceHandler()
        self.running = True
        self.mode = "hybrid"

    def process_instruction(self, instruction: str) -> str:
        """Procesa una instrucción del usuario"""
        logger.info(f"Instrucción recibida: {instruction}")

        screenshot_path = self.desktop.take_screenshot()
        logger.info(f"Screenshot tomado: {screenshot_path}")

        response = self.gemini.execute_command(instruction, screenshot_path)
        logger.info(f"Respuesta de Gemini: {response}")

        try:
            action_data = json.loads(response)
            execution_result = self.desktop.parse_and_execute_action(json.dumps(action_data))
            logger.info(f"Acción ejecutada: {execution_result}")

            feedback_message = f"Acción completada: {execution_result['message']}"
            return feedback_message

        except json.JSONDecodeError:
            logger.warning("Respuesta no es JSON válido, tratando como respuesta directa")
            return f"Respuesta: {response[:200]}"

    def interactive_mode(self) -> None:
        """Modo interactivo donde el usuario puede dar instrucciones"""
        print("\n" + "="*60)
        print("🤖 AGENTE GEMINI - MODO INTERACTIVO")
        print("="*60)
        print("Instrucciones:")
        print("  'voz' - Cambiar a modo voz")
        print("  'screenshot' - Tomar captura de pantalla")
        print("  'salir' - Cerrar el agente")
        print("="*60 + "\n")

        while self.running:
            try:
                instruction = input("📝 Instrucción: ").strip()

                if not instruction:
                    continue

                if instruction.lower() == "salir":
                    print("👋 Cerrando agente...")
                    self.running = False
                    break

                if instruction.lower() == "voz":
                    self.voice_mode()
                    continue

                if instruction.lower() == "screenshot":
                    path = self.desktop.take_screenshot()
                    print(f"✓ Screenshot guardado en: {path}")
                    continue

                result = self.process_instruction(instruction)
                print(f"✓ {result}\n")

            except KeyboardInterrupt:
                print("\n👋 Agente interrumpido")
                self.running = False
                break
            except Exception as e:
                logger.error(f"Error en modo interactivo: {e}")
                print(f"❌ Error: {e}\n")

    def voice_mode(self) -> None:
        """Modo voz continuo"""
        print("\n🎤 MODO VOZ ACTIVADO (di 'salir' para volver atrás)")
        self.voice.speak("Modo voz activado. Estoy escuchando.")

        while self.running:
            try:
                instruction = self.voice.listen_for_command()

                if not instruction:
                    continue

                if instruction.lower() in ["salir", "exit", "terminar"]:
                    self.voice.speak("Volviendo al modo de texto.")
                    break

                result = self.process_instruction(instruction)
                self.voice.speak(result, wait=False)
                print(f"✓ {result}\n")

            except KeyboardInterrupt:
                print("\n👋 Modo voz cerrado")
                break
            except Exception as e:
                logger.error(f"Error en modo voz: {e}")

    def hybrid_mode(self) -> None:
        """Modo híbrido: combina voz y texto"""
        print("\n" + "="*60)
        print("🤖 AGENTE GEMINI - MODO HÍBRIDO")
        print("="*60)
        print("Opciones:")
        print("  [1] Modo voz")
        print("  [2] Modo texto")
        print("  [3] Salir")
        print("="*60 + "\n")

        while self.running:
            try:
                choice = input("Selecciona modo (1/2/3): ").strip()

                if choice == "1":
                    self.voice_mode()
                elif choice == "2":
                    self.interactive_mode()
                elif choice == "3":
                    print("👋 Cerrando agente...")
                    self.running = False
                    break
                else:
                    print("❌ Opción inválida\n")

            except KeyboardInterrupt:
                print("\n👋 Agente interrumpido")
                self.running = False
                break
            except Exception as e:
                logger.error(f"Error: {e}")

    def run(self) -> None:
        """Inicia el agente"""
        self.hybrid_mode()
