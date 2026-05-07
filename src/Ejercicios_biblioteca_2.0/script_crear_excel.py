import os
from openpyxl import Workbook

"""Script para crear un excel desde python"""

wb = Workbook()
ws = wb.active

ws.append(["titulo", "autor", "prestado"])
ws.append(["1984", "Orwell", False])

wb.save("src/Ejercicios_biblioteca_2.0/data/libros.xlsx")