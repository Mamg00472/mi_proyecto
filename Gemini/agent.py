import json
import time
from gemini_api import GeminiAPI
from desktop_control import DesktopControl
from voice_handler import VoiceHandler
from learning_system import LearningSystem
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GeminiAgent:
    def __init__(self):
        self.gemini = GeminiAPI()
        self.desktop = DesktopControl()
        self.voice = VoiceHandler()
        self.learning = LearningSystem()
        self.running = True
        self.mode = "hybrid"
        self.max_iterations = 5  # Máximo de acciones por instrucción

    def process_instruction(self, instruction: str) -> str:
        """Procesa una instrucción del usuario ejecutando múltiples acciones"""
        logger.info(f"Instrucción recibida: {instruction}")
        self.learning.session_attempts += 1

        # Verificar si ya existe un patrón exitoso similar
        similar = self.learning.get_similar_successful_pattern(instruction)
        if similar:
            logger.info(f"Patrón similar encontrado en memoria")
            print(f"📚 Usando patrón aprendido anteriormente...")

        iteration = 0
        while iteration < self.max_iterations:
            iteration += 1
            logger.info(f"Iteración {iteration}/{self.max_iterations}")

            # Tomar screenshot
            screenshot_path = self.desktop.take_screenshot()
            if not screenshot_path:
                logger.warning("No se pudo tomar screenshot, intentando sin imagen")

            logger.info(f"Screenshot: {screenshot_path}")

            # Obtener siguiente acción de Gemini
            response = self.gemini.execute_command(instruction, screenshot_path)
            logger.info(f"Respuesta de Gemini: {response[:200]}")

            # Parsear y ejecutar acción
            try:
                # Limpiar respuesta si tiene texto adicional
                json_str = response.strip()
                if json_str.startswith("```"):
                    json_str = json_str.split("```")[1]
                    if json_str.startswith("json"):
                        json_str = json_str[4:]

                action_data = json.loads(json_str)
                execution_result = self.desktop.parse_and_execute_action(json.dumps(action_data))

                logger.info(f"Acción ejecutada: {execution_result}")
                print(f"  ✓ [{iteration}] {execution_result['message']}")

                if execution_result['success']:
                    self.learning.record_success(instruction, action_data)

                # Verificar si la instrucción está completa
                if self._is_instruction_complete(instruction, execution_result):
                    feedback = f"✅ Instrucción completada en {iteration} paso(s)"
                    print(f"\n{feedback}")
                    self.learning.log_stats()
                    return feedback

                time.sleep(0.5)  # Pausa entre acciones

            except json.JSONDecodeError as e:
                logger.warning(f"JSON inválido: {response}")
                print(f"  ⚠️ Respuesta no es JSON válido, reintentando...")
                self.learning.record_failure(instruction, {}, "JSON parsing failed")

            except Exception as e:
                logger.error(f"Error: {e}")
                print(f"  ❌ Error: {str(e)}")
                self.learning.record_failure(instruction, {}, str(e))

        feedback = f"⏱️ Agotadas {iteration} iteraciones. La instrucción podría no estar completada."
        print(f"\n{feedback}")
        self.learning.log_stats()
        return feedback

    def _is_instruction_complete(self, instruction: str, result: dict) -> bool:
        """Determina si la instrucción ha sido completada"""
        # Palabras clave que indican fin
        end_keywords = ["hecho", "completado", "finalizado", "guardado", "creado", "cerrado"]

        if result.get('success'):
            action_desc = result.get('message', '').lower()
            for keyword in end_keywords:
                if keyword in action_desc:
                    return True

        # Si es un comando del sistema, probablemente esté completo
        if result.get('action') == 'command' and result.get('success'):
            return True

        return False

    def interactive_mode(self) -> None:
        """Modo interactivo donde el usuario puede dar instrucciones"""
        print("\n" + "="*60)
        print("🤖 AGENTE GEMINI - MODO INTERACTIVO")
        print("="*60)
        print("Instrucciones:")
        print("  'voz' - Cambiar a modo voz")
        print("  'stats' - Ver estadísticas")
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

                if instruction.lower() == "stats":
                    self.learning.log_stats()
                    continue

                result = self.process_instruction(instruction)
                print()

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
        self.voice.speak("Modo voz activado. Estoy escuchando.", wait=False)

        while self.running:
            try:
                instruction = self.voice.listen_for_command()

                if not instruction:
                    continue

                if instruction.lower() in ["salir", "exit", "terminar"]:
                    self.voice.speak("Volviendo al modo de texto.", wait=False)
                    break

                result = self.process_instruction(instruction)
                self.voice.speak(result, wait=False)
                print()

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
