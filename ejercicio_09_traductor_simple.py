diccionario_es_en = {
    "hola":       "hello",
    "mundo":      "world",
    "casa":       "house",
    "perro":      "dog",
    "gato":       "cat",
    "computadora": "computer",
    "libro":      "book",
    "agua":       "water",
    "sol":        "sun",
    "luna":       "moon",
}

def traducir_frase(frase, diccionario):
    """Traduce una frase palabra por palabra."""
    palabras = frase.lower().split()
    traduccion = []
    for palabra in palabras:
        traducida = diccionario.get(palabra, f"[{palabra}?]")  
        traduccion.append(traducida)
    return " ".join(traduccion)


frases = [
    "hola mundo",
    "el perro y el gato",
    "casa computadora libro",
    "hola universo",  
]

print("=== Traductor Español → Inglés ===")
for frase in frases:
    resultado = traducir_frase(frase, diccionario_es_en)
    print(f"  '{frase}' → '{resultado}'")
