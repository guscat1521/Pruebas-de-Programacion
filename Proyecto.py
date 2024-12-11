import pandas as pd
import numpy as np
import matplotlib.pyplot as pltt
import seaborn as sns

#Ventas simuladas 
data = {
    "fecha": pd.date_range(start="2023-01-01", periods=100, freq="D"),
    "categoria": np.random.choice(["Electronica", "Ropa", "Alimentos", "Hogar"],100),
    "ventas": np.random.randint(100, 5000, 100),
    "region": np.random.choice(["Norte", "Sur", "Este", "Oeste"], 100)
}
df = pd.DataFrame(data)

#Mostramos las primeras filas del DataFrame
print("Datsos iniciales")
print(df.head())

#Verificamos valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Análisis de ventas por categoría de producto
pltt.figure(figsize= (10,6))
sns.barplot(x="categoria", y="ventas", data=df, estimator=sum)
pltt.title("Ventas Totales por categoria")
pltt.show()

#Analsis de venta por region
df["mes"] = df["fecha"].dt.month
ventas_mensuales = df.groupby("mes")["ventas"].sum()
pltt.title("ventas Mensuales")
pltt.xlabel("Mes")
pltt.ylabel("ventas Toltales")
pltt.show()

#Promedio de ventas mensuales
primedio_ventas_mensuales = ventas_mensuales.mean()
print(f"\nPromedio de ventas mensuales: {primedio_ventas_mensuales:.2f}")

#Ticket promedio (ventas por transaccion)
ticket_promedio = df["ventas"].mean()
print(f"Ticket promedio: {ticket_promedio}")

#Ventas totales
ventas_totales = df["ventas"].sum()
print(f"venatstotales en el periodo: {ventas_totales}")