# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:53:37 2018

@author: alexa
"""
import math

class calculosD:
    
    def calcularDistacia(self, X, Y, Z):
        self.num_conver_X = X
        self.num_conver_Y = Y
        self.num_conver_Z = Z
        self.Dist = []
        e = []
        d = []
        f = []
        mins = 0
        self.Dist.append(mins)
        for i in self.num_conver_X:  
            d.append(i)
            e.append(self.num_conver_Y[mins])
            f.append(self.num_conver_Z[mins])
            
            if(len(e) == 2):
                    result = math.sqrt(math.pow((d[1] - d[0]), 2) + math.pow((e[1]-[e[0]]),2) + math.pow((f[1]-[f[0]]),2))
                    self.Dist.append(result)
                    del d[0]
                    del e[0]
                    del f[0]             
            mins = mins + 1

    def calcularDistaciaElongacion(self, Xmax, Xmin,Ymax, Ymin, Zmax, Zmin):
        self.Dist = []
        cont = 0
        
        for i in Xmax:
            result = math.sqrt(math.pow((Xmax[cont] - Xmin[cont]),2) + 
                               math.pow((Ymax[cont] - Ymin[cont]),2))
            #math.pow((Zmax[cont] - Zmin[cont]),2)
            self.Dist.append(result)
            cont = cont + 1
        
    def GetDistancias(self):
        return self.Dist