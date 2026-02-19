import pandas as pd
import os
from datetime import datetime

def main():
    # 1. Cargar datos
    df = pd.read_csv("data/input/ventas_experimento.csv")

    # 2. Calcular métricas del experimento
    resumen = df.groupby("price_variant").agg(
        pasajeros=("passenger_id", "count"),
        conversion_rate=("purchased", "mean"),
        unidades_promedio=("units", "mean"),
        revenue_promedio=("revenue", "mean"),
        revenue_total=("revenue", "sum")
    ).reset_index()

    # 3. Crear carpeta output si no existe
    os.makedirs("output", exist_ok=True)

    # 4. Generar nombre con fecha
    fecha = datetime.today().strftime("%Y-%m-%d")
    output_path = f"output/resumen_experimento_pricing_{fecha}.csv"

    # 5. Guardar resultado
    resumen.to_csv(output_path, index=False)

    print(f"Análisis ejecutado correctamente. Archivo generado: {output_path}")

if __name__ == "__main__":
    main()

