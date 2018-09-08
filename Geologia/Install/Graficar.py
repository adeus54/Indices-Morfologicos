# -*- coding: utf-8 -*-
"""
Created on Fri May  4 01:21:32 2018

@author: Ing. Santiago Quiñones, Ing María FeRnanda Guarderas, Nelson Aranda
"""

from matplotlib import pyplot as plt
import pylab

class GraficarG(object):
    
    def graficarGRF(self, Zcoor, dist, slK, lim1I, lim1S, lim2I, lim2S ):
        # Inicializacion de variable
        Zcoor = Zcoor
        Dist = dist
        SL_K = slK
        Inf_I = int(lim1I)
        Inf_S = int(lim1S)
        Inf_I2 = int(lim2I)
        Inf_S2 = int(lim2S)
        # Se crea el grafico
        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        # Primer eje
        ax1.plot(Dist, Zcoor, 'b-', linewidth = 1, label = 'Perfil del rio')
        
        # Activacion de lineas de dibujo
        ax1.grid(True)
        ax1.grid(color = '0.5', linestyle = '--', linewidth = 1)
        
        # Segundo eje
        ax2.plot(Dist, SL_K, 'r-', marker = '.', linewidth = 1, label = 'Gradiente')
        
        # Aplicacion de los nombres de los ejes
        ax1.set_xlabel('Distacia')
        ax1.set_ylabel('Zcoor(Altura)', color='b')
        ax2.set_ylabel('SL_K', color='r')
        
        # Agragado de leyendas
        ax1.legend(loc = 2)
        ax2.legend(loc = 9)
        
        """Limite estatico para que los puntos iniciales y finales esten alejados 
        del borde"""
        ax1.set_xlim(-200, Dist[len(Dist) -1] + 300)
        
        # Se agrega los limites para cada una de los ejes
        ax1.set_ylim(Inf_I, Inf_S)
        ax2.set_ylim(Inf_I2, Inf_S2)
        
        # Muestra la imagen
        plt.show()
       