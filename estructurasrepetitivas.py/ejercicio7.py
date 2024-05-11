#La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad
#de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo
#dígito de la placa de cada carro, se puede determinar el color de la calcomanía
#utilizando la siguiente relación

def contar_calcomanias(placas):
    colores = {"roja": 0, "verde": 0, "azul": 0, "amarilla": 0, "rosa": 0}
    for placa in placas:
        colores[{"1": "roja", "2": "roja", "3": "verde", "4": "verde", "5": "azul", "6": "azul", "7": "amarilla", "8": "amarilla", "9": "rosa", "0": "rosa"}[placa[-1]]] += 1
    return colores

placas = ["ABC123", "DEF456", "GHI789", "JKL012", "MNO345"]
cantidad_calcomanias = contar_calcomanias(placas)

for color, cantidad in cantidad_calcomanias.items():
    print(f"Número de calcomanías {color}: {cantidad}")