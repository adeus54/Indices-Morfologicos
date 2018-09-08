# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:37:18 2018

@author: Ing. Santiago Quiñones, Ing María FeRnanda Guarderas, Nelson Aranda
"""
import arcpy
from LecturaElongacion  import lecturaElongacion
from CalculoElongacion import calcularElongacion

PointsDir = arcpy.GetParameterAsText(0)
PoligonsDir = arcpy.GetParameterAsText(1)
SaveDir = arcpy.GetParameterAsText(2)

# Campos Nuevos a crear
nuevosCampos = ["MINPOINT_X", "MINPOINT_Y", "MINPOINT_Z", "MAXPOINT_X", 
                "MAXPOINT_Y", "MAXPOINT_Z","VALOR_OBT", "CLASIF"]

lectura = lecturaElongacion()
lectura.readPointsShape(PointsDir)
distancias = lectura.get_Dist()
areas = lectura.get_Area()

# Puntos Selecionados
xCoorm = lectura.get_XcooMINr()
xCoorM = lectura.get_XcoorMAX()
yCoorm = lectura.get_YcoorMIN()
yCoorM = lectura.get_YcoorMAX()
zCoorm = lectura.get_ZcoorMIN()
zCoorM = lectura.get_ZcoorMAX()

# Envio de la data a calcularse
cle = calcularElongacion()
cle.calcRadioElongacion(areas, distancias) 
  
clasificacion = cle.getClasificacion();
valor = cle.getValor_Clasificacion();
# Crea una copia del shape para modificarlo
arcpy.CopyFeatures_management(PoligonsDir, SaveDir)
SaveDirr = SaveDir.replace("\\","/")
    
# Agrega los nueevos campos al shape
for campo in nuevosCampos:
   if campo == "CLASIF":
       arcpy.AddField_management(SaveDirr + ".shp", campo, "TEXT", "", "", "", "", "NULLABLE")
   else:
       arcpy.AddField_management(SaveDirr + ".shp", campo, "DOUBLE", "", "", "", "", "NULLABLE")


for i in range(len(areas)):
    # Actualizacion del shape
    #arcpy.AddMessage(" Pasa por aqui")
    cursor = arcpy.UpdateCursor(SaveDirr + ".shp")
    for row in cursor:
        if row.Shape_Area == areas[i]:  
            row.setValue("MINPOINT_X", xCoorm[i])
            row.setValue("MINPOINT_Y", yCoorm[i])
            row.setValue("MINPOINT_Z", zCoorm[i])
            row.setValue("MAXPOINT_X", xCoorM[i])
            row.setValue("MAXPOINT_Y", yCoorM[i])
            row.setValue("MAXPOINT_Z", zCoorM[i])
            row.setValue("VALOR_OBT", valor[i])
            row.setValue("CLASIF", clasificacion[i])
            cursor.updateRow(row)
