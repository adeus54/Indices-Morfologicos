# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:27:28 2018

@author: alexa
"""
    
import pandas as pd
import shapefile
from CalculoDistancia import calculosD

class lecturaElongacion():
   
    def readPointsShape(self, directory):
        #Inicializacion
        num_Zmax = []
        num_Zmin = []
        self.clc = calculosD()
        self.areas = []
        #Lee la data del archivo
        sf = shapefile.Reader(directory)
       
        fields = [x[0] for x in sf.fields][1:]      
        records = sf.records() 
        
        # Se escribe en el datagrama y se agrupa por Shapearea
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
                    
        #inicializacion de contadores
        cont1 = 0 
        cont2 = 0
        max_drop=[]
        min_drop=[]
        pointXmax = [] 
        pointYmax = [] 
        pointZmax = []
        pointXmin = [] 
        pointYmin = [] 
        pointZmin = []
        
        #Extraccion de fila correspondiente a los max valores
        for names, groups in s:
            self.areas.append(names)
            #print(names)
            max_values = groups[groups.Z == num_Zmax[cont1]]        
            a = max_values.drop_duplicates(subset=None, keep="first", inplace=False)
            # Comprobacion de tamano 
            if len(a) > 1:
                b = a[:1]
                max_drop.append(b)
            else:
                max_drop.append(a)
                
            cont1 = cont1 + 1
        #Extraccion de fila correspondiente a los min valores
        for names, groups in s:
            min_values = groups[groups.Z == num_Zmin[cont2]]
            a = min_values.drop_duplicates(subset=None, keep="first", inplace=False)
            # Comprobacion de tamano
            if len(a) > 1:
                b = a[:1]
                min_drop.append(b)
            else:
                min_drop.append(a)        
            
            cont2 = cont2 + 1
  
        # Reemplazo de los datos 
        for rows in max_drop:
            for x in rows.X:
                xm = x.replace(',','.')
                pointXmax.append(float(xm))
            for y in rows.Y:
                ym = y.replace(',','.')
                pointYmax.append(float(ym))
          
            pointZmax.append(float(rows.Z))
        
        for rows in min_drop:
            for x in rows.X:
                xm = x.replace(',','.')
                pointXmin.append(float(xm))
            for y in rows.Y:
                ym = y.replace(',','.')
                pointYmin.append(float(ym))
          
            pointZmin.append(float(rows.Z))
        
        self.clc.calcularDistaciaElongacion(pointXmax, pointXmin, pointYmax, 
                                            pointYmin, pointZmax, pointZmin)

    
    def get_Dist(self):
        #print(self.clc.GetDistancias())
        return self.clc.GetDistancias()

    def get_Area(self):
        #print(self.areas)
        return self.areas

#obj = lecturaElongacion()
#obj.readPointsShape("C:/Users/alexa/Desktop/Datos/Datos/cuencas segundo orden/puntos_cuenca2do")
#obj.readAreaPoligons("C:/Users/alexa/Desktop/Datos/Datos/cuencas segundo orden/poly_cuencas2do")
#obj.get_Dist()
#obj.get_Area()