# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:36:57 2018

@author: alexa
"""
#import arcpy
#from arcpy import env
from pruebalectura import modelo
from calc import calcular
from Graficar import GraficarG
from CalculoElongacion import calcularElongacion
     
obj1 = modelo()      
obj1.readArea("C:/Users/alexa/Desktop/Indices Geomorfológicos/ElongaciónCuenca/elongaciondecuenca(arcgis)/poligono_cuenca")
obj1.readDistancia("C:/Users/alexa/Desktop/Indices Geomorfológicos/ElongaciónCuenca/elongaciondecuenca(arcgis)/largo_cuenca")

o = calcularElongacion(obj1.get_Area(), obj1.get_Distancias())

obj1.readPointsShape("C:/Users/alexa/Desktop/Indices Geomorfológicos/Gradiente/perfil del gradiente(arcgis)/puntos_gradiente.shp")

obj2 = calcular(obj1.get_Zcoor(), obj1.get_Dist())      
ob = GraficarG(obj1.get_Zcoor(), obj1.get_Dist(), obj2.get_SL_K())
ob.graficarGRF()
    
#arcpy.GetParameterAsText(0)