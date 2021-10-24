# -*- coding: utf-8 -*-

"""
Created on Thu Apr 26 20:55:47 2018

@author: Ing. Santiago Quiñones, Ing María FeRnanda Guarderas, Nelson Aranda
"""
import pandas as pd
import shapefile
import arcpy
from CalculoDistancia import calculosD


class lecturaGradiente():

    def readPointsShape(self, directory):
        self.num_conver_Z = []
        self.clc = calculosD()

        # Variables para almacenar los puntos
        self.pointX = []
        self.pointY = []
        self.pointZ = []

        try:
            # Lee la data del archivo
            sf = shapefile.Reader(directory)
            fields = [x[0] for x in sf.fields][1:]
            records = [y[:] for y in sf.records()]

            # Se escribe la data en un datagrama
            self.data = pd.DataFrame(columns=fields, data=records)

            # Posibles nombres para los puntos
            fieldsnamesX = ["POINT_X", "X"]
            fieldsnamesY = ["POINT_Y", "Y"]
            fieldsnamesZ = ["Z"]
            
            
            # Asigna las nombres de las columnas
            x = [ele for ele in fieldsnamesX if (ele in fields)]
            y = [ele for ele in fieldsnamesY if (ele in fields)]
            z = [ele for ele in fieldsnamesZ if (ele in fields)]

            if x is not [] and y is not [] and z is not []:
                self.nameX = x[0]
                self.nameY = y[0]
                self.nameZ = z[0]

        except shapefile.ShapefileException:
            arcpy.AddError("No se ha podido leer el archivo especificado")
            arcpy.AddMessage("{0}".format(directory))
        except IndexError:
                arcpy.AddError("El archivo de entrada debe contener los puntos del gradiente a calcular.")
                arcpy.AddError("Los nombres de las columnas pueden ser: \nAtributo X como: {0} o {1}\nAtributo Y como: {"
                               "2} o {3} \nAtributo Z como: {4}".format(fieldsnamesX[0], fieldsnamesX[1], fieldsnamesY[
                    0], fieldsnamesY[1], fieldsnamesZ[0]))
        else:
            # Ordena de menor a mayor
            sort_ed = self.data[[self.nameX, self.nameY, self.nameZ]].sort_values(by=self.nameZ, ascending=True)

            # Asigna los datos obtenidos a una lista
            for rowsX in sort_ed[self.nameX]:
                self.pointX.append(float(rowsX))
            for rowsY in sort_ed[self.nameY]:
                self.pointY.append(float(rowsY))
            for rowsZ in sort_ed[self.nameZ]:
                self.pointZ.append(float(rowsZ))

            # Se calculan las distancias
            self.clc.calcularDistaciaGradiente(self.pointX, self.pointY, self.pointZ)
            return 1
        return 0

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
