import pandas as pd

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

    # 3. Guardar resultado para Power BI
    resumen.to_csv("output/resumen_experimento_pricing.csv", index=False)

    print("Análisis ejecutado correctamente. Archivo generado.")

if __name__ == "__main__":
    main()

