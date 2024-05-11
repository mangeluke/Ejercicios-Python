#Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto

numero = int(input("digite el numero: "))

for i in range(0, 11):
    resultado = i * numero
    print(numero, "x", i, " = ", resultado)
    