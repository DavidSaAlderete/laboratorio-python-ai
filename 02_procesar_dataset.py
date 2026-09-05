import os
import pandas as pd

# 1. Crear un archivo CSV simulado con datos "sucios"
datos_brutos = {
    "Cliente_ID": [101, 102, 103, 104, 105, 106],
    "Nombre": ["Ana", "Carlos", "Beatriz", "David", "Elena", "Fernando"],
    "Categoria": ["Tech", "Hogar", "Tech", None, "Hogar", "Tech"],
    "Gasto_USD": [350.5, 120.0, None, 450.0, 95.0, 600.0],
}

df_original = pd.DataFrame(datos_brutos)
archivo_csv = "clientes_temp.csv"
df_original.to_csv(archivo_csv, index=False)

print("--- DATASET ORIGINAL (con valores nulos) ---")
print(df_original)

# 2. Cargar y Limpiar los datos usando Pandas
df = pd.read_csv(archivo_csv)

# Eliminar filas con valores nulos (NaN)
df_limpio = df.dropna()

print("\n--- DATASET LIMPIO ---")
print(df_limpio)

# 3. Agrupación y Métricas por Categoría
resumen = df_limpio.groupby("Categoria")["Gasto_USD"].agg(["count", "mean", "sum"])
resumen.columns = ["Total_Clientes", "Promedio_USD", "Suma_Total_USD"]

print("\n--- RESUMEN POR CATEGORÍA ---")
print(resumen.round(2))

# 4. Limpieza del archivo temporal generado (opcional)
if os.path.exists(archivo_csv):
    os.remove(archivo_csv)