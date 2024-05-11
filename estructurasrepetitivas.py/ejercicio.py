#Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros.

positivo = 0
negativo = 0
neutro = 0

for i in range(-10, 9):
    if i > 0:
        positivo += 1
    elif i < 0:
        negativo += 1
    elif i == 0:
        neutro += 1
        
print("el numero positivo es", positivo)
print("el numero negativo es", negativo)
print("el nuemro neutro es", neutro)