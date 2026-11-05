# ==========================================
# Script de Demo: Análisis Exploratorio + Métricas
# Rama: experimento-analisis
# ==========================================
pip install pandas matplotlib

import csv

def cargar_y_analizar(ruta_csv):
    total_ventas = 0
    conteo = 0
    ventas_por_categoria = {}

    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            monto = float(fila['monto'])
            cat = fila['categoria']
            
            total_ventas += monto
            conteo += 1
            
            ventas_por_categoria[cat] = ventas_por_categoria.get(cat, 0) + monto

    promedio = total_ventas / conteo si conteo > 0 else 0

    print("📊 --- REPORTE DETALLADO DE VENTAS ---")
    print(f"Total registros procesados: {conteo}")
    print(f"Monto total: ${total_ventas:.2f}")
    print(f"Promedio general: ${promedio:.2f}\n")
    
    print("📈 --- VENTAS POR CATEGORÍA ---")
    for cat, total in ventas_por_categoria.items():
        print(f"- {cat}: ${total:.2f}")

if __name__ == "__main__":
    cargar_y_analizar('../data/ventas.csv')
