import json
import os
from datetime import datetime
from typing import Dict, List

class LearningSystem:
    """Sistema de aprendizaje del agente - guarda intentos exitosos"""

    def __init__(self, memory_file: str = "agent_memory.json"):
        self.memory_file = memory_file
        self.memory = self.load_memory()
        self.session_attempts = 0
        self.session_successes = 0

    def load_memory(self) -> Dict:
        """Carga la memoria de intentos anteriores"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                return {"successful_patterns": [], "failed_patterns": []}
        return {"successful_patterns": [], "failed_patterns": []}

    def save_memory(self):
        """Guarda la memoria al disco"""
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)

    def record_success(self, instruction: str, action: Dict):
        """Registra un intento exitoso"""
        self.session_successes += 1
        pattern = {
            "instruction": instruction,
            "action": action,
            "timestamp": datetime.now().isoformat(),
            "success_count": 1
        }

        # Verificar si ya existe un patrón similar
        for p in self.memory["successful_patterns"]:
            if p["instruction"].lower() in instruction.lower() or instruction.lower() in p["instruction"].lower():
                p["success_count"] += 1
                self.save_memory()
                return

        self.memory["successful_patterns"].append(pattern)
        self.save_memory()

    def record_failure(self, instruction: str, action: Dict, error: str):
        """Registra un intento fallido"""
        pattern = {
            "instruction": instruction,
            "action": action,
            "error": error,
            "timestamp": datetime.now().isoformat()
        }
        self.memory["failed_patterns"].append(pattern)
        self.save_memory()

    def get_similar_successful_pattern(self, instruction: str) -> Dict:
        """Busca un patrón exitoso similar"""
        for pattern in self.memory["successful_patterns"]:
            if pattern["instruction"].lower() in instruction.lower():
                return pattern
        return None

    def get_success_rate(self) -> float:
        """Retorna el porcentaje de éxito"""
        if self.session_attempts == 0:
            return 0.0
        return (self.session_successes / self.session_attempts) * 100

    def log_stats(self):
        """Registra estadísticas de la sesión"""
        print(f"\n📊 ESTADÍSTICAS DE LA SESIÓN")
        print(f"   Intentos totales: {self.session_attempts}")
        print(f"   Exitosos: {self.session_successes}")
        print(f"   Tasa de éxito: {self.get_success_rate():.1f}%")
        print(f"   Patrones memorizados: {len(self.memory['successful_patterns'])}\n")
