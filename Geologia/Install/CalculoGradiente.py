# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:15:11 2018

@author: Ing. Santiago Quiñones, Ing María FeRnanda Guarderas, Nelson Aranda
"""

import numpy as np

class calcularGradiente():

    def calcular_SLK(self, Zcoor, Dist):
        # Inicializacion de variables
        self.num_conver_A = Zcoor
        self.num_conver_B = Dist 
        
        # Variable para almacenar distancias
        sublista_Dis = []
        # Variable para almacenar alturas
        sublista_Alt = []   
        
        self.SLK = []
        #Iguala el vector agregando cero al inicio
        self.SLK.append(0)

        for cont in range(len(self.num_conver_A)):  
            # Agregado de valores a las sublistas
            sublista_Alt.append(self.num_conver_A[cont])
            sublista_Dis.append(self.num_conver_B[cont])
            
            if(len(sublista_Dis) == 2):
                
                #Aplicación de la fórmula para calcular el gradiente
                result = (((sublista_Alt[0]-sublista_Alt[1])/(sublista_Dis[1]-
                           sublista_Dis[0]))*(sublista_Dis[0]+((sublista_Dis[1]
                           -sublista_Dis[0])/2)))*-1
                
                self.SLK.append(result)
                
                # Eliminación del valor previo de las sublistas
                del sublista_Alt[0]
                del sublista_Dis[0]


    def calc_SL_KMedia(self):
        self.slkMedia = []
        # Calcula el promedio de todo el vector
        media = np.mean(self.SLK)
        print("Media", media)
        print(np.average(self.SLK))
        for numSLK in self.SLK:
            # Aplicación de formula
            self.slkMedia.append(numSLK/media)
    
    def calc_DispPuntoMedio(self):
        # Variables
        sublist_Dist = [] 
        self.DispPunto = []
        # Relleno de vector
        self.DispPunto.append(0)
        for i in self.num_conver_B: 
            # Agregado de valores a las sublista
            sublist_Dist.append(i)
            if(len(sublist_Dist) == 2):
                # Aplicación de fórmula
                result = sublist_Dist[0]+((sublist_Dist[1]-sublist_Dist[0])/2)
                self.DispPunto.append(result)
                
                # Eliminación del valor previo de la sublista
                del sublist_Dist[0]
   

    def get_SL_K(self):   
        return self.SLK
    
    def getSL_KPuntoMedio(self):
        self.calc_DispPuntoMedio()
        return self.DispPunto
        
    def getSL_K_Media(self):
        self.calc_SL_KMedia()
        return self.slkMedia
    
    def presentarSL(self):
        print("xxxxxxxx SLK xxxxxxxxxx\n")
        for i in self.SLK:
            print(i)
    

