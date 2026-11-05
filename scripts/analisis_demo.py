# ==========================================
# Script de Demo: Análisis Exploratorio de Datos
# Autor: Edgar Bume
# ==========================================

import math

# Datos simulados: Ventas diarias
ventas = [150, 200, 250, 180, 300, 400, 350]

# Cálculo de estadísticas básicas
total_ventas = sum(ventas)
promedio_ventas = total_ventas / len(ventas)
max_venta = max(ventas)
min_venta = min(ventas)

print("--- REPORTE DE VENTAS ---")
print(f"Total vendido: ${total_ventas}")
print(f"Promedio diario: ${promedio_ventas:.2f}")
print(f"Venta máxima: ${max_venta}")
print(f"Venta mínima: ${min_venta}")
