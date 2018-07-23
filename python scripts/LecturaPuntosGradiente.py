# -*- coding: utf-8 -*-

"""
Created on Thu Apr 26 20:55:47 2018

@author: alexa
"""
import pandas as pd
import shapefile
from CalculoDistancia import calculosD

class lecturaGradiente():
   
    def readPointsShape(self, directory):
        #Inicializacion
        self.num_conver_A = []
        self.num_conver_B = []
        self.num_conver_C = []
        self.info_sesg = []
        self.clc = calculosD()
        #Lee la data del archivo
        sf = shapefile.Reader(directory)
       
        fields = [x[0] for x in sf.fields][1:]      
        records = sf.records()      
        # Se escribe en el datagrama
        self.data = pd.DataFrame(columns=fields, data=records)
        # Posibles nombres para los puntos
        fieldsnamesX = ["POINT_X","X"]
        fieldsnamesY = ["POINT_Y","Y"]
        fieldsnamesZ = ["Z"] 
        
        # Asigna las nombres de las columnas
        for a in fields:
            if a in fieldsnamesX:
                nameX = a
            if a in fieldsnamesY:
                nameY = a
            if a in fieldsnamesZ:
                nameZ = a
        
        X = self.data[nameX]
        for i in X:
            
            try:
                self.num_conver_A.append(float(i))

            except ValueError:
                self.info_sesg.append(i)

        Y = self.data[nameY]
        for i in Y:         
            try:
                self.num_conver_B.append(float(i))

            except ValueError:
                self.info_sesg.append(i)
             
        ZC = self.data[nameZ]
        for i in ZC:
            try:
               self.num_conver_C.append(float(i))
               
            except ValueError:
                self.info_sesg.append(i)        

        self.clc.calcularDistacia(X,Y, ZC)
        
    def get_Zcoor(self):
       
        return self.num_conver_C
    
    def get_Dist(self):
        return self.clc.GetDistancias()
    
    def get_Area(self):
        return self.num_conver_Ar
    

obj = lecturaGradiente()
obj.readPointsShape("C:/Users/alexa/Desktop/Indices Geomorfológicos/Gradiente/perfil del gradiente(arcgis)/puntos_gradiente")
obj.get_Dist()
