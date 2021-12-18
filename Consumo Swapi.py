# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:37:31 2021

@author: Abraham
"""

import requests

## Primera Pregunta

Root = "https://www.swapi.tech/api/films/"

Peliculas_Planetas_Aridos = []
pelicula= 1
while pelicula < 6:
    Url_request =Root+ str(pelicula)
    response = requests.get(Url_request)
    response = response.json()
    Lista_Planetas = (response['result']['properties']['planets'])
    for element in Lista_Planetas:
        response_Planetas = requests.get(element)
        response_Planetas  = response_Planetas.json()
        if ('arid' in response_Planetas['result']['properties']['climate']) == True and (response['result']['properties']['title'] not in Peliculas_Planetas_Aridos) == True :
            Peliculas_Planetas_Aridos.append(response['result']['properties']['title'])
    pelicula+=1
print('Peliculas Planetas con clima áridos: ',Peliculas_Planetas_Aridos)


## Segunda Pregunta

Root = "https://www.swapi.tech/api/films/"
pelicula = 1
id_peliculas = 1
Wookies = 0
while id_peliculas != 6:
    Url_request =Root+ str(pelicula)
    response = requests.get(Url_request)
    response = response.json()
    id_peliculas = response['result']['properties']['episode_id']
    pelicula+=1

Especies = response['result']['properties']['species']
for element in Especies:
    response_Especies = requests.get(element)
    response_Especies  = response_Especies.json()
    if response_Especies['result']['properties']['name'] == 'Wookie':
        Personajes= response_Especies['result']['properties']['people']
        for Personaje in Personajes:
            if (Personaje in (response['result']['properties']['characters'])) == True:
                Wookies+=1

print('Los wookies que aparecen en la pelicula 6 son : ',Wookies)


## Tercera Pregunta

Root = "https://www.swapi.tech/api/starships/"
Numero_Peliculas = 0
Longitud = 0
for i in range(1,36):
    try:
        URL_BASE =Root + str(i)
        response = requests.get(URL_BASE)
        response = response.json()
        Starships = (response['result']['properties']['length'])
        if Longitud<float(Starships) : 
            Longitud = float(Starships)
            Nombre = response['result']['properties']['name']
    except:
        continue

print('La Aeronave Mas grande de la saga es  : ',Nombre)







