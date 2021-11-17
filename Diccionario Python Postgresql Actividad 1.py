# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:43:19 2021

"""

#Importamos la libreria sqlite3
import sqlite3

#Creamos la base de datos haciendo uso de la libreria antes importada

ConexionBD = sqlite3.connect('DiccionarioPostgreSQL.db')


cursorBD = ConexionBD.cursor()

#Creamos la tabla que contiene las palabras del diccionario
cursorBD.execute("""CREATE TABLE if not exists Diccionario (
            Palabra_id integer primary key autoincrement,
            Palabra_E VARCHAR (255) NOT NULL ,
            Palabra_S VARCHAR (255) NOT NULL
            )""")

ConexionBD.commit()


# Funciones para la manipulación de la base de datos.

def Insert():
    Answ1 = "Si"
    while Answ1 == "Si":
        Answ1 = input("Quieres agregar una nueva palabra ('Si' o 'No') : ")
        if Answ1== "Si":
            x1 = input("Palabra en Español : ")
            x2 = input("Significado : ")
            Palabras = (x1,x2)
            cursorBD.execute("insert into Diccionario(Palabra_E,Palabra_S) VALUES (?,?)", (Palabras))
            ConexionBD.commit()
            print("Ha agregado la palabra", x1, "de forma correcta a su diccionario")
        else:
            Answ1= "No"
    
def Delete(x3):
    cursorBD.execute("delete from Diccionario WHERE Palabra_E= '%s'" % x3)
    ConexionBD.commit()
    print("Se borro la palabra", x3, "de forma correcta de su diccionario")

def ShowData():
    cursorBD.execute("SELECT Palabra_id,Palabra_E,Palabra_S from Diccionario")
    Datos_Filas = cursorBD.fetchall()
    for Dato in Datos_Filas:
        print("Id_Palabra= ", Dato[0], "Palabra_Español = ", Dato[1], "Palabra_Slang", Dato[2])

def Mean(x4):     
    cursorBD.execute("select Palabra_E, Palabra_S from Diccionario WHERE Palabra_E = '%s'" % x4 )
    Datos = cursorBD.fetchall()
    print("La palabra", Datos[0][0],"Significa : ",Datos[0][1])


def Edit(x5,x6):
    SQLcode = "UPDATE Diccionario SET Palabra_S =" +"'" + x6 + "'" "WHERE Palabra_E =" + "'" + x5 + "'"
    cursorBD.execute(SQLcode)
    ConexionBD.commit()


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

ConexionBD.close()
