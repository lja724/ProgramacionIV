#Importamos la libreria pymongo

from pymongo import MongoClient



cliente= MongoClient("localhost")

#Creamos la base de datos haciendo uso de la libreria antes importada
db= cliente["InventarioMongoDB"]

basedatos = db['InventarioProductos']


# Funciones para la manipulación de la base de datos.

def Insert():
    Answ1 = "Si"
    i= 1
    while Answ1 == "Si":
        Answ1 = input("Quieres agregar un nuevo producto ('Si' o 'No') : ")
        if Answ1== "Si":
            x1 = input("Producto : ")
            x2 = input("Distribuidor : ")
            x3 = int(input("Cantidad : "))
            x4 = float(input("Precio : "))
            basedatos.insert_one(({"id": i ,
                                   'Producto':x1,
                        'Distribuidor':x2,
                        'Cantidad': x3,
                        'Precio': x4}))
            print("Ha agregado el producto", x1, "de forma correcta a su base de datos")
            i+=1
        else:
            Answ1= "No"
  
            
def Delete(x5):
    basedatos.delete_one({'Producto': x5})

def ShowData():
    for datos in basedatos.find({}):
        print(datos)
        
def Search(x6):
    for productos in basedatos.find({'Producto':x6}):
        print (productos)

def Edit():
    AnswEdit = input("Quieres editar una precio ('Si' o 'No') : ")
    if AnswEdit == 'Si':
        x7 = input("Introduzca el producto : ")
        x8 = input("Introduzca el nuevo precio : ")
        basedatos.update_one({'Producto': x7},
                         {"$set": {"Precio":x8}})
    else:
        x7 = input("Introduzca el producto : ")
        x8 = input("Introduzca la nueva cantidad : ")
        basedatos.update_one({'Producto': x7},
                         {"$set": {"Cantidad":x8}})
    

#Programa

while True:
    
    Insert()
    Answ2 = input("Quieres editar un producto ('Si' o 'No') : ")
    if Answ2 == "Si":
        Edit()
                
    Answ3 = input("Quieres buscar un producto ('Si' o 'No') : ")
    if Answ3 == "Si":
        x6= input("Producto : ")
        Search(x6)
        
    Answ4 = input("Quieres eliminar una producto ('Si' o 'No') : ")
    if Answ4 == "Si":
        x5 = input("Producto : ")
        Delete(x5)
    
    AnswData = input("Quieres que se imprima la base de datos ('Si' o 'No') : ")
    if AnswData == "Si":
        ShowData()
            
    AnswF = input("Deseas Salir del programa ('Si' o 'No') : ")
    if AnswF == "Si":
        break