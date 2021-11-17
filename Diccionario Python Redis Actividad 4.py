import redis
r= redis.Redis()

#Borramos todos los elementos que contegan la base de datos antes de iniciar el programa:
r.flushall()
#Creamos las funciones que manipularan las bases de datos
def Insert():
    Answ1 = "Si"
    while Answ1 == "Si":
        Answ1 = input("Quieres agregar una nueva palabra ('Si' o 'No') : ")
        if Answ1== "Si":
            x1 = input("Palabra en Español : ")
            x2 = input("Significado : ")
            r.set(x1,x2)
            print("Ha agregado la palabra", x1, "de forma correcta a su diccionario")
        else:
            Answ1= "No"

def Delete(x3):
    r.delete(x3)
    print("Se borro la palabra", x3, "de forma correcta de su diccionario")

def ShowData():
    Datos_Filas = r.keys()
    for Datos in Datos_Filas:
        Resultados = r.get(Datos)
        print("Palabra Español : ",Datos, "Palabra Slang : ", Resultados)

def Mean(x4): 
    print("La palabra", x4, " Significa : ", r.get(x4))

def Edit(x5,x6):
    r.set(x5,x6)


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