# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:39:52 2022

@author: dcastro31
"""

# 2. Haga un programa en Python que permita ingresar el dinero invertido por
# tres personas para formar una empresa. Cada una de ellas invierte una
# cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
# al total de la inversión.

nombre_persona_uno = (input('Digite nombre de la primera persona: '))
inversion_persona_uno = int(input(f'{nombre_persona_uno} digite el valor de su inversion: $'))
nombre_persona_dos = (input('Digite nombre de la segunda persona: '))
inversion_persona_dos = int(input(f'{nombre_persona_dos} digite el valor de su inversion: $'))
nombre_persona_tres = (input('Digite nombre de la tercera persona: '))
inversion_persona_tres = int(input(f'{nombre_persona_tres} digite el valor de su inversion: $'))
total = (inversion_persona_uno + inversion_persona_dos + inversion_persona_tres)
print(f'El valor total de la inversion es: ${total:,}')
porcentaje_persona_uno = (inversion_persona_uno / total) * 100
porcentaje_persona_dos = (inversion_persona_dos / total) * 100
porcentaje_persona_tres = (inversion_persona_tres / total) * 100
print(f'El valor de la inversion de {nombre_persona_uno} es de ${inversion_persona_uno:,} y su porcentaje es de {porcentaje_persona_uno}%')
print(f'El valor de la inversion de {nombre_persona_dos} es de ${inversion_persona_dos:,} y su porcentaje es de {porcentaje_persona_dos}%')
print(f'El valor de la inversion de {nombre_persona_tres} es de ${inversion_persona_tres:,} y su porcentaje es de {porcentaje_persona_tres}%')
