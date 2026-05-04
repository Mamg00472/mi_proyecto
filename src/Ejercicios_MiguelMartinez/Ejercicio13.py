with open("../Documentos/Ejercicio_13.csv", "r", encoding="utf-8") as lectura, open("../Documentos/datos_actualizados.csv", "w", encoding="utf-8") as escritura:
    for linea in lectura:
        linea = linea.replace("\n", "")
        if linea == "nombre,valor":
            continue
        linea = linea.split(",")
        linea[1] = int(linea[1])
        linea.append(linea[1] * 2)
        for count, i in enumerate(linea):
            linea[count] = str(i)
        escritura.write(",".join(linea) + "\n")
        
