import os
import pandas as pd
import requests
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()
api_url = os.getenv("API_URL")

# Consultar la API
print(f" Conectando a la API: {api_url}")
respuesta = requests.get(api_url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    
    # Convertir la respuesta JSON a un DataFrame de Pandas
    df = pd.DataFrame(datos)
    
    print("\n=== PRIMEROS 5 REGISTROS DE LA API ===")
    print(df[["id", "title"]].head())
    
    print(f"\nTotal de publicaciones obtenidas: {len(df)}")
else:
    print(f"Error al consultar la API. Código de estado: {respuesta.status_code}")