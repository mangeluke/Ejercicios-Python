#Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.

edades_hombres = []

edades_mujeres = []




while True:
    genero = input("Ingrese el género del alumno (Hombre/Mujer): ").lower()
    if genero not in ['hombre', 'mujer']:
        print("Género no válido. Por favor, ingrese 'Hombre' o 'Mujer'.")
        continue
    
    edad = int(input("Ingrese la edad del alumno: "))
    
    if genero == 'hombre':
        edades_hombres.append(edad)
    else:
        edades_mujeres.append(edad)
        
        break

promedio_edad_hombres = sum(edades_hombres) / len(edades_hombres) if edades_hombres else 0
promedio_edad_mujeres = sum(edades_mujeres) / len(edades_mujeres) if edades_mujeres else 0
promedio_edad_grupo = (sum(edades_hombres) + sum(edades_mujeres)) / (len(edades_hombres) + len(edades_mujeres)) if edades_hombres or edades_mujeres else 0

print(f"Promedio de edad de hombres: {promedio_edad_hombres:.2f} años")
print(f"Promedio de edad de mujeres: {promedio_edad_mujeres:.2f} años")
print(f"Promedio de edad del grupo completo: {promedio_edad_grupo:.2f} años")
