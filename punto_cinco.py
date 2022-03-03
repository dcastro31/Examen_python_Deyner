# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:36:26 2022

@author: dcastro31
"""

# 5. Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el
# porcentaje de alumnos de cada uno de los cursos.

alumno_redes = int(input('Digite la cantidad de alumnos de redes: '))
alumno_contabilidad = int(input('Digite la cantidad de alumnos de contabilidad: '))
alumno_diseño = int(input('Digite la cantidad de alumnos de diseño: '))
total = (alumno_redes + alumno_contabilidad + alumno_diseño)
print(f'La cantidad de alumnos del curso es: {total}')
porcentaje_redes = (alumno_redes / total) * 100
porcentaje_contabilidad = (alumno_contabilidad / total) * 100
porcentaje_diseño = (alumno_diseño / total) * 100
print(f'El porcentaje de alumnos de redes es: {porcentaje_redes}%')
print(f'El porcentaje de alumnos de contabilidad es: {porcentaje_contabilidad}%')
print(f'El porcentaje de alumnos de diseño es: {porcentaje_diseño}%')