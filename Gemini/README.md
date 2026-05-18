# 🤖 Agente Gemini - Control Virtual de Computadora

Un agente de IA potente que usa Google Gemini para controlar tu computadora mediante:
- **Comandos de voz** 🎤 (escuchando como en el video)
- **Interfaz de terminal** 💬 (escribiendo instrucciones)
- **Visión por computadora** 👁️ (analizando pantalla)
- **Automación completa** ⚙️ (mouse, teclado, comandos del sistema)
- **Sistema de aprendizaje** 🧠 (mejora con cada intento)

## ⚠️ Requisitos de Entorno

Este agente funciona mejor en:
- ✅ **Windows/Mac con GUI** - Control total del mouse y pantalla
- ✅ **Linux con servidor X11** - Screenshots y automación completa
- ⚠️ **Servidores headless** - Modo simulación disponible

### En Servidor/Headless
Si estás en un servidor sin GUI, usa el **modo de demostración**:
```bash
python demo.py
```

## 📋 Requisitos

- Python 3.8+
- Micrófono (para modo voz)
- Acceso a Internet (para API de Gemini)
- GUI (para control del sistema) - OPCIONAL

## 🚀 Instalación

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar API Key de Gemini

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

### Iniciar el agente completo
```bash
python main.py
```

### Ver demostración (sin tocar el sistema)
```bash
python demo.py
```

### Probar configuración
```bash
python test_setup.py
```

## 🎯 Modos de Operación

### 🎤 Modo Voz
- El agente escucha tus instrucciones
- Ejecuta acciones en la pantalla
- Responde por voz

Ejemplo:
```
"Abre Google Chrome"
"Busca Python en Google"
"Haz clic en el primer resultado"
```

### 📝 Modo Texto
- Escribe instrucciones en la terminal
- El agente las ejecuta
- Muestra resultados en texto

### 🔄 Modo Híbrido (Recomendado)
- Elige entre voz y texto
- Cambia entre modos fácilmente
- Combina ambas formas de control

## 🧠 Sistema de Aprendizaje

El agente guarda patrones exitosos en `agent_memory.json`:

```json
{
  "successful_patterns": [
    {
      "instruction": "crea una carpeta",
      "action": {...},
      "success_count": 5
    }
  ]
}
```

Con cada intento exitoso:
- 📈 Mejora su velocidad
- 🧠 Reconoce patrones similares
- ⚡ Ejecuta acciones más rápido

## 🛠️ Arquitectura

```
Gemini/
├── main.py              # Punto de entrada principal
├── agent.py             # Lógica principal del agente
├── gemini_api.py        # Integración con API Gemini
├── desktop_control.py   # Control de mouse/teclado
├── voice_handler.py     # Procesamiento de voz
├── learning_system.py   # Sistema de aprendizaje
├── demo.py              # Demostración (modo simulación)
├── config.py            # Configuración
├── requirements.txt     # Dependencias
├── .env                 # Variables de entorno (crear)
└── agent_memory.json    # Memoria de aprendizaje (auto-generado)
```

## 🔧 Funcionalidades del Agente

### Control de Sistema
- ✅ **Captura de Pantalla**: Analiza qué hay en tu pantalla
- ✅ **Movimiento de Mouse**: Mueve a coordenadas específicas
- ✅ **Clics**: Ejecuta clics en posiciones precisas
- ✅ **Escritura**: Escribe texto en campos y campos de entrada
- ✅ **Comandos del Sistema**: Ejecuta scripts y comandos
- ✅ **Scroll**: Desplaza páginas y ventanas
- ✅ **Teclas Especiales**: Presiona Enter, Tab, Ctrl+C, etc.

### Inteligencia
- ✅ **Reconocimiento de Voz**: Entiende comandos en español
- ✅ **Síntesis de Voz**: Responde hablando
- ✅ **Visión Artificial**: Analiza capturas de pantalla
- ✅ **Aprendizaje**: Mejora con cada intento
- ✅ **Contexto**: Mantiene historial de conversación
- ✅ **Iteraciones Múltiples**: Ejecuta hasta 5 acciones por instrucción

## 📊 Estadísticas del Agente

El agente muestra en tiempo real:
```
📊 ESTADÍSTICAS DE LA SESIÓN
   Intentos totales: 5
   Exitosos: 4
   Tasa de éxito: 80.0%
   Patrones memorizados: 3
```

## 🌐 Modelos Disponibles

El agente probó automáticamente y usa:
- `gemini-3.1-flash-lite` - Recomendado (rápido, eficiente)
- Puede cambiar a otros en `config.py`

## ⚙️ Configuración Avanzada

### Editar número de iteraciones máximas
En `agent.py`, línea 12:
```python
self.max_iterations = 5  # Cambiar este número
```

### Usar otro modelo de Gemini
En `config.py`:
```python
MODEL_NAME = "gemini-2.0-flash"  # Cambiar a otro modelo
```

## 🎓 Ejemplos de Uso

### Ejemplo 1: Crear una carpeta
```
📝 Instrucción: crea una carpeta llamada "prueba" en el escritorio
  ✓ [1] Clic en escritorio
  ✓ [2] Clic en menú contextual
  ✓ [3] Texto escrito: prueba
  ✓ [4] Tecla presionada: enter

✅ Instrucción completada en 4 paso(s)
```

### Ejemplo 2: Navegar por web
```
📝 Instrucción: abre Google y busca "Python"
  ✓ [1] Clic en navegador
  ✓ [2] Texto escrito: google.com
  ✓ [3] Tecla presionada: enter
  ✓ [4] Clic en barra de búsqueda
  ✓ [5] Texto escrito: Python

✅ Instrucción completada en 5 paso(s)
```

## 📌 Notas Importantes

1. **Seguridad**: No ejecuta comandos peligrosos sin confirmación
2. **Failsafe**: Mueve el mouse a esquina superior izquierda para emergencia
3. **Logs**: Todos los comandos se guardan en `agent.log`
4. **Screenshots**: Se guardan en `/tmp/gemini_screenshots/`
5. **Memoria**: Los patrones se guardan en `agent_memory.json`

## 🚨 Limitaciones en Entornos Headless

Si estás en un servidor sin GUI:

| Característica | Estado |
|---|---|
| Gemini API | ✅ Funciona |
| Procesamiento de voz | ⚠️ Requiere audio |
| Screenshots reales | ❌ No disponible |
| Control del mouse | ❌ No disponible |
| **Modo Simulación** | ✅ **Disponible** |

**Solución**: Usa `python demo.py` para ver cómo funcionaría

## 🎯 Próximas Mejoras

- [ ] Historial persistente de comandos
- [ ] Confirmación de acciones peligrosas
- [ ] Macros personalizadas
- [ ] Integración con aplicaciones
- [ ] Interfaz gráfica web
- [ ] Sincronización entre dispositivos
- [ ] Manejo de múltiples pantallas
- [ ] Reconocimiento de ventanas activas

## 📚 Referencias

Basado en: **"Le di un Cuerpo Virtual a Gemini para que trabaje en mi computadora"**

- Usa Google Gemini 3.1 Flash Lite
- Automación completa de desktop
- Soporte para voz e interfaz de texto
- Sistema de aprendizaje por refuerzo
- Iteraciones múltiples para tareas complejas

## ⚠️ Disclaimer

Este agente tiene acceso a tu computadora. **Úsalo responsablemente.**
- No lo uses para acceder a sistemas sin autorización
- Verifica qué acciones va a ejecutar antes de confirmar
- Ten cuidado con comandos del sistema

## 🤝 Contribuciones

Este proyecto está en desarrollo. Si encuentras bugs o tienes ideas:
1. Documenta el problema
2. Sugiere mejoras
3. Prueba en diferentes escenarios

## 📞 Soporte

Si tienes problemas:
1. Verifica que `GEMINI_API_KEY` esté configurada
2. Comprueba que tienes conexión a Internet
3. Lee los logs en `agent.log`
4. Prueba con `python test_setup.py`

---

**Creado con ❤️ usando Google Gemini**

*Nota: El agente está diseñado para ejecutarse en máquinas con GUI. En servidores headless, usa el modo de demostración.*
