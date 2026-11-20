documentos = {
    "doc1": "python es un lenguaje de programación",
    "doc2": "los diccionarios en python son rápidos",
    "doc3": "la programación con python es divertida",
    "doc4": "los lenguajes de programación son variados",
}
indice = {}
for doc_id, contenido in documentos.items():
    for palabra in contenido.split():
        if palabra not in indice:
            indice[palabra] = []
        indice[palabra].append(doc_id)
def buscar_palabra(indice, palabra):
    resultados = indice.get(palabra, [])
    if resultados:
        print(f"'{palabra}' encontrada en: {resultados}")
    else:
        print(f"'{palabra}' no está en ningún documento.")

buscar_palabra(indice, "python")
buscar_palabra(indice, "programación")
buscar_palabra(indice, "java")  
