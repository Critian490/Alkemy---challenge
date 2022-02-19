                ##### SCRIPT PRINCIPAL - LLAMA A LOS DEMÁS SCRIPS.PY #####

#Importar los otros archivos (scrips.py)
from db.conection import engine_message 
from db.normalization import message_normalization 
from db.table_creation import *
from db.upload_tables_to_db import *

engine_message() #Llamadada el mensaje de conexión con la bd, se encuentra en conection.py
message_normalization() #Llamada al mensaje de normalización, se encuentra en normalization.py
message_table_creation() #Llamada al mensaje de table_creation, se encuentra en table_creation.py

upload_table_1() #Llamada a la funcion que craga la primera tabla, se encuentra en upload_tables_to_db.py
upload_table_2() #Llamada a la funcion que craga la segunda tabla, se encuentra en upload_tables_to_db.py
upload_table_3() #Llamada a la funcion que craga la tercera tabla, se encuentra en upload_tables_to_db.py