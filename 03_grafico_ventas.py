import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


datos = {
    "Mes": ["Ene", "Feb", "Mar", "Abr", "May"],
    "Ventas_USD": [1500, 2200, 1800, 2900, 3100],
}

df = pd.DataFrame(datos)


plt.figure(figsize=(8, 5))
plt.bar(df["Mes"], df["Ventas_USD"], color="skyblue")
plt.title("Evolución de Ventas Mensuales")
plt.xlabel("Mes")
plt.ylabel("Ventas (USD)")
plt.grid(axis="y", linestyle="--", alpha=0.7)


nombre_grafico = "reporte_ventas.png"
plt.savefig(nombre_grafico)
print(f" Gráfico generado y guardado exitosamente como '{nombre_grafico}'.")