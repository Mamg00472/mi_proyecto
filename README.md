# 📘 Formación Técnica Base – Python

Este reposorio contiene una colección de ejercicios y proyectos diseñados para fortalecer habilidades en Python, desde conceptos básicos hasta programación orientada a objetos y desarrollo de proyectos completos.

---

## 🧠 Ejercicios de Python

### 📌 Lista de ejercicios

1. Verificar si un número es par o impar  
2. Calcular el factorial de un número  
3. Ordenar una lista  
4. Verificar si una cadena es un palíndromo  
5. Generar la sucesión de Fibonacci  
6. Encontrar números primos en un rango  
7. Contar palabras en una cadena  
8. Crear una matriz identidad  
9. Validar un correo electrónico  
10. Buscar una palabra en un archivo de texto  
11. Operaciones con listas (uso de librerías como numpy)  
12. Simular un juego de dados  
13. Analizar datos de un CSV  
14. Contador de frecuencia de palabras  

---

### 📝 Enunciados

#### Ejercicio 1
Escribe un programa que solicite al usuario un número y determine si es par o impar.

#### Ejercicio 2
Escribe una función que calcule el factorial de un número ingresado por el usuario.

#### Ejercicio 3
Solicita al usuario una lista de números separados por comas y ordénalos en orden ascendente.

#### Ejercicio 4
Escribe un programa que verifique si una palabra o frase es un palíndromo.

#### Ejercicio 5
Crea una función que genere los primeros *n* números de la sucesión de Fibonacci.

#### Ejercicio 6
Escribe un programa que encuentre todos los números primos entre 1 y un número dado.

#### Ejercicio 7
Cuenta el número de palabras en una cadena ingresada por el usuario.

#### Ejercicio 8
Genera una matriz identidad de tamaño *n x n*.

#### Ejercicio 9
Valida si una cadena tiene formato correcto de correo electrónico.

#### Ejercicio 10
Lee un archivo de texto y busca una palabra, indicando cuántas veces aparece.

#### Ejercicio 11
Suma dos listas de números elemento por elemento.

#### Ejercicio 12
Simula el lanzamiento de dos dados hasta obtener un doble seis.

#### Ejercicio 13
Lee un archivo CSV, procesa los datos y genera un nuevo archivo con información adicional.

#### Ejercicio 14
Cuenta la frecuencia de cada palabra en un texto.

---

## 🧱 Programación Orientada a Objetos (POO)

### 📌 Lista de ejercicios

1. Crear y usar una clase  
2. Crear múltiples instancias  
3. Herencia básica  
4. Uso de `super()`  
5. Objetos como atributos  
6. Herencia múltiple  
7. Métodos estáticos y de clase  
8. Métodos mágicos  
9. Sistema de registro  
10. Calculadora con POO  

---

### 📝 Enunciados

#### Ejercicio POO 1
Define una clase `Animal` con un atributo nombre y un método hablar.

#### Ejercicio POO 2
Crea una clase `Libro` con atributos título y autor, y múltiples instancias.

#### Ejercicio POO 3
Crea una clase `Vehiculo` y una subclase `Coche` con un método adicional.

#### Ejercicio POO 4
Implementa una clase `Empleado` que herede de `Persona` usando `super()`.

#### Ejercicio POO 5
Crea una clase `Direccion` y úsala como atributo en `Persona`.

#### Ejercicio POO 6
Implementa herencia múltiple con clases `Volador`, `Nadador` y `Pato`.

#### Ejercicio POO 7
Usa métodos estáticos y de clase en una clase de automóviles.

#### Ejercicio POO 8
Implementa los métodos mágicos `__str__` y `__eq__` en una clase `Producto`.

#### Ejercicio POO 9
Crea un sistema de registro de usuarios con operaciones básicas.

#### Ejercicio POO 10
Desarrolla una calculadora orientada a objetos.

---

## 📚 Proyecto Final: Sistema de Gestión de Biblioteca

### 🎯 Objetivo
Desarrollar un sistema que permita:

- Registrar libros y usuarios  
- Prestar libros a usuarios  
- Devolver libros  
- Mostrar libros disponibles y prestados  

---

### 📁 Estructura sugerida

```bash
biblioteca/
│
├── main.py
├── libro.py
├── usuario.py
├── biblioteca.py
└── utils.py
```

---

### 🧩 Componentes

- **Libro**: información del título, autor y estado de préstamo  
- **Usuario**: gestión de libros prestados  
- **Biblioteca**: lógica del sistema  
- **Utils**: funciones auxiliares (opcional)  
- **Main**: interfaz por consola  

---

## 🚀 Proyecto Final II: Biblioteca Avanzada

### 🔧 Descripción

Extensión del sistema anterior con:

- Persistencia en archivos JSON  
- Control de errores  
- Roles de usuario  
- Historial de préstamos  
- Importación/exportación de datos  

---

### 📁 Estructura sugerida

```bash
biblioteca_avanzada/
│
├── main.py
├── models/
│ ├── libro.py
│ ├── usuario.py
│ └── historial.py
├── services/
│ ├── biblioteca.py
│ ├── persistencia.py
│ └── excel_csv.py
├── utils/
│ └── menu.py
└── data/
├── libros.json
├── usuarios.json
├── historial.json
└── libros.csv
```
---

## 🧠 Proyecto Final III: Biblioteca Profesional

### 🎯 Objetivo

Ampliar el sistema con:

- Herencia avanzada de usuarios  
- Tipos de recursos bibliográficos  
- Control de préstamos diferenciado  
- Gestión de sanciones  
- Reportes polimórficos  
- Persistencia avanzada  
- Importación/exportación (CSV y Excel)  
- Autenticación y roles  
- Interfaz en consola estructurada  

---

### 🧩 Requisitos funcionales

#### 👤 Usuarios

- Clase base `Usuario` (abstracta): id, nombre, correo  
- Estudiante: máximo 3 préstamos  
- Profesor: máximo 5 préstamos + acceso digital  
- Bibliotecario: acceso total  

#### 📚 Recursos

- Clase base `Recurso`  
- Subclases:
  - Libro  
  - Revista  
  - Tesis  
  - RecursoDigital  

#### 🔄 Préstamos

- Registrar fechas  
- Validar disponibilidad  
- Controlar límites por usuario  
- Generar sanciones por retrasos  

#### 📊 Sistema

- Registro de usuarios  
- Gestión de recursos  
- Préstamos y devoluciones  
- Reportes  
- Importación/exportación de datos  

---

### 📁 Estructura recomendada

```bash
biblioteca_avanzada/
├── main.py
├── models/
│ ├── usuario.py
│ ├── estudiante.py
│ ├── profesor.py
│ ├── bibliotecario.py
│ ├── recurso.py
│ ├── libro.py
│ ├── revista.py
│ ├── tesis.py
│ ├── recurso_digital.py
│ ├── prestamo.py
│ └── historial.py
├── services/
│ ├── sistema_biblioteca.py
│ ├── persistencia.py
│ └── excel_csv.py
├── utils/
│ └── validaciones.py
└── data/
├── usuarios.json
├── recursos.json
├── historial.json
├── recursos.xlsx
└── prestamos.csv
```

---

## 🏁 Cómo usar este repositorio

1. Clona el repositorio  
2. Resuelve los ejercicios sin consultar soluciones  
3. Implementa los proyectos paso a paso  
4. Mejora el código aplicando buenas prácticas  

---

## 📌 Recomendaciones

- Usa control de versiones (Git)  
- Escribe código limpio y documentado  
- Aplica principios SOLID  
- Prueba tu código con distintos casos  

---
