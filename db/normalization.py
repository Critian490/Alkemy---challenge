                ##### SCRIPT PARA NORMALIZAR LOS DATOS #####

#Importar librerías
import pandas as pd
import logging
from datetime import datetime

#Importar archivo (script.py)
from data_csv.generate_csv import generating

generating() #Llamado a la funcion que genera los archivos CSV

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s - %(message)s')
current_datetime = datetime.now().strftime("%d-%m-%Y")
current_datetime = str(current_datetime)

#Mensaje de normalización
def message_normalization():
    logging.info('Normalizando los datos...\n'+'-'*70)

#Normalización de los datos
df_museum = pd.read_csv('museos_'+current_datetime+'.csv', sep=',', encoding='UTF-8')
df_museum.rename(columns = {'categoria':'Categoría', 'provincia':'Provincia', 'localidad':'Localidad',
                            'nombre':'Nombre', 'direccion':'Dirección', 'telefono':'Teléfono',
                            'fuente':'Fuente'}, inplace = True)
df_cinema = pd.read_csv('cines_'+current_datetime+'.csv', sep=',', encoding='UTF-8')
df_library = pd.read_csv('bibliotecas_'+current_datetime+'.csv', sep=',', encoding='UTF-8')
df_library.rename(columns = {'Domicilio':'Dirección'}, inplace = True)
