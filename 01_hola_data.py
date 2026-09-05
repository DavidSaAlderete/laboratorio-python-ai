import numpy as np
import pandas as pd

datos = {
    "Producto": ["Laptop","Mouse","Teclado","Monitor"],
    "Ventas_USD": [1200,250,450,800],
}

df = pd.DataFrame(datos)

print("---RESUMEN DE VENTAS ---")
print(df)
print(f"\nTotal de ventas: ${df['Ventas_USD'].sum()}")
print(f"Promedio por producto: ${df['Ventas_USD'].mean():.2f}")