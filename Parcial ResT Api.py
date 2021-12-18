
## Importamos las librerias que utilizaremos en el proyecto
from flask import Flask,jsonify
import pandas as pd

app = Flask(__name__)

#Importamos los datos
df=pd.read_csv('Datos_Vacunas.csv')


#Diseño de Api Rest (Solo lectura metodo GET por defecto)
# La api muestra todos los datos almacenados, puede ademas ver la información por cada pais y por cada año.

@app.route('/Alldata')
def MostrarDatos():
    #Eliminamos los datos que no posean valor registrado
    All_Data = df.dropna(1)
    #Convertimos el dataframe en un archivo json para ser mostrado cuando se realice una consulta
    All_Data = All_Data.to_json()
    return jsonify(All_Data)

#Creamos una ruta para filtrar los datos por fecha
@app.route('/Datos/<string:Fechas>')
def Datos_Fechas(Fechas):
    ListaFechas= Fechas.split(',')
    Datos_por_Fechas = df[ListaFechas]
    Datos_por_Fechas = Datos_por_Fechas.to_json(orient='index')
    return jsonify(Datos_por_Fechas)

@app.route('/Datos/<string:Pais>/<string:Fechas>')
def FiltroYear(Pais,Fechas):
    try:
        Datos_Pais = df[df['Country Name']==Pais]
        Datos_Pais  = Datos_Pais.dropna(1)
        ListaFechas = Fechas.split(',')
        Datos_Pais_Fecha  = Datos_Pais[ListaFechas]
        Datos_Pais_Fecha = Datos_Pais_Fecha.to_json(orient='index')
        if Datos_Pais_Fecha == "{}":
            return jsonify({'message':'Pais o fecha no encontrada'})
        else:
            return jsonify(Datos_Pais_Fecha)
        
    except:
        return jsonify({'message':'Pais o fecha no encontrada'})

if __name__ == '__main__':
    app.run(debug=True,port=5000)