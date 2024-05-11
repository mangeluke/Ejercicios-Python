#Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa
#se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio
#,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos
#que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad
#sea igual a 0

cantidad_hombres = 0
cantidad_mujeres = 0
altura_total = 0
cantidad_altura_mayor_170 = 0
cantidad_altura_menor_150 = 0
cantidad_alumnos = 0

# Bucle para ingresar datos de los alumnos
while True:
    # Solicitar datos del alumno
    sexo = input("Ingrese el sexo del alumno (M/F): ").upper()
    if sexo == "0":
        break 
    edad = int(input("Ingrese la edad del alumno: "))
    altura = float(input("Ingrese la altura del alumno en metros: "))


    cantidad_alumnos += 1


    if sexo == "M":
        cantidad_hombres += 1
    elif sexo == "F":
        cantidad_mujeres += 1


    altura_total += altura


    if altura > 1.70:
        cantidad_altura_mayor_170 += 1
    elif altura <= 1.50:
        cantidad_altura_menor_150 += 1


if cantidad_alumnos != 0:
    altura_promedio = altura_total / cantidad_alumnos
else:
    altura_promedio = 0


print("Cantidad de hombres:", cantidad_hombres)
print("Cantidad de mujeres:", cantidad_mujeres)
print("Altura promedio:", altura_promedio)
print("Cantidad de alumnos con altura mayor a 1.70m:", cantidad_altura_mayor_170)
print("Cantidad de alumnos con altura menor o igual a 1.50m:", cantidad_altura_menor_150)