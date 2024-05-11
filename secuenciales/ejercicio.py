ValorCompra = 200
descuento = 0.05
ValorTotal = (ValorCompra-descuento)

ValorCompra = int(input("digite el valor para la variable ValorCompra: "))
descuento = int(input("digite el valor para la variable descuento: "))
ValorTotal = int(input("digite el valor para la variable ValorTotal: "))

print(f"el valor de la compra es: {ValorCompra}")
print(f"el descuento es de: {ValorCompra * descuento}")
print("el ValorTotal es: ",ValorTotal)


