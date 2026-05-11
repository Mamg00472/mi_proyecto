import numpy as np
import time
import random

# --- CONFIGURACIÓN DEL MUNDO ---
TAMANO_MUNDO = 10  # Posiciones de 0 a 9
OBJETIVO = 9       # El "tesoro" está al final
EPISODIOS = 100    # Cuántas veces lo intentará
ALPHA = 0.1        # Learning rate (qué tan rápido aprende)
GAMMA = 0.9        # Discount factor (importancia del futuro)
EPSILON = 0.3      # Probabilidad de explorar (30%)

# 1. Inicializamos la Q-Table (10 estados x 2 acciones: 0=Izquierda, 1=Derecha)
q_table = np.zeros((TAMANO_MUNDO, 2))

print(f"--- INICIANDO ENTRENAMIENTO ---")
print(f"Objetivo: Llegar a la posición {OBJETIVO}")
time.sleep(2)

for episodio in range(EPISODIOS):
    estado = 0  # Empezamos siempre al inicio
    pasos = 0
    recompensa_total = 0
    terminado = False

    while not terminado:
        # A. DECISIÓN (Epsilon-Greedy)
        if random.uniform(0, 1) < EPSILON:
            accion = random.randint(0, 1) # Explorar
        else:
            accion = np.argmax(q_table[estado]) # Explotar

        # B. EJECUTAR ACCIÓN (Moverse)
        nuevo_estado = estado
        if accion == 1 and estado < TAMANO_MUNDO - 1: # Derecha
            nuevo_estado += 1
        elif accion == 0 and estado > 0: # Izquierda
            nuevo_estado -= 1

        # C. RECOMPENSA
        if nuevo_estado == OBJETIVO:
            recompensa = 100
            terminado = True
        else:
            recompensa = -1 # Castigo por cada paso (para que sea rápido)

        # D. FÓRMULA DE BELLMAN
        viejo_q = q_table[estado, accion]
        proximo_max = np.max(q_table[nuevo_estado])
        
        # Actualizamos la memoria
        q_table[estado, accion] = viejo_q + ALPHA * (recompensa + GAMMA * proximo_max - viejo_q)

        # E. ACTUALIZAR INFO
        estado = nuevo_estado
        pasos += 1
        recompensa_total += recompensa

    # Cada 10 episodios imprimimos cómo va la IA
    if (episodio + 1) % 10 == 0:
        print(f"Episodio {episodio + 1}: Llegó al objetivo en {pasos} pasos. Memoria (Q-Table) actualizada.")

print("\n--- ENTRENAMIENTO FINALIZADO ---")
print("Valores finales de la Q-Table (Izquierda | Derecha):")
print(q_table)

# PRUEBA FINAL (La IA ya es experta)
print("\n--- PRUEBA FINAL (MODO EXPERTO) ---")
estado = 0
camino = [0]
while estado != OBJETIVO:
    accion = np.argmax(q_table[estado])
    estado = estado + 1 if accion == 1 else estado - 1
    camino.append(estado)
print(f"Camino tomado por la IA: {camino}")