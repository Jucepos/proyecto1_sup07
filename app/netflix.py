#Importamos librerias para limpieza

from fastapi import FastAPI

app = FastAPI()

import numpy as np
import pandas as pd

#Leemos el archivo con pandas

df_netflix = pd.read_csv('netflix.csv')

#Cambiamos el tipo de dato de la columna date_added

from datetime import datetime
df_netflix['date_added'] = pd.to_datetime(df_netflix['date_added'])

#Ordenamos los campos en forma ascendente por fecha (del mas viejo al mas nuevo) 

df_netflix.sort_values(by=['date_added'], inplace= True)

#Reemplazamos los campos que tengan 'Not Given' en la columna director

df_netflix.loc[df_netflix['director'].str.contains('Not Given', case = False), 'director'] = 'None'

#Creamos los dataframes con las mascaras solo de los años que queremos 

netf_2019 = df_netflix[df_netflix["release_year"] == 2019]
netf_2020 = df_netflix[df_netflix["release_year"] == 2020]
netf_2021 = df_netflix[df_netflix["release_year"] == 2021]

#Transformamos en diccionario los dataframes

net_2019= netf_2019.reset_index().to_dict(orient="index")
net_2020= netf_2020.reset_index().to_dict(orient="index")
net_2021= netf_2021.reset_index().to_dict(orient="index")


#Creamos la Api

@app.get("/")
async def index():
    return {"Elegi el catalogo que quieras ver /2019 /2020 /2021"}

@app.get("/2019")
async def index():
    return net_2019

@app.get("/2020")
async def index():
    return net_2020

@app.get("/2021")
async def index():
    return net_2021