import os
from dotenv import load_dotenv
import requests
import pandas as pd

# Carga las variables de entorno desde .env
load_dotenv()

def descargar_imagen(url, folder_name, file_name, base_folder):
    token = os.getenv('TOKEN_KOBO')
    if token is None:
        print("Token no encontrado. Asegúrate de que el archivo .env esté configurado correctamente.")
        return
    
    headers = {'Authorization': 'Token ' + token}
    full_folder_path = os.path.join(base_folder, folder_name)
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        os.makedirs(full_folder_path, exist_ok=True)
        file_path = os.path.join(full_folder_path, file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"No se pudo descargar la imagen {file_name}: Estado {response.status_code}")

file_path = 'archivos_descargar.csv'  # Ruta del archivo CSV
data = pd.read_csv(file_path)
columnas_relevantes = data[['Tipo_Insecto', 'Tipo insecto detalle', 'Url foto']]

base_folder = 'descargas'  # Carpeta base para todas las descargas

print("Directorio actual:", os.getcwd())

for index, row in columnas_relevantes.iterrows():
    tipo_insecto_detalle = row['Tipo insecto detalle']
    url_foto = row['Url foto']
    file_name = url_foto.split('/')[-1]
    try:
        descargar_imagen(url_foto, tipo_insecto_detalle, file_name, base_folder)
    except Exception as e:
        print(f"Error al descargar la imagen {file_name}: {e}")

print("Descarga completada.")
