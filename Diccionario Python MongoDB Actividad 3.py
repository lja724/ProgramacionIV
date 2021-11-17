# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:51:18 2021

"""

#Importamos la libreria pymongo

from pymongo import MongoClient



cliente= MongoClient("localhost")

#Creamos la base de datos haciendo uso de la libreria antes importada
db= cliente["DiccionarioMongoDB"]

basedatos = db['Diccionario']


# Funciones para la manipulación de la base de datos.

def Insert():
    Answ1 = "Si"
    i= 1
    while Answ1 == "Si":
        Answ1 = input("Quieres agregar una nueva palabra ('Si' o 'No') : ")
        if Answ1== "Si":
            x1 = input("Palabra en Español : ")
            x2 = input("Significado : ")
            basedatos.insert_one(({"id": i ,
                                   'Palabra_E':x1,
                        'Palabra_S':x2}))
            print("Ha agregado la palabra", x1, "de forma correcta a su diccionario")
            i+=1
        else:
            Answ1= "No"
  
            
def Delete(x3):
    basedatos.delete_one({'Palabra_E': x3})

def ShowData():
    for datos in basedatos.find({}):
        print(datos)
        
def Mean(x4):
    for palabras in basedatos.find({'Palabra_E':x4}):
        print (palabras)

def Edit(x5,x6):
    basedatos.update_one({'Palabra_E': x5},
                         {"$set": {"Palabra_S":x6}})


#Programa

while True:
    
    Insert()
    Answ2 = input("Quieres editar una palabra ('Si' o 'No') : ")
    if Answ2 == "Si":
        x5 = input("Palabra Español: ")
        x6 = input("Significado : ")
        Edit(x5,x6)
                
    Answ3 = input("Quieres ver el significado de una palabra ('Si' o 'No') : ")
    if Answ3 == "Si":
        x4= input("Palabra Español : ")
        Mean(x4)
        
    Answ4 = input("Quieres eliminar una palabra ('Si' o 'No') : ")
    if Answ4 == "Si":
        x3 = input("Palabra : ")
        Delete(x3)
    
    AnswData = input("Quieres que se imprima la base de datos ('Si' o 'No') : ")
    if AnswData == "Si":
        ShowData()
            
    AnswF = input("Deseas Salir del programa ('Si' o 'No') : ")
    if AnswF == "Si":
        break
