# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:37:18 2018

@author: alexa
"""

from LecturaElongacion import lecturaElongacion
from CalculoElongacion import calcularElongacion

lte = lecturaElongacion()
lte.readPointsShape("C:/Users/alexa/Desktop/Datos/Datos/cuencas segundo orden/puntos_cuenca2do")
distancias = lte.get_Dist()
areas = lte.get_Area()

ce = calcularElongacion(areas, distancias)
