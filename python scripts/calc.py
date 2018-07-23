# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:15:11 2018

@author: alexa
"""

from LecturaPuntosGradiente import lecturaGradiente
import numpy as np

class calcular():
    
    def __init__(self, Zcoor, Dist):     
        self.calcular_SL(Zcoor, Dist)
        self.calc_SL_K(Zcoor, Dist)


    def calcular_SL(self, Zcoor, Dist):
        self.num_conver_A = Zcoor
        self.num_conver_B = Dist
        e = []
        d = []     
        self.SL = []
        
        mins = 0
        for i in self.num_conver_A:  
            d.append(i)
            e.append(self.num_conver_B[mins])
            
            if(len(e) == 2):
                    result = (((d[0]-d[1])/(e[1]-e[0]))*(e[0]+((e[1]-e[0])/2)))-1
                    self.SL.append(result)
                    del d[0]
                    del e[0]
                                 
            mins = mins + 1
        
        
    def calc_SL_K(self, Zcoor, Dist):
        self.num_conver_A = Zcoor
        self.num_conver_B = Dist
        e = []
        d = []     
        self.SLK = []
        
        mins = 0
        for i in self.num_conver_A:  
            d.append(i)
            
            e.append(self.num_conver_B[mins])
            
            if(len(e) == 2):
                    result = ((d[0]-d[1])/(e[1]-e[0]))*(e[0]+((e[1]-e[0])/2))*-1
                    self.SLK.append(result)
                    del d[0]
                    del e[0]
                                 
            mins = mins + 1   


    def calc_SL_KMedia(self):
        self.slkMedia = []
        media = np.average(self.SLK)
        for i in self.SLK:
            self.slkMedia.append(i/media)
        
    
    def calc_DispPuntoMedio(self):
        d = [] 
        self.DispPunto = []
        for i in self.num_conver_B:
            d.append(i)
            if(len(d) == 2):
                
                result = d[0]+((d[1]-d[0])/2)
                self.DispPunto.append(result)
                del d[0]
                
            
    def calc_Resultado(self):
        e = []
        d = []     
        self.resultado = []
        
        mins = 0
        for i in self.num_conver_A:  
            d.append(i)
            e.append(self.num_conver_B[mins])
            
            if(len(e) == 2):
                    result = ((e[1]-e[0])*(d[1]+d[0]))
                    self.resultado.append(result)
                    del d[0]
                    del e[0]
                                 
            mins = mins + 1 
           

    def get_SL(self):
        return self.SL
   

    def get_SL_K(self):
        return self.SLK
    
    
    def presentarSL(self):
        print("xxxxxxxx SL xxxxxxxxxx\n")
        for i in self.SL:
            print(i)
    

#obj = lecturaGradiente()
#obj.readPointsShape("C:/Users/alexa/Desktop/Indices Geomorfológicos/Gradiente/perfil del gradiente(arcgis)/puntos_gradiente")
#o = calcular(obj.get_Zcoor(), obj.get_Dist())  
#o.presentarSL()