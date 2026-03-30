import json
import os # Importamos 'os' para manejar rutas del sistema operativo

# --- TRUCO PARA EVITAR ERRORES DE ARCHIVO NO ENCONTRADO ---
# Esto detecta en qué carpeta exacta está guardado este script (.py),
# sin importar desde dónde lo ejecutes en tu computadora.
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))

# Construimos la ruta completa uniendo la carpeta con el nombre del archivo
ruta_datos_iniciales = os.path.join(DIRECTORIO_ACTUAL, 'datos_iniciales.json')
ruta_datos_actualizados = os.path.join(DIRECTORIO_ACTUAL, 'datos_actualizados.json')

# ==========================================
# PARTE 1: LEYENDO UN ARCHIVO JSON
# ==========================================
print("--- LEYENDO DATOS JSON ---")

# 1. Abrimos el archivo pasándole la ruta completa que calculamos arriba
with open(ruta_datos_iniciales, 'r', encoding='utf-8') as archivo_lectura:
    # 2. json.load() convierte el texto del archivo en objetos de Python (listas/diccionarios)
    datos = json.load(archivo_lectura)

print("Datos cargados del archivo:")
print(datos)
print("\n¿Qué tipo de dato es en Python?:", type(datos)) # Verás que es una lista (list)

# Como es una lista de diccionarios, podemos iterar sobre los datos como cualquier lista normal
print("\nDetalle de cada persona:")
for persona in datos:
    # Accedemos a los valores del diccionario usando la clave entre corchetes
    print(f"- Nombre: {persona['nombre']}, Ciudad: {persona['ciudad']}")

# ==========================================
# PARTE 2: ESCRIBIENDO A UN ARCHIVO JSON
# ==========================================
print("\n--- ESCRIBIENDO NUEVOS DATOS JSON ---")

# 1. Vamos a crear nuevos datos en Python (una lista de diccionarios)
nuevos_datos = [
    {
        "nombre": "Beatriz", 
        "edad": 25, 
        "ciudad": "Valencia", 
        "habilidades": ["JavaScript", "HTML"]
    },
    {
        "nombre": "David", 
        "edad": 40, 
        "ciudad": "Sevilla", 
        "habilidades": ["Python", "AWS"]
    }
]

# 2. Agregamos los nuevos datos a los que ya teníamos (concatenando listas)
datos_completos = datos + nuevos_datos

# 3. Abrimos un NUEVO archivo en modo escritura ('w' de write)
with open(ruta_datos_actualizados, 'w', encoding='utf-8') as archivo_escritura:
    # 4. json.dump() toma nuestros objetos de Python y los guarda como texto JSON en el archivo
    
    # Explicación de los parámetros:
    # datos_completos: lo que queremos guardar
    # archivo_escritura: dónde lo queremos guardar
    # indent=4: le da un formato bonito y fácil de leer (con espacios de sangría)
    # ensure_ascii=False: permite que los acentos y tildes se guarden correctamente en lugar de códigos extraños
    
    json.dump(datos_completos, archivo_escritura, indent=4, ensure_ascii=False)

print("¡Éxito! Hemos creado 'datos_actualizados.json' y guardado los nuevos datos allí.")


# ==========================================
# PARTE 3: CRUD CON UNA LISTA DE DICCIONARIOS (JSON)
# ==========================================
print("\n--- EJEMPLO DE CRUD (Crear, Leer, Actualizar, Borrar) ---")

# Imaginemos que leímos un JSON y ahora lo tenemos en la variable lista 'mi_base_de_datos'
mi_base_de_datos = [
    {"id": 1, "nombre": "Juan", "rol": "Admin"},
    {"id": 2, "nombre": "Maria", "rol": "Usuario"}
]
print("Estado Inicial:", mi_base_de_datos)

# ------------------------------------------
# 1. CREATE (Crear / Añadir nuevo elemento)
# ------------------------------------------
# Creamos un Nuevo diccionario y lo agregamos a la lista con .append()
nuevo_usuario = {"id": 3, "nombre": "Pedro", "rol": "Invitado"}
mi_base_de_datos.append(nuevo_usuario)

print("\n[C] Después de CREAR (adicionar) a Pedro:")
print(mi_base_de_datos)

# ------------------------------------------
# 2. READ (Leer / Buscar algún elemento)
# ------------------------------------------
# Buscamos en la lista iterando sobre ella para encontrar el id=2
print("\n[R] Buscando (LEER) al usuario con id 2:")
for usuario in mi_base_de_datos:
    if usuario["id"] == 2:
        print(f"¡Encontrado!: {usuario['nombre']} (Rol: {usuario['rol']})")

# ------------------------------------------
# 3. UPDATE (Actualizar / Modificar datos)
# ------------------------------------------
# Para modificar, primero buscamos a la persona, y luego le cambiamos sus llaves
print("\n[U] Actualizando (UPDATE) el rol de Pedro (Pasa de 'Invitado' a 'Usuario'):")
for usuario in mi_base_de_datos:
    if usuario["nombre"] == "Pedro":
        usuario["rol"] = "Usuario" # ¡Aquí hacemos la modificación, reasignando su valor!

print(mi_base_de_datos)

# ------------------------------------------
# 4. DELETE (Borrar / Eliminar un elemento)
# ------------------------------------------
# Lo más fácil en Python es sobreescribir la lista con todos los objetos MENOS el que queremos borrar
print("\n[D] Borrando (DELETE) a Juan (el id 1):")

# Como principiante, la forma más fácil de entender cómo "borrar",
# es simplemente creando una nueva lista y agregando a todos
# los que NO queremos borrar (es decir, todos menos Juan, que tiene el id 1).

nueva_lista_sin_juan = []

for usuario in mi_base_de_datos:
    # Si el id del usuario ¡NO ES igual a 1! (!= significa diferente)
    if usuario["id"] != 1:
        # Lo agregamos a nuestra nueva lista a salvo
        nueva_lista_sin_juan.append(usuario)

# Finalmente, reemplazamos nuestra antigua base de datos con la nueva lista
mi_base_de_datos = nueva_lista_sin_juan

print("Base de datos actual después de borrar:")
for usuario in mi_base_de_datos:
    print(f"- {usuario['nombre']}")

# ------------------------------------------
# ¿Y PARA GUARDAR? 
# ------------------------------------------
# Al final, para que estos cambios NO se pierdan al cerrar el programa, 
# tendrías que volver a guardar esta lista en tu archivo JSON así:
#
# with open('usuarios.json', 'w', encoding='utf-8') as archivo:
#     json.dump(mi_base_de_datos, archivo, indent=4)


# ==========================================
# PARTE 4: MANEJO DE ERRORES AL TRABAJAR CON JSON
# ==========================================
print("\n--- MANEJO DE ERRORES ---")

# Al trabajar con archivos, siempre es una buena práctica usar bloques try...except
# para evitar que el programa se "rompa" o cierre bruscamente si algo sale mal.

# 1. Error de archivo no encontrado (FileNotFoundError)
# Esto ocurre comúnmente cuando la ruta o el nombre están mal escritos.
ruta_archivo_falso = os.path.join(DIRECTORIO_ACTUAL, 'archivo_que_no_existe.json')

print("\nIntentando leer un archivo inexistente:")
try:
    with open(ruta_archivo_falso, 'r', encoding='utf-8') as archivo:
        datos_falsos = json.load(archivo)
except FileNotFoundError:
    print("❌ ERROR CAPTURADO (FileNotFoundError): El archivo no fue encontrado.")
    print("   💡 Solución: Verifica que el archivo exista en la ruta especificada.")
except Exception as e:
    # Este bloque atrapa cualquier otro error no previsto
    print(f"❌ ERROR INESPERADO: {e}")

# 2. Error de lectura o decodificación del JSON (JSONDecodeError)
# Esto pasa cuando el archivo existe, pero en su interior está vacío o tiene texto plano
# que no respeta la estructura estricta de un JSON (usar comillas dobles, llaves, etc)
ruta_json_invalido = os.path.join(DIRECTORIO_ACTUAL, 'json_malformado.json')

# Primero, creamos a propósito un archivo que tiene formato incorrecto
with open(ruta_json_invalido, 'w', encoding='utf-8') as archivo:
    # Esto dará error porque usa comillas simples en lugar de dobles,
    # y la clave 'nombre' no tiene comillas. (O simplemente escribiendo texto normal)
    archivo.write("{nombre: 'Maria'}")

print("\nIntentando leer un archivo con formato JSON incorrecto:")
try:
    with open(ruta_json_invalido, 'r', encoding='utf-8') as archivo:
        # Aquí 'json.load' intentará traducirlo y se dará cuenta que la estructura está mal
        datos_malos = json.load(archivo)
except json.decoder.JSONDecodeError as error_detalle:
    print("❌ ERROR CAPTURADO (JSONDecodeError): El archivo no tiene un formato JSON válido.")
    print(f"   💡 Detalle técnico del error: {error_detalle}")
    print("   💡 Solución: Asegúrate de que las propiedades tengan comillas dobles (\") y la estructura sea correcta.")
except FileNotFoundError:
    print("❌ ERROR: El archivo no existe.")

# Para mantener la limpieza, borramos el archivo de prueba que acabamos de crear
if os.path.exists(ruta_json_invalido):
    os.remove(ruta_json_invalido)

