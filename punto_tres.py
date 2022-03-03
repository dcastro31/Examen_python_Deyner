# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:12:24 2022

@author: dcastro31
"""

# 3. Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
# ventas efectuadas en el mes. El vendedor desea saber cuanto dinero en
# total obtendrá por las ventas que realiza en el mes. Desarrolle un programa
# en Python que permita mostrar el valor ganado por comisión y el valor total
# a pagar al vendedor.

sueldo_base = int(input('Digite valor del sueldo del vendedor: $'))
total_ventas = int(input('Digite valor total de lo vendido: $'))
valor_comision = total_ventas * 0.15
total_pagar = sueldo_base + valor_comision

print(f'El total ganado del vendedor por cosion es: ${valor_comision:,}')
print(f'El valor total pagado a el vendedor es: ${total_pagar:,}')