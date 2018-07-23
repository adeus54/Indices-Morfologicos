# -*- coding: utf-8 -*-
"""
Created on Fri May  4 01:21:32 2018

@author: alexa
"""
#from matplotlib import plot as pl
from pruebalectura import modelo
from calc import calcular
from matplotlib import pyplot as plt

class GraficarG():
    
    def __init__(self, Zcoor, dist, slk):
        self.Zcoor = Zcoor
        self.Dist = dist
        self.SLK = slk
        
    def graficarGRF(self):
        #Iguala el vector agregando cero al inicio
        relleno = [0]
        for i in self.SLK:
            relleno.append(i)   
        
        #Crea la grafica
        plt.figure()
        plt.plot(self.Dist, self.Zcoor, 'b-', label = 'Perfil')
        plt.xlabel("Dist")
        plt.ylabel("Zcoor")
        plt.grid(True)
        plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
        plt.legend(loc="best")  
        
        #Se agrega doble eje 
        plt.twinx()   
        plt.plot(self.Dist, relleno, 'r-.', label = 'Gradiente')  
        plt.ylabel("SL")
        plt.legend(loc="best")
        #Se da nuevo escala
        #plt.ylim(0, 100000)
        
        plt.show()
        
#ob = modelo()
#ob.readPointsShape("C:/Users/alexa/Desktop/Indices Geomorfológicos/Gradiente/perfil del gradiente(arcgis)/puntos_gradiente.shp")
#o = calcular(ob.get_Zcoor(), ob.get_Dist())      
#obj = GraficarG(ob.get_Zcoor(), ob.get_Dist(), o.get_SL_K())
#obj.graficarGRF()