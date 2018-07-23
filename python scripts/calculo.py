# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 04:41:25 2018

@author: alexa
"""
from pruebalectura import modelo

class calcular():
    
    def __init__(self):
        obj = modelo()
        global num_conver_A
        global num_conver_B
        num_conver_A = obj.obtener_zcoor()
        num_conver_B = obj.obtener_dist()
        e = []
        d = []
        resultado = []
        contador = len(num_conver_B)
        mins = 0
        for i in num_conver_A:  
            print(len(d))
            print (len(e))   
            
            for j in num_conver_B(range(mins, mins+1)):
                
                print(len(num_conver_B) - contador + 1)
                print("xxxxxx")
                print(mins)
                print(i)
                print(j)
                print("-----")
                d.append(i)
                e.append(j)
               
                if(len(e) == 2):
                    print("pasa por aqui")
                    result = ((d[0]-d[1])/(e[1]-e[0]))*(e[0]+((e[1]-e[0])/2))*-1
                    resultado.append(result)
            mins = mins + 1
            #print(resultado)
            
        
obj = calcular()