#. Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
#Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja de todo el grupo.
calificaciones = [float(input(f"Ingrese la calificación del alumno {i+1}: ")) for i in range(20)]
promedio = sum(calificaciones) / len(calificaciones)
calificacion_maxima = max(calificaciones)
calificacion_minima = min(calificaciones)

print("El promedio del grupo es:", promedio)
print("La calificación más alta es:", calificacion_maxima)
print("La calificación más baja es:", calificacion_minima)