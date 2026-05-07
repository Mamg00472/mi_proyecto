import csv

def exportar_libros_csv(lista_libros):
    with open("data/libros.csv", "w", encoding="utf-8") as file:
        escritura = csv.writer(file)

        escritura.writerow([
            "titulo",
            "autor",
            "prestado"
        ])
        for libro in lista_libros:
            escritura.writerow([
                libro.titulo,
                libro.autor,
                libro.prestado
            ])