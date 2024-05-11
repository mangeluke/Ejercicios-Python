ValorCompra = int(input("ingrese el valor de su compra: "))
ValorReferencia =  50000
descuento1 = 0.1
descuento2 = 0.05
descuento3 = 0.07

if ValorCompra>ValorReferencia:
    print("el valor con el descuento del 10% es", ValorCompra-(ValorCompra*descuento1))
elif ValorCompra==0:
    print("no tendra descuento ya que el valor de la compra es 0")
elif ValorCompra<ValorReferencia:
    print("el valor con el descuento del 5% es", ValorCompra-(ValorCompra*descuento2))
elif ValorCompra==ValorReferencia:
    print("el valor con el descuento del 7% es", ValorCompra-(ValorCompra*descuento3))