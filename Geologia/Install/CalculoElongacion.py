# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:07:16 2018

@author: Ing. Santiago Quiñones, Ing María FeRnanda Guarderas, Nelson Aranda
"""
import math

class calcularElongacion():    
    
    def calcDiametro(self, Area):
        #Calculo del diametro de un circulo
        Rc = 2 * math.sqrt(Area/math.pi)
        return Rc
    
    def calcRadioElongacion(self, Area, Dist):
        cont = 0
        self.respuesta = []
        self.valor = []
        
        for area in Area:
            print("=> ",area)
            dist = Dist[cont]
            rc = self.calcDiametro(area)
            #Calculo del radio de elongación
            Re = rc/dist
            print("=> ",Re)
            
            #Clasificación del radio de elongación por rango
            if (Re < 0.22):
                txt = "Muy alargada" 
                self.respuesta.append(txt)
                self.valor.append(Re)
            elif (Re >= 0.22 and Re < 0.30):  
                txt = "Alargada" 
                self.respuesta.append(txt)
                self.valor.append(Re)
            elif (Re >= 0.30 and Re < 0.37):
                txt = "Ligeramente alargada" 
                self.respuesta.append(txt)
                self.valor.append(Re)
            elif (Re >= 0.37 and Re < 0.45):
                txt = "Ni alargada ni ensanchada" 
                self.respuesta.append(txt)
                self.valor.append(Re)
            elif (Re >= 0.45 and Re <= 0.60):
                txt = "Ligeramente ensanchada" 
                self.respuesta.append(txt)
                self.valor.append(Re)
            elif (Re >= 0.60 and Re <= 0.80):
                txt = "Ensanchada" 
                self.respuesta.append(txt)
                self.valor.append(Re)
            elif (Re >= 0.80 and Re <= 1.20):
                txt = "Muy ensanchada" 
                self.respuesta.append(txt)
                self.valor.append(Re)
            elif (Re >= 1.20):
                txt = "Rodeando el desagüe"
                self.respuesta.append(txt)
                self.valor.append(Re)
            cont = cont + 1
    
    def getClasificacion(self):
        return self.respuesta
    
    def getValor_Clasificacion(self):
        return self.valor
    
        