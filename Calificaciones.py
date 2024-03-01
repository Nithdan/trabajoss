print("----Calificaciones----")

calificacion = float(input("Ingrese calificacion:"))

if calificacion >= 100:
    print("-----Excelente, Felicidades-----")

elif calificacion >= 90 and calificacion <= 99.9:
    print("-----Muy bien-----")

elif calificacion >= 80 and calificacion <= 89.9:
    print("-----Bien-----")

elif calificacion >= 70 and calificacion <= 79.9:
    print("-----Regular-----")

elif calificacion >= 60 and calificacion <= 69.9:
    print("-----Suficiente-----")

else:
    print("Insuficiente :(, echele ganas.")