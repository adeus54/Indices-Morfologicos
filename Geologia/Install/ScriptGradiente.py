# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:36:57 2018

@author: Ing. Santiago Quiñones, Ing María FeRnanda Guarderas, Nelson Aranda
"""
import arcpy
from LecturaPuntosGradiente import lecturaGradiente
from CalculoGradiente import calcularGradiente
from Graficar import GraficarG

# Datos de entrada
PointsDir = arcpy.GetParameterAsText(0)
SaveDir = arcpy.GetParameterAsText(1)
lim1_In = arcpy.GetParameterAsText(2)
lim1_Sp = arcpy.GetParameterAsText(3)
lim2_In = arcpy.GetParameterAsText(4)
lim2_Sp = arcpy.GetParameterAsText(5)

cont = 0
# Campos a crear en el shape
nuevosCampos = ["SLK", "DIST", "P_MEDIO", "SLK/MEDIA"]

try:
    #Creacion del objeto para la lectura
    lectura = lecturaGradiente()
    estado = lectura.readPointsShape(PointsDir)
    
    if estado == 0:
        raise Exception
        
    if estado == 1:
        # Nombres de los campos de entrada
        campos = lectura.get_namesFields()
       
        # Puntos ordenados de menor a menor
        orden_X = lectura.get_Point_X()
        arcpy.MessageBox(orden_X)
        orden_Y = lectura.get_Point_Y()
        arcpy.MessageBox(orden_Y)
        orden_Z = lectura.get_Zcoor()

        # Obtencion de las distancias
        Distancia = lectura.get_Dist()
        #Creacion del objeto para calcular el gradiente
        cal = calcularGradiente()
        cal.calcular_SLK(lectura.get_Zcoor(), lectura.get_Dist()) 

        #Obtencion de los datos calculados
        SLK = cal.get_SL_K()
        media = cal.getSL_K_Media()
        medio = cal.getSL_KPuntoMedio()

        # Crea una copia del shape para modificarlo
        arcpy.CopyFeatures_management(PointsDir, SaveDir)

        # Reemplaza los backslashes por slashes
        SaveDirr = SaveDir.replace("\\","/")

        # Agrega los nueevos campos al shape
        for campo in nuevosCampos:
            arcpy.AddField_management(SaveDirr + ".shp", campo, "DOUBLE", "", "", "", "", "NULLABLE")
            
        # Actualizacion del shape
        cursor = arcpy.UpdateCursor(SaveDirr + ".shp") 
        for row in cursor:
            row.setValue(campos[0], orden_X[cont])
            row.setValue(campos[1], orden_Y[cont])
            row.setValue(campos[2], orden_Z[cont])
            row.setValue("SLK", SLK[cont])
            row.setValue("DIST", Distancia[cont])
            row.setValue("P_MEDIO", medio[cont])
            row.setValue("SLK/MEDIA", media[cont])
            cont = cont + 1
            cursor.updateRow(row)   

        #Creacion del objeto para graficar
        grafica = GraficarG()
        grafica.graficarGRF(lectura.get_Zcoor(), lectura.get_Dist(), cal.get_SL_K(), lim1_In, lim1_Sp, lim2_In, lim2_Sp)

except Exception:
    arcpy.AddError("Error con los datos necesarios a procesar")
