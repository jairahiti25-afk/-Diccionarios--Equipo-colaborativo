texto = "el gato come y el perro come y el gato duerme"

frecuencia = {}
for palabra in texto.split():
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Frecuencia de cada palabra:")
for palabra, conteo in sorted(frecuencia.items()):
    print(f"  '{palabra}': {conteo} vez/veces")

buscar = "gato"
print(f"\n¿Cuántas veces aparece '{buscar}'? → {frecuencia.get(buscar, 0)}")
