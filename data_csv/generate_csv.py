                    ##### GENERAR LOS ARCHIVOS CSV #####

#Importar librerias
import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s - %(message)s')
current_datetime = datetime.now().strftime("%d-%m-%Y")
current_datetime = str(current_datetime)

#Funcion para generar los csv con los link del documento
def generating():
    logging.info('Generando los CSV...\n' + '-'*70)

    url1 = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv'
    url2 = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
    url3 = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
    museum = requests.get(url1, allow_redirects=True)
    cinema = requests.get(url2, allow_redirects=True)
    library = requests.get(url3, allow_redirects=True)
    open('museos_'+current_datetime+'.csv', 'wb').write(museum.content)
    open('cines_'+current_datetime+'.csv', 'wb').write(cinema.content)
    open('bibliotecas_'+current_datetime+'.csv', 'wb').write(library.content)