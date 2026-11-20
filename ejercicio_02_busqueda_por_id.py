productos = {
    1001: ("Laptop",    15000),
    1002: ("Mouse",       350),
    1003: ("Teclado",     800),
    1004: ("Monitor",   5500),
    1005: ("Audífonos",  1200),
}

def buscar_producto(catalogo, id_producto):
    """Busca un producto por su ID en O(1)."""
    producto = catalogo.get(id_producto)   
    if producto:
        nombre, precio = producto
        print(f"ID {id_producto} → {nombre}  |  Precio: ${precio:,}")
    else:
        print(f"Producto con ID {id_producto} no existe.")

# Pruebas
buscar_producto(productos, 1003)
buscar_producto(productos, 9999) 
