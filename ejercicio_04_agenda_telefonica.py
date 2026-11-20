agenda = {
    "Ana López":    "555-1001",
    "Luis Ramírez": "555-2002",
    "María Torres": "555-3003",
}

def mostrar_agenda(agenda):
    print("\n--- Agenda ---")
    for nombre, tel in agenda.items():
        print(f"  {nombre}: {tel}")

def buscar_contacto(agenda, nombre):
    tel = agenda.get(nombre, "No encontrado")
    print(f"\nBúsqueda '{nombre}': {tel}")

agenda["Carlos Vega"] = "555-4004"

agenda["Ana López"] = "555-9999"

del agenda["Luis Ramírez"]

mostrar_agenda(agenda)
buscar_contacto(agenda, "Carlos Vega")
buscar_contacto(agenda, "Luis Ramírez")  
