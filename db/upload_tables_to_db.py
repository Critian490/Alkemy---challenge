            ##### SCRIPT PARA SUBIR LAS TABLAS A LA BASE DE DATOS #####

#Importar archivos (scripts.py)
from sqlalchemy import Integer, Text
from db.table_creation import *
from db.conection import engine

table_1() #Tabla #1 creada, se encuentra en table_creation.py
table_2() #Tabla #2 creada, se encuentra en table_creation.py
table_3() #Tabla #3 creada, se encuentra en table_creation.py

#Funcion para subir la primera tabla
def upload_table_1():
    logging.info('Subiendo tabla 1 a PostgreSQL: main_table')
    table_1().to_sql(
        'main_table',
        engine,
        if_exists='replace',
        index=False,
        chunksize=500,
        dtype={
            "Cod_Localidad": Integer,
            "IdProvincia": Integer,
            "IdDepartamento": Integer,
            "Categoría":  Text,
            "Provincia": Text,
            "Localidad": Text,
            "Nombre": Text,
            "Dirección": Text,
            "CP": Text,
            "Teléfono": Text,
            "Mail": Text,
            "Web": Text
            })
    
#Funcion para subir la segunda tabla
def upload_table_2():
    logging.info('Subiendo tabla 2 a PostgreSQL: category_table')
    table_2().to_sql(
        'category_table',
        engine,
        if_exists='replace',
        chunksize=500,
        dtype={
            "Total por categoría": Integer,
            "Fuente": Text,
            "Total por fuente": Integer,
            "Provincia":  Text,
            "Categorías por provincia": Integer,
            })
    
#Funcion para subir la tercera tabla
def upload_table_3():
    logging.info('Subiendo la tabla # 3 a PostgreSQL: cinema_table\n'+'-'*70)
    table_3().to_sql(
        'cinema_table',
        engine,
        if_exists='replace',
        chunksize=500,
        dtype={
            "Provincia": Text,
            "Pantallas": Integer,
            "Butacas": Integer,
            "espacio_INCAA":  Text,
            })