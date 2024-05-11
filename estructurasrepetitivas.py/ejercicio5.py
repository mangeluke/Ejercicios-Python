'''
Una persona debe realizar un muestreo con 50 personas para determinar el
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona.
Las categorías se determinan de acuerdo a la siguiente tabla:
'''
import numpy as np
import random

grupos_edad = {'niños': (0, 12), 'jóvenes': (13, 25), 'adultos': (26, 60), 'ancianos': (61, 120)}
peso_promedio = {'niños': 30, 'jóvenes': 60, 'adultos': 70, 'ancianos': 65}

muestra = {grupo: [random.uniform(peso_promedio[grupo]-10, peso_promedio[grupo]+10) 

for _ in range(50)] for grupo in grupos_edad}

for grupo, pesos in muestra.items():
    print(f"Promedio de peso de {grupo}: {np.mean(pesos):.2f} kg")