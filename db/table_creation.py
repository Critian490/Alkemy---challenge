            ##### SCRIPT PARA CREAR LAS TABLAS PARA LA BASE DE DATOS#####

#Importar librerias
import logging
import pandas as pd
from datetime import datetime
#Importar archivo (script.py)
from db.normalization import df_cinema, df_museum, df_library

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s - %(message)s')
current_datetime = datetime.now().strftime("%d-%m-%Y")
current_datetime = str(current_datetime)

# dataframe principal
master_df = df_museum.append(df_cinema)
master_df = master_df.append(df_library)

def message_table_creation():
    logging.info('Creando las tablas...\n'+'-'*70)
    
# tabla 1
def table_1():
    table1 = master_df.loc[:,['Cod_Loc','IdProvincia','IdDepartamento','Categoría','Provincia','Localidad',
                       'Nombre','Dirección','CP','Teléfono','Mail','Web']]
    table1['Fecha de carga'] = pd.to_datetime('today').strftime("%d-%m-%Y")
    return table1

# tabla 2
def table_2():
    table2_1 = master_df.groupby(['Categoría']).size().to_frame(name = 'Total por categoría')
    table2_2 = master_df.groupby(['Categoría','Fuente']).size().to_frame(name = 'Total por fuente')
    table2_3 = master_df.groupby(['Categoría','Provincia']).size().to_frame(name = 'Categorías por provincia')
    table2 = table2_1.merge(table2_2, how='outer', left_index=True, right_index=True)
    table2 = table2.merge(table2_3, how='outer', left_index=True, right_index=True)
    table2.reset_index(inplace=True)
    table2.set_index('Categoría', inplace=True)
    table2 = table2[['Total por categoría','Fuente','Total por fuente','Provincia','Categorías por provincia']]
    table2['Fecha de carga'] = pd.to_datetime('today').strftime("%d-%m-%Y")
    return table2

# tabla 3
def table_3():
    table3 = df_cinema.loc[:,['Provincia','Pantallas','Butacas','espacio_INCAA']]
    aggregation_functions = {'Pantallas': 'sum', 'Butacas': 'sum','espacio_INCAA':'count'}
    table3 = table3.groupby(table3['Provincia']).aggregate(aggregation_functions)
    table3['Fecha de carga'] = pd.to_datetime('today').strftime("%d-%m-%Y")
    return table3