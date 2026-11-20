
cache = {}   # Diccionario que actúa como caché

def fibonacci(n):
    """Calcula Fibonacci usando caché para evitar recalcular."""
    if n in cache:
        print(f"  [cache] fib({n}) = {cache[n]}")
        return cache[n]
    if n <= 1:
        resultado = n
    else:
        resultado = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = resultado  
    return resultado

print("Calculando fibonacci(6):")
print(f"Resultado: {fibonacci(6)}\n")

print("Calculando fibonacci(6) de nuevo (todo desde caché):")
print(f"Resultado: {fibonacci(6)}\n")

print(f"Contenido del caché: {cache}")
