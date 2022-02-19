        ##### SCRIPT PARA HACER LA CONEXION CON LA BASE DE DATOS #####

#Importar librería
import logging
from sqlalchemy import create_engine

#Conectar con la base de datos postgreSQL
def engine_message():
    logging.info('Conectando con la base de datos PostgreSQL... \n' + '-'*70)
    # 'postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>'
engine = create_engine('postgresql+psycopg2://postgres:2818@localhost:5432/Alkemy')
