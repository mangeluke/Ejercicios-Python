
monto_compra = float(input("Ingrese el monto de la compra (en pesos): "))

if monto_compra >= 50000:

    color_balota = input("Ingrese el color de la balota (roja, verde, azul, amarilla, negra): ")

    if color_balota == "roja":
        descuento = 0.10
    elif color_balota == "verde":
        descuento = 0.15
    elif color_balota == "azul":
        descuento = 0.20
    elif color_balota == "amarilla":
        descuento = 0.50
    elif color_balota == "negra":
        descuento = 1.00
    else:
        print("Color de balota inválido. Por favor ingrese un color válido.")
        exit()

    monto_descontado = monto_compra * descuento
    
    monto_final = monto_compra - monto_descontado

    print(f"Monto de la compra: {monto_compra:.2f} pesos")
    print(f"Color de la balota: {color_balota}")
    print(f"Monto descontado: {monto_descontado:.2f} pesos")
    print(f"Monto final a pagar: {monto_final:.2f} pesos")
else:
    print(f"Monto de la compra: {monto_compra:.2f} pesos")
    print("No participa en el sorteo. No se aplica ningún descuento.")
    print(f"Monto final a pagar: {monto_compra:.2f} pesos")