# 🤖 Agente Gemini - Control Virtual de Computadora

Un agente de IA potente que usa Google Gemini para controlar tu computadora mediante:
- **Comandos de voz** 🎤 (escuchando como en el video)
- **Interfaz de terminal** 💬 (escribiendo instrucciones)
- **Visión por computadora** 👁️ (analizando pantalla)
- **Automación completa** ⚙️ (mouse, teclado, comandos del sistema)

## 📋 Requisitos

- Python 3.8+
- Micrófono (para modo voz)
- Acceso a Internet (para API de Gemini)

## 🚀 Instalación

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar API Key de Gemini

Sigue estos pasos:

1. Ve a https://aistudio.google.com/app/apikeys
2. Crea una nueva API key
3. En la carpeta `Gemini/`, copia `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
4. Edita `.env` y pega tu API key:
   ```
   GEMINI_API_KEY=tu_clave_aqui
   ```

## 💻 Uso

### Iniciar el agente
```bash
python main.py
```

### Modos disponibles

#### 🎤 Modo Voz
- El agente escucha tus instrucciones
- Ejecuta acciones en la pantalla
- Responde por voz

Ejemplo de instrucciones:
- "Abre Google Chrome"
- "Busca Python en Google"
- "Haz clic en el primer resultado"

#### 📝 Modo Texto
- Escribe instrucciones en la terminal
- El agente las ejecuta
- Muestra resultados en texto

#### 🔄 Modo Híbrido (Recomendado)
- Elige entre voz y texto
- Cambia entre modos fácilmente
- Combina ambas formas de control

## 🛠️ Arquitectura

```
Gemini/
├── main.py              # Punto de entrada
├── agent.py             # Lógica principal del agente
├── gemini_api.py        # Integración con API Gemini
├── desktop_control.py   # Control de mouse/teclado
├── voice_handler.py     # Procesamiento de voz
├── config.py            # Configuración
├── requirements.txt     # Dependencias
├── .env                 # Variables de entorno (crear)
└── prueba.py           # Ejemplo de Q-Learning
```

## 🔧 Funcionalidades

- **Captura de Pantalla**: Analiza qué hay en tu pantalla
- **Movimiento de Mouse**: Hace clic en coordenadas específicas
- **Escritura de Teclado**: Escribe texto en campos
- **Comandos del Sistema**: Ejecuta comandos en terminal
- **Scroll**: Desplaza páginas
- **Teclas Especiales**: Presiona Enter, Tab, etc.
- **Reconocimiento de Voz**: Entiende comandos en español
- **Síntesis de Voz**: Responde hablando

## 📌 Notas Importantes

1. **Seguridad**: No ejecuta comandos peligrosos sin confirmación
2. **Failsafe**: Mueve el mouse a esquina superior izquierda para emergencia
3. **Logs**: Todos los comandos se guardan en `agent_log.txt`
4. **Screenshots**: Se guardan en `/tmp/gemini_screenshots/`

## 🎯 Próximas Mejoras

- [ ] Historial persistente de comandos
- [ ] Confirmación de acciones peligrosas
- [ ] Macros personalizadas
- [ ] Integración con más servicios
- [ ] Interfaz gráfica

## 📚 Referencias

Basado en: "Le di un Cuerpo Virtual a Gemini para que trabaje en mi computadora"
- Usa Google Gemini 2.0 Flash
- Integración completa con desktop automation
- Soporte para voz e interfaz de texto

## ⚠️ Disclaimer

Este agente tiene acceso a tu computadora. Úsalo responsablemente.
No lo uses para acceder a sistemas sin autorización.

---

**Creado con ❤️ usando Google Gemini**
