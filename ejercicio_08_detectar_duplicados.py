
def encontrar_duplicados(lista):
    """Encuentra elementos duplicados usando un diccionario."""
    visto = {}       
    duplicados = []

    for i, elemento in enumerate(lista):
        if elemento in visto:
            duplicados.append((elemento, visto[elemento], i))
        else:
            visto[elemento] = i  

    return duplicados, visto
numeros = [4, 7, 2, 9, 7, 1, 4, 3]
dups, indice = encontrar_duplicados(numeros)
print("Lista:", numeros)
print("Duplicados (valor, pos1, pos2):", dups)
print("Índice de primeras apariciones:", indice)

usuarios = ["ana", "luis", "maría", "ana", "carlos", "luis"]
dups2, _ = encontrar_duplicados(usuarios)
print("\nUsuarios:", usuarios)
print("Duplicados:", dups2)
