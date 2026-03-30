import json
import os

# Archivo para guardar los datos
ARCHIVO = 'clientes.json'

# Cargar clientes desde archivo si existe
if os.path.exists(ARCHIVO):
    with open(ARCHIVO, 'r', encoding='utf-8') as file:
        try:
            clientes = json.load(file)
        except json.JSONDecodeError:
            clientes = []
else:
    clientes = []

# Función para guardar clientes en archivo
def guardar_clientes():
    with open(ARCHIVO, 'w', encoding='utf-8') as file:
        json.dump(clientes, file, indent=4, ensure_ascii=False)

# Crear cliente
def crear_cliente():
    id_cliente = len(clientes) + 1  # ID automático
    nombre = input("Nombre: ").strip()
    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Debe ser un número entero.")
    plan = input("Tipo de plan (mensual, trimestral, anual): ").strip().lower()
    estado = input("Estado (activo/inactivo): ").strip().lower()
    
    cliente = {
        "id": id_cliente,
        "nombre": nombre,
        "edad": edad,
        "plan": plan,
        "estado": estado
    }
    clientes.append(cliente)
    guardar_clientes()
    print(f"Cliente {nombre} agregado con éxito.")

# Listar clientes
def listar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
        return
    for c in clientes:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Edad: {c['edad']} | Plan: {c['plan']} | Estado: {c['estado']}")

# Buscar cliente por ID o nombre
def buscar_cliente():
    criterio = input("Buscar por ID o nombre? ").strip().lower()
    if criterio == 'id':
        try:
            id_buscar = int(input("Ingrese ID: "))
        except ValueError:
            print("ID inválido.")
            return
        for c in clientes:
            if c['id'] == id_buscar:
                print(c)
                return
    elif criterio == 'nombre':
        nombre_buscar = input("Ingrese nombre: ").strip().lower()
        for c in clientes:
            if c['nombre'].lower() == nombre_buscar:
                print(c)
                return
    print("Cliente no encontrado.")

# Actualizar cliente
def actualizar_cliente():
    try:
        id_buscar = int(input("Ingrese ID del cliente a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    for c in clientes:
        if c['id'] == id_buscar:
            nombre = input(f"Nuevo nombre ({c['nombre']}): ").strip() or c['nombre']
            while True:
                edad_input = input(f"Nueva edad ({c['edad']}): ").strip()
                if not edad_input:
                    edad = c['edad']
                    break
                try:
                    edad = int(edad_input)
                    break
                except ValueError:
                    print("Debe ser un número.")
            plan = input(f"Nuevo plan ({c['plan']}): ").strip() or c['plan']
            estado = input(f"Nuevo estado ({c['estado']}): ").strip() or c['estado']
            c.update({"nombre": nombre, "edad": edad, "plan": plan, "estado": estado})
            guardar_clientes()
            print("Cliente actualizado.")
            return
    print("Cliente no encontrado.")

# Eliminar cliente
def eliminar_cliente():
    try:
        id_buscar = int(input("Ingrese ID del cliente a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
    for c in clientes:
        if c['id'] == id_buscar:
            clientes.remove(c)
            guardar_clientes()
            print("Cliente eliminado.")
            return
    print("Cliente no encontrado.")

# Menú principal
def menu():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Crear cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("6. Salir")
        opcion = input("Elige una opción: ").strip()
        
        if opcion == '1':
            crear_cliente()
        elif opcion == '2':
            listar_clientes()
        elif opcion == '3':
            buscar_cliente()
        elif opcion == '4':
            actualizar_cliente()
        elif opcion == '5':
            eliminar_cliente()
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecutar menú
menu()