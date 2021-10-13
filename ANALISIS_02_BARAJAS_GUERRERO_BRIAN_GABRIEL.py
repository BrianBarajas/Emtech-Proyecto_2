# -*- coding: utf-8 -*-
"""
Codigo para el analisis de datos del caso práctico 2

@author: Brian gabriel Barajas Guerrero
"""

import csv

"Ordenando los datos en diccionarios que agregamos a una lista"
lista_d = []
with open("synergy_logistics_database.csv", "r") as archivo:
    
    lector = csv.DictReader(archivo)
    
    for registro in lector:
        lista_d.append(registro)
        

#print(lista_d[0])

"Definimos una función que nos dé una lista con las las rutas y el numero de operaciones de importaciones o exportaciones de algun año segun elijamos"
def rutas_exp_imp (direccion, año):
    contador = 0
    rutas_contadas = []
    rutas_conteo = []
    for ruta in lista_d:
        if ruta["direction"] == direccion and año == ruta["year"]:
            ruta_actual = [ruta["origin"], ruta["destination"]]
            
            if ruta_actual not in rutas_contadas:
                for ruta_bd in lista_d:
                    if ruta_actual == [ruta_bd["origin"], ruta_bd["destination"]] and año == ruta_bd["year"]:
                        contador += 1
                
                #print(rutas_contadas)
                #print(ruta_actual)
                rutas_contadas.append(ruta_actual)
                
                
                rutas_conteo.append([ruta_actual, contador])
                #print(ruta_actual)
                #rutas_conteo.append([ruta_bd["origin"], ruta_bd["destination"], contador])
                contador = 0
                
            #print(rutas_conteo)
    rutas_conteo.sort(reverse = True, key = lambda x:x[1])
    
    tamaño_lista = 10
    while len(rutas_conteo) > tamaño_lista:
        rutas_conteo.pop(-1)
    
    return rutas_conteo 

"guardamos las listas de cada año en variables llamando a la funcion"

conteo_exportaciones_2015 = rutas_exp_imp("Exports", "2015")
conteo_exportaciones_2016 = rutas_exp_imp("Exports", "2016")
conteo_exportaciones_2017 = rutas_exp_imp("Exports", "2017")
conteo_exportaciones_2018 = rutas_exp_imp("Exports", "2018")
conteo_exportaciones_2019 = rutas_exp_imp("Exports", "2019")
conteo_exportaciones_2020 = rutas_exp_imp("Exports", "2020")

conteo_importaciones_2015 = rutas_exp_imp("Imports", "2015")
conteo_importaciones_2016 = rutas_exp_imp("Imports","2016")
conteo_importaciones_2017 = rutas_exp_imp("Imports","2017")
conteo_importaciones_2018 = rutas_exp_imp("Imports","2018")
conteo_importaciones_2019 = rutas_exp_imp("Imports","2019")
conteo_importaciones_2020 = rutas_exp_imp("Imports","2020")


"Definimos otra funcion para que esta vez nos dé las rutas y el numero de operaciones de forma global a lo largo de todos los años registrados"
def rutas_exp_imp_global (direccion):
    contador = 0
    rutas_contadas = []
    rutas_conteo = []
    for ruta in lista_d:
        if ruta["direction"] == direccion:
            ruta_actual = [ruta["origin"], ruta["destination"]]
            
            if ruta_actual not in rutas_contadas:
                for ruta_bd in lista_d:
                    if ruta_actual == [ruta_bd["origin"], ruta_bd["destination"]]:
                        contador += 1
                
                #print(rutas_contadas)
                #print(ruta_actual)
                rutas_contadas.append(ruta_actual)
                
                
                rutas_conteo.append([ruta_actual, contador])
                #print(ruta_actual)
                #rutas_conteo.append([ruta_bd["origin"], ruta_bd["destination"], contador])
                contador = 0
                
            #print(rutas_conteo)
    rutas_conteo.sort(reverse = True, key = lambda x:x[1])
    
    tamaño_lista = 10
    while len(rutas_conteo) > tamaño_lista:
        rutas_conteo.pop(-1)
    
    return rutas_conteo 

"Guardamos las listas llamando a la funcion"
conteo_exportaciones_global = rutas_exp_imp_global("Exports")
conteo_importaciones_global = rutas_exp_imp_global("Imports")


"Creamos un archivo csv para guardar y mostrar ahi los datos recabados sobre las rutas de exportaciones"

with open("exportaciones_por_año.csv", "w") as archivo: 
    escritor = csv.writer(archivo)
    
    año = ["Top 10 de rutas de exportaciones", "Global"]
    escritor.writerow(año)
    escritor.writerows(conteo_exportaciones_global)
    
    año = ["Top 10 de rutas de exportaciones", 2015]
    escritor.writerow(año)
    escritor.writerows(conteo_exportaciones_2015)
    año = ["Top 10 de rutas de exportaciones", 2016]
    escritor.writerow(año)
    escritor.writerows(conteo_exportaciones_2016)
    año = ["Top 10 de rutas de exportaciones", 2017]
    escritor.writerow(año)
    escritor.writerows(conteo_exportaciones_2017)
    año = ["Top 10 de rutas de exportaciones", 2018]
    escritor.writerow(año)
    escritor.writerows(conteo_exportaciones_2018)
    año = ["Top 10 de rutas de exportaciones", 2019]
    escritor.writerow(año)
    escritor.writerows(conteo_exportaciones_2019)
    año = ["Top 10 de rutas de exportaciones", 2020]
    escritor.writerow(año)
    escritor.writerows(conteo_exportaciones_2020)
    
"Creamos un archivo csv para guardar y mostrar ahi los datos recabados sobre las rutas de importaciones"
    
with open("importaciones_por_año.csv", "w") as archivo:
    escritor = csv.writer(archivo)
    
    año = ["Top 10 de rutas de importaciones", "Global"]
    escritor.writerow(año)
    escritor.writerows(conteo_importaciones_global)
    
    año = ["Top 10 de rutas de importaciones", 2015]
    escritor.writerow(año)
    escritor.writerows(conteo_importaciones_2015)
    año = ["Top 10 de rutas de importaciones", 2016]
    escritor.writerow(año)
    escritor.writerows(conteo_importaciones_2016)
    año = ["Top 10 de rutas de importaciones", 2017]
    escritor.writerow(año)
    escritor.writerows(conteo_importaciones_2017)
    año = ["Top 10 de rutas de importaciones", 2018]
    escritor.writerow(año)
    escritor.writerows(conteo_importaciones_2018)
    año = ["Top 10 de rutas de importaciones", 2019]
    escritor.writerow(año)
    escritor.writerows(conteo_importaciones_2019)
    año = ["Top 10 de rutas de importaciones", 2020]
    escritor.writerow(año)
    escritor.writerows(conteo_importaciones_2020)


"Definimos una funcion rapida que calcule el porcentaje"
def calculo_porcentaje(total, individual):
    porcentaje = (individual / total) * 100
    return porcentaje
    

"Definimos una funcion que nos muestre una lista con el porcentaje en el valor total de las operaciones con el que tuvo que ver cada pais y nos regrese los paises que representaron el 80%"
def valor_exp_imp_global(direccion):
    contador = 0
    rutas_contadas = []
    rutas_conteo = []
    for ruta in lista_d:        
        if ruta["direction"] == direccion:
            ruta_actual = [ruta["origin"], ruta["destination"]]   
            if ruta_actual not in rutas_contadas:
                for ruta_bd in lista_d:
                    if ruta_actual == [ruta_bd["origin"], ruta_bd["destination"]]:
                        contador += int(ruta_bd["total_value"])
                
                rutas_contadas.append(ruta_actual)                           
                rutas_conteo.append([ruta_actual, contador])
                contador = 0               
            #print(rutas_conteo)
    rutas_conteo.sort(reverse = True, key = lambda x:x[1])
     
    valor_pais = []
    paises = []
    suma_pais = 0
    for pais in rutas_conteo:
        if pais[0][0] not in paises:
            for pais1 in rutas_conteo:
                if pais[0][0] == pais1[0][0] or pais[0][0] == pais1[0][1]:
                    suma_pais += int(pais1[1])
            paises.append(pais[0][0])
            valor_pais.append([pais[0][0], suma_pais])
            suma_pais = 0
            
        elif pais[0][1] not in paises:
            for pais1 in rutas_conteo:
                if pais[0][1] == pais1[0][0] or pais[0][1] == pais1[0][1]:
                    suma_pais += int(pais1[1])
            paises.append(pais[0][1])
            valor_pais.append([pais[0][1], suma_pais])
            suma_pais = 0
    #print(valor_pais)
    valor_pais.sort(reverse = True, key = lambda x:x[1])
    
    suma_valor = 0
    for valor in valor_pais: 
        suma_valor += valor[1]
        
    porcentaje_actual = 0
    porcentajes = []
    for valor_ind in valor_pais:
        porcentaje = calculo_porcentaje(suma_valor, valor_ind[1])
        porcentajes.append([valor_ind[0], porcentaje])
        porcentaje_actual += porcentaje
        if porcentaje_actual > 80:
            porcentajes.pop(-1)
            porcentaje_actual -= porcentaje
            
    #print(porcentajes)
    #print(porcentaje_actual)    
    return porcentajes, porcentaje_actual 


"Definimos una funcion que nos muestre por cada año una lista con el porcentaje en el valor total de las operaciones con el que tuvo que ver cada pais y nos regrese los paises que representaron el 80%"
def valor_exp_imp_anual(direccion, año):
    contador = 0
    rutas_contadas = []
    rutas_conteo = []
    for ruta in lista_d:        
        if ruta["direction"] == direccion and ruta["year"] == año:
            ruta_actual = [ruta["origin"], ruta["destination"]]   
            if ruta_actual not in rutas_contadas:
                for ruta_bd in lista_d:
                    if ruta_actual == [ruta_bd["origin"], ruta_bd["destination"]]:
                        contador += int(ruta_bd["total_value"])
                
                rutas_contadas.append(ruta_actual)                           
                rutas_conteo.append([ruta_actual, contador])
                contador = 0               
            #print(rutas_conteo)
    rutas_conteo.sort(reverse = True, key = lambda x:x[1])
     
    valor_pais = []
    paises = []
    suma_pais = 0
    for pais in rutas_conteo:
        if pais[0][0] not in paises:
            for pais1 in rutas_conteo:
                if pais[0][0] == pais1[0][0] or pais[0][0] == pais1[0][1]:
                    suma_pais += int(pais1[1])
            paises.append(pais[0][0])
            valor_pais.append([pais[0][0], suma_pais])
            suma_pais = 0
            
        elif pais[0][1] not in paises:
            for pais1 in rutas_conteo:
                if pais[0][1] == pais1[0][0] or pais[0][1] == pais1[0][1]:
                    suma_pais += int(pais1[1])
            paises.append(pais[0][1])
            valor_pais.append([pais[0][1], suma_pais])
            suma_pais = 0
    #print(valor_pais)
    valor_pais.sort(reverse = True, key = lambda x:x[1])
    
    suma_valor = 0
    for valor in valor_pais: 
        suma_valor += valor[1]
        
    porcentaje_actual = 0
    porcentajes = []
    for valor_ind in valor_pais:
        porcentaje = calculo_porcentaje(suma_valor, valor_ind[1])
        porcentajes.append([valor_ind[0], porcentaje])
        porcentaje_actual += porcentaje
        if porcentaje_actual > 80:
            porcentajes.pop(-1)
            porcentaje_actual -= porcentaje
        elif porcentaje < 0.001:
            porcentajes.pop(-1)
            porcentaje_actual -= porcentaje
            
    #print(porcentajes)
    #print(porcentaje_actual)    
    return porcentajes, porcentaje_actual 

"Definimos una funcion que nos cree un archivo CSV con los porcentajes de cada pais"
def archivo_de_porcentajes (nombre, direccion):
    
    lista_global, porcentaje_global = valor_exp_imp_global(direccion)
    lista_2015, porcentaje_15 = valor_exp_imp_anual(direccion, "2015")
    lista_2016, porcentaje_16 = valor_exp_imp_anual(direccion, "2016")
    lista_2017, porcentaje_17 = valor_exp_imp_anual(direccion, "2017")
    lista_2018, porcentaje_18 = valor_exp_imp_anual(direccion, "2018")
    lista_2019, porcentaje_19 = valor_exp_imp_anual(direccion, "2019")
    lista_2020, porcentaje_20 = valor_exp_imp_anual(direccion, "2020")  
    
    with open(nombre, "w") as archivo:
        
        escritor = csv.writer(archivo)
        
        año = ["Lista de paises que generan el " + str(porcentaje_15) + " porciento del valor de " + direccion + "(aparecen ya sea en origen o en destino de la operación)", "Global" ]
        escritor.writerow(año)
        escritor.writerows(lista_global)
        
        año = ["Lista de paises que generan el " + str(porcentaje_15) + " porciento del valor de las " + direccion , 2015]
        escritor.writerow(año)
        escritor.writerows(lista_2015)
        año = ["Lista de paises que generan el " + str(porcentaje_16) + " porciento del valor de las " + direccion , 2016]
        escritor.writerow(año)
        escritor.writerows(lista_2016)
        año = ["Lista de paises que generan el " + str(porcentaje_17 )+ " porciento del valor de las " + direccion , 2017]
        escritor.writerow(año)
        escritor.writerows(lista_2017)
        año = ["Lista de paises que generan el " + str(porcentaje_18) + " porciento del valor de las " + direccion , 2018]
        escritor.writerow(año)
        escritor.writerows(lista_2018)
        año = ["Lista de paises que generan el " + str(porcentaje_19) + " porciento del valor de las " + direccion , 2019]
        escritor.writerow(año)
        escritor.writerows(lista_2019)
        año = ["Lista de paises que generan el " + str(porcentaje_20) + " porciento del valor de las " + direccion , 2020]
        escritor.writerow(año)
        escritor.writerows(lista_2020)
        

"Llamamos la funcion 2 veces para crear dos documentos"
archivo_de_porcentajes("80%_de_las_exportaciones.csv","Exports")
archivo_de_porcentajes("80%_de_las_importaciones.csv","Imports")
