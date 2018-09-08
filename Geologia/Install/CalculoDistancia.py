# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:53:37 2018

@author: Ing. Santiago Quiñones, Ing María FeRnanda Guarderas, Nelson Aranda
"""
import math

class calculosD:
    
    def calcularDistaciaGradiente(self, X, Y, Z):
        num_conver_X = X
        num_conver_Y = Y
        num_conver_Z = Z
        # Variables para el almacenamiento de la distancia
        self.Dist_Final = []
        Dist_Prev = []
        # Variables para almacenar una parte de los datos
        subList_X = []
        subList_Y = []
        subList_Z = []
        # Relleno de la primera posicion
        inicial = 0
        Dist_Prev.append(inicial)
        self.Dist_Final.append(inicial)
        # Contador para las posiciones
        cont = 0
        for i in range(len(num_conver_X)):  
            # Relleno de las sublistas
            subList_X.append(num_conver_X[i])
            subList_Y.append(num_conver_Y[i])
            subList_Z.append(num_conver_Z[i])
            
            # Si las sublistas tienen dos valores se procede con el calculo
            if(len(subList_X) == 2):
                
                    # Aplicacion de la formula para calcular distancias
                    result = math.sqrt(math.pow((subList_X[1] - subList_X[0]), 2) + 
                                       math.pow((subList_Y[1]- subList_Y[0]),2))
                    
                    # Se guarda la distancia previa acumulada
                    Dist_Prev.append(result + Dist_Prev[cont])
                    
                    #Guarda la distancia final sumandole la distancia previa
                    self.Dist_Final.append(Dist_Prev[cont] + result)
                    
                    # Vacia una posicion para un nuevo llenado
                    del subList_X[0]
                    del subList_Y[0]
                    
                    # Se incremeta el contador
                    cont = cont + 1
        
    def calcularDistaciaElongacion(self, Xmax, Xmin,Ymax, Ymin, Zmax, Zmin):
        self.Dist = []
        
        for cont in range(len(Xmax)):
            
            # Aplicacion de la formula para calcular distancias
            result = math.sqrt(math.pow((Xmax[cont] - Xmin[cont]),2) + 
                               math.pow((Ymax[cont] - Ymin[cont]),2) +
                               math.pow((Zmax[cont] - Zmin[cont]),2))
            self.Dist.append(result)
        
    def GetDistancias(self):
        return self.Dist
    
    def GetDistanciasGradiente(self):
        return self.Dist_Final