# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:03:01 2022

@author: dcastro31
"""

# 1. Una Institución educativa ha recibido una donación especial que será 
# repartida entre las carreras de Telecomunicaciones, Sistemas,
# Administración y Contabilidad de la siguiente forma:
# a. Telecomunicaciones 10% del valor dado a sistemas
# b. Sistemas: 25% del valor dado a Administración
# c. Administración: 35% del valor de la donación
# d. Contabilidad: lo que resta de la donación

donacion = int(input('Digite valor de donacion: $'))
administracion = donacion * 0.35
sistemas = administracion * 0.25
telecomunicaciones = sistemas * 0.10
contabilidad = (donacion - (administracion + sistemas + telecomunicaciones))
print(f'El valor de la donacion es: ${donacion:,}')
print(f'El valor dado a Telecomunicaciones es: ${telecomunicaciones:,}')
print(f'El valor dado a Sistemas es: ${sistemas:,}')
print(f'El valor dado a Administración es: ${administracion:,}')
print(f'El valor dado a Contabilidad es: ${contabilidad:,}')