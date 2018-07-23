# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:07:16 2018

@author: alexa
"""
import math

class calcularElongacion():
    
    def __init__(self, Area, Dist):      
        self.calcRadioElongacion(Area, Dist)      
    
    def calcDiametro(self, Area):
        Rc = 2 * math.sqrt(Area/math.pi)
        return Rc
    
    def calcRadioElongacion(self, Area, Dist):
        cont = 0
        self.respuesta = []
        self.valor = []
        for area in Area:
            print("=========================================",cont)
            print("=> ",area)
            dist = Dist[cont]
            rc = self.calcDiametro(area)
            Re = rc/dist
            print("=> ",Re)
            if (Re >= 0.4 and Re < 0.55):  
                txt = " => %.3f: Altamente Elongado" % Re
                
                resp = str(area) + txt
                print(resp)
            elif (Re >= 0.55 and Re < 0.7):
                txt = " => %.3f Elongado" % Re
                resp = str(area) + txt
                print(resp)
            elif (Re >= 0.7 and Re < 0.85):
                txt = " => %.3f Levemente Elongado" % Re
                resp = str(area) + txt
                print(resp)
            elif (Re >= 0.85 and Re < 1):
                txt = " => %.3f No Elongado" % Re
                resp = str(area) + txt
                print(resp)
            cont = cont + 1
    