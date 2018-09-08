# -*- coding: utf-8 -*-

"""
Created on Thu Apr 26 20:55:47 2018

@author: Ing. Santiago Quiñones, Ing María FeRnanda Guarderas, Nelson Aranda
"""
import pandas as pd
import shapefile
from CalculoDistancia import calculosD

class lecturaGradiente():
   
    def readPointsShape(self, directory):
        self.num_conver_Z = []
        self.clc = calculosD()
        
        # Variables para almacenar los puntos
        self.pointX = [] 
        self.pointY = [] 
        self.pointZ = []
        
        #Lee la data del archivo
        sf = shapefile.Reader(directory)
        
        fields = [x[0] for x in sf.fields][1:]      
        records = sf.records()   
        
        # Se escribe la data en un datagrama
        self.data = pd.DataFrame(columns=fields, data=records)
        
        # Posibles nombres para los puntos
        fieldsnamesX = ["POINT_X","X"]
        fieldsnamesY = ["POINT_Y","Y"]
        fieldsnamesZ = ["Z"] 
        
        # Asigna las nombres de las columnas
        for a in fields:
            if a in fieldsnamesX:
                self.nameX = a
            if a in fieldsnamesY:
                self.nameY = a
            if a in fieldsnamesZ:
                self.nameZ = a
        # Ordena de menor a mayor       
        sort_ed = self.data[[self.nameX, self.nameY, self.nameZ]].sort_values(by= self.nameZ, ascending=True)
        
        # Asigna los datos obtenidos a una lista
        for rowsX in sort_ed[self.nameX]:
            self.pointX.append(float(rowsX))
        for rowsY in sort_ed[self.nameY]:
            self.pointY.append(float(rowsY))
        for rowsZ in sort_ed[self.nameZ]:
            self.pointZ.append(float(rowsZ))        
              
        # Se manda a calcular las distancias 
        self.clc.calcularDistaciaGradiente(self.pointX, self.pointY, self.pointZ)
        
    def get_Point_X(self):
        return self.pointX
        
    def get_Point_Y(self):
        return self.pointY
    
    def get_Zcoor(self):    
        return self.pointZ
    
    def get_Dist(self):
        return self.clc.GetDistanciasGradiente()
    
    def get_namesFields(self):
        names = [self.nameX, self.nameY, self.nameZ]
        return names
