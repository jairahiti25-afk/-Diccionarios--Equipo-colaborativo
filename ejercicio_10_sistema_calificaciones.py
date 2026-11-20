calificaciones = {
    "Ana":     [90, 85, 92, 88],
    "Luis":    [70, 75, 68, 80],
    "María":   [95, 98, 100, 97],
    "Carlos":  [60, 65, 70, 55],
    "Sofía":   [88, 91, 85, 90],
}

def promedio(lista):
    return sum(lista) / len(lista)

def reporte_estudiante(calificaciones, nombre):
    """Busca y muestra el reporte de un estudiante en O(1)."""
    notas = calificaciones.get(nombre)
    if notas is None:
        print(f"  '{nombre}' no encontrado.")
        return
    prom = promedio(notas)
    estado = " Aprobado" if prom >= 70 else " Reprobado"
    print(f"  {nombre}: notas={notas}  |  promedio={prom:.1f}  |  {estado}")

def mejor_estudiante(calificaciones):
    """Encuentra al estudiante con mayor promedio."""
    mejor = max(calificaciones, key=lambda n: promedio(calificaciones[n]))
    return mejor, promedio(calificaciones[mejor])

print("=== Sistema de Calificaciones ===\n")

for nombre in ["María", "Carlos", "Roberto"]:
    reporte_estudiante(calificaciones, nombre)

print("\n--- Reporte General ---")
for nombre in calificaciones:
    reporte_estudiante(calificaciones, nombre)

mejor, prom = mejor_estudiante(calificaciones)
print(f"\n Mejor estudiante: {mejor} con promedio {prom:.1f}")
