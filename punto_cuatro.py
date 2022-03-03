# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:22:40 2022

@author: dcastro31
"""

# 4. Un alumno desea saber cuál será su calificación final en la materia de
# fundamentos de programación. Dicha calificación se compone de los
# siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
# calificación de un examen en clase y 20% de la calificación de un proyecto
# final.

nombre_alumno = (input('Digite el nombre del alumno: '))
taller1 = float(input('Digite nota del taller uno: '))
taller2 = float(input('Digite nota del taller dos: '))
taller3 = float(input('Digite nota del taller tres: '))
promedio_talleres = (taller1 + taller2 + taller3) / 3
examen = float(input('Digite nota del examen: '))
proyecto = float(input('Digite nota del proyecto: '))
final = (promedio_talleres * 0.50) + (examen * 0.30) + (proyecto * 0.20)
print(f'La nota final del alumno {nombre_alumno} es: {final}')