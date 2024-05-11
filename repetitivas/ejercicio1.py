

for i in range (10):
    nota = float(input(f"ingrese la calificacion del estudiante {i + 1}: "))
    if nota < 50:
        nota += 1
    elif 50 <= nota < 70:
        nota += 1
    elif 70 <= nota < 80:
        nota += 1
    else:
        nota += 1

    
print(f"numero de calificacion con calificacion menor a 50 :{nota}")   
print(f"numero de calificacion con calificacion 50 y 70 :{nota}")
print(f"numero de calificacion con calificacion 70 y 80 :{nota}")
print(f"numero de calificacion con calificacion mayor a 80 :{nota}")

