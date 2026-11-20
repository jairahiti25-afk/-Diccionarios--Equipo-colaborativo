inventario = {
    "A001": {"nombre": "Manzana",   "precio": 10, "stock": 150},
    "B002": {"nombre": "Pan",       "precio": 25, "stock": 80},
    "C003": {"nombre": "Leche",     "precio": 22, "stock": 60},
    "D004": {"nombre": "Huevos",    "precio": 45, "stock": 200},
    "E005": {"nombre": "Naranja",   "precio": 12, "stock": 90},
}

def consultar_producto(inventario, codigo):
    """Consulta un producto por su código."""
    prod = inventario.get(codigo)
    if prod:
        print(f"\nCódigo: {codigo}")
        print(f"  Nombre : {prod['nombre']}")
        print(f"  Precio : ${prod['precio']}")
        print(f"  Stock  : {prod['stock']} unidades")
    else:
        print(f"\nCódigo '{codigo}' no encontrado en inventario.")

def productos_sin_stock(inventario):
    """Busca todos los productos con stock bajo (menos de 70)."""
    print("\n--- Productos con stock bajo (<70) ---")
    for codigo, datos in inventario.items():
        if datos["stock"] < 70:
            print(f"  {codigo} - {datos['nombre']}: {datos['stock']} uds.")

consultar_producto(inventario, "C003")
consultar_producto(inventario, "X999")
productos_sin_stock(inventario)
