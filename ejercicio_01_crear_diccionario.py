estudiantes = {
    "Ana":    95,
    "Luis":   87,
    "María":  92,
    "Carlos": 78,
    "Sofía":  99,
}
nombre_buscar = "María"
if nombre_buscar in estudiantes:
    print(f"Calificación de {nombre_buscar}: {estudiantes[nombre_buscar]}")
else:
    print(f"{nombre_buscar} no encontrado.")

print("\n--- Lista de estudiantes ---")
for nombre, calificacion in estudiantes.items():
    print(f"  {nombre}: {calificacion}")
