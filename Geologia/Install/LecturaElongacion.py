# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:27:28 2018

@author: Ing. Santiago Quiñones, Ing María FeRnanda Guarderas, Nelson Aranda
"""
    
import pandas as pd
import shapefile
from CalculoDistancia import calculosD

class lecturaElongacion():
   
    def readPointsShape(self, directory):
        #Inicializacion de variables 
        num_Zmax = []
        num_Zmin = []
        self.clc = calculosD()
        self.areas = []
        # Variables de contadores
        cont1 = 0 
        cont2 = 0
        # Variables para eliminar duplicados
        max_drop=[]
        min_drop=[]
        # Variables para almacenar los puntos
        self.pointXmax = [] 
        self.pointYmax = [] 
        self.pointZmax = []
        self.pointXmin = [] 
        self.pointYmin = [] 
        self.pointZmin = []
        
        # Lee la data del archivo
        sf = shapefile.Reader(directory)
       
        fields = [x[0] for x in sf.fields][1:]      
        records = sf.records() 
        
        # Se escribe en el datagrama y se agrupa por Shape_Area
        self.data = pd.DataFrame(columns=fields, data=records)  
        s = self.data[['X', 'Y', 'Z']].groupby(self.data['Shape_Area'])
        
        # Se obtienen los max y min de los datos seleccionados
        maxT = pd.DataFrame(s['Z'].max())
        minT = pd.DataFrame(s['Z'].min())

        # Asignacion  valores min y max a listas
        for i in maxT['Z']:
            num_Zmax.append(i)
        
        for i in minT['Z']:
            num_Zmin.append(i)
        
        #Extraccion de fila correspondiente a los max valores
        for names, groups in s:
            self.areas.append(names)
            max_values = groups[groups['Z'] == num_Zmax[cont1]]
            # Almacena temporalmente lo data del punto seleccionado
            tempMax = max_values.drop_duplicates(subset=None, keep="first", inplace=False)
            #print("puntos maximos")
            #print(tempMax)
            # Comprobacion de tamano para escoger el primer caso
            if len(tempMax) > 1:
                #print("================= Puntos Encontados con la misma altura")
                #print(a)
                p = tempMax[tempMax['X'] == tempMax['X'].max()]
                #print("Punto escogiendo X minimo")
                #print("", p)
                max_drop.append(p)
            else:
                max_drop.append(tempMax)      
            cont1 = cont1 + 1

        #Extraccion de fila correspondiente a los min valores
        for names, groups in s:
            min_values = groups[groups['Z'] == num_Zmin[cont2]]
            # Almacena temporalmente lo data del punto seleccionado y elimina duplicados
            tempMin = min_values.drop_duplicates(subset=None, keep="first", inplace=False)
            #print("puntos minimos")
            #print(tempMin)
            # Comprobacion de ta`mano para escoger el dato correcto
            if len(tempMin) > 1:
                #print("================= Puntos Encontados con la misma altura")
                #print(a)
                p = tempMin[tempMin['X'] == tempMin['X'].min()]
                #print("Punto escogiendo X minimo")
                #print("", p)
                min_drop.append(p)
            else:
                min_drop.append(tempMin)           
            cont2 = cont2 + 1
  
        # Reemplazo de los datos por posibles inconsistencias en el formato de origen
        for rows in max_drop:
            for x in rows.X:
                if (isinstance(x, float)):
                    self.pointXmax.append(float(x))
                else:
                    # Reemplaza la coma por el punto
                    xm = x.replace(',','.')
                    self.pointXmax.append(float(xm))
                    
            for y in rows.Y:
                if (isinstance(y, float)):
                    self.pointYmax.append(float(y))          
                else:
                    # Reemplaza la coma por el punto
                    ym = y.replace(',','.')
                    self.pointYmax.append(float(ym))
                    
            for z in rows.Z:
                if (isinstance(z, float)):
                    self.pointZmax.append(float(z))
                else:
                    # Reemplaza la coma por el punto
                    zm = y.replace(',','.')
                    self.pointZmax.append(float(zm))
        
        # Reemplazo para los valores minimos
        for rows in min_drop:
            for x in rows.X:
                if (isinstance(x, float)):
                    self.pointXmin.append(float(x))
                else:
                    xm = x.replace(',','.')
                    self.pointXmin.append(float(xm))

            for y in rows.Y:
                if (isinstance(y, float)):
                    self.pointYmin.append(float(y))
                else:
                    ym = y.replace(',','.')
                    self.pointYmin.append(float(ym))
                    
            for z in rows.Z:
                if (isinstance(z, float)):
                    self.pointZmin.append(float(z))
                else:
                    zm = z.replace(',','.')
                    self.pointZmin.append(float(zm))
        
        # Se envia la data a procesarse
        self.clc.calcularDistaciaElongacion(self.pointXmax, self.pointXmin, self.pointYmax, 
                                            self.pointYmin, self.pointZmax, self.pointZmin)
    
    def get_Dist(self):
        return self.clc.GetDistancias()

    def get_Area(self):
        return self.areas
    
    def get_XcooMINr(self):    
        return self.pointXmin
    
    def get_XcoorMAX(self):    
        return self.pointXmax
    
    def get_YcoorMIN(self):    
        return self.pointYmin
    
    def get_YcoorMAX(self):    
        return self.pointYmax
    
    def get_ZcoorMIN(self):    
        return self.pointZmin
    
    def get_ZcoorMAX(self):    
        return self.pointZmax
 