import speech_recognition as sr
import pyttsx3
import threading
from config import ENABLE_VOICE_INPUT

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

    def listen_for_command(self, timeout: int = 10) -> str:
        """Escucha un comando de voz del usuario"""
        if not ENABLE_VOICE_INPUT:
            return ""

        try:
            with sr.Microphone() as source:
                print("🎤 Escuchando... (di tu instrucción)")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=timeout)

            print("⏳ Procesando audio...")
            text = self.recognizer.recognize_google(audio, language='es-ES')
            print(f"✓ Escuchado: {text}")
            return text

        except sr.UnknownValueError:
            print("❌ No se entendió el audio")
            return ""
        except sr.RequestError as e:
            print(f"❌ Error con el servicio: {e}")
            return ""
        except Exception as e:
            print(f"❌ Error escuchando: {e}")
            return ""

    def speak(self, text: str, wait: bool = True) -> None:
        """Reproduce un mensaje de voz"""
        try:
            print(f"🔊 Hablando: {text}")
            self.engine.say(text)
            if wait:
                self.engine.runAndWait()
            else:
                threading.Thread(target=self.engine.runAndWait, daemon=True).start()
        except Exception as e:
            print(f"Error hablando: {e}")

    def process_voice_loop(self) -> None:
        """Loop continuo de escucha de voz"""
        while True:
            command = self.listen_for_command()
            if command:
                yield command
