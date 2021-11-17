
#Importamos la librería sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import sessionmaker

#Creamos la base de datos haciendo uso de la libreria antes importada


engine = create_engine("mariadb+mariadbconnector://root:1234@127.0.0.1:3307/diccionario")
Base=declarative_base()
#Creamos la tabla que contiene las palabras del diccionario
class Diccionarios(Base):

    __tablename__ = 'Diccionario'
    Palabra_E = Column(String(100),primary_key=True)
    Palabra_S = Column(String(100))


Session = sessionmaker(engine)
session= Session()
Base.metadata.create_all(engine)

# Funciones para la manipulación de la base de datos.

def Insert():
    Answ1 = "Si"
    while Answ1 == "Si":
        Answ1 = input("Quieres agregar una nueva palabra ('Si' o 'No') : ")
        if Answ1== "Si":
            x1 = input("Palabra en Español : ")
            x2 = input("Significado : ")
            Palabras = (x1,x2)
            Insertar = Diccionarios(Palabra_E=x1,Palabra_S=x2)
            session.add(Insertar)
            session.commit()
            print("Ha agregado la palabra", x1, "de forma correcta a su diccionario")
        else:
            Answ1= "No"


def Delete(x3):
    session.query(Diccionarios).filter(Diccionarios.Palabra_E == x3).delete()
    session.commit()
    print("Se borro la palabra", x3, "de forma correcta de su diccionario")


def ShowData():
    Datos_Filas = session.query(Diccionarios).all()
    for Dato in Datos_Filas:
        print("Palabra_Español = ", Dato.Palabra_E, "Palabra_Slang = ", Dato.Palabra_S)



def Mean(x4):     
    Datos = session.query(Diccionarios).filter_by(Palabra_E = x4)
    for Dato in Datos:
        print("La palabra", Dato.Palabra_E,"Significa : ",Dato.Palabra_S)



def Edit(x5,x6):
    Edits = session.query(Diccionarios).get(x5)
    Edits.Palabra_S= x6
    session.commit()



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
