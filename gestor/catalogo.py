#Identificador unico para cada juego
def normalizar_titulo(titulo):
    palabras = titulo.strip().lower().split()
    return " ".join(palabras)


def crear_videojuego(catalogo, titulo, anio, generos):
    titulo_limpio = titulo.strip()
    if titulo_limpio == "":
        return False, "El título no puede estar vacío."

    if type(anio) is not int or anio <= 0:
        return False, "El año debe ser un número entero positivo."

    if len(generos) == 0:
        return False, "El videojuego debe tener al menos un género."

    clave = normalizar_titulo(titulo_limpio)
    if clave in catalogo:
        return False, "Ya existe un videojuego con ese título en el catálogo."

    generos_limpios = set()
    for genero in generos:
        genero_limpio = genero.strip().capitalize()
        if genero_limpio != "":
            generos_limpios.add(genero_limpio)

    if len(generos_limpios) == 0:
        return False, "Debes indicar al menos un género válido."

    catalogo[clave] = {
        "titulo": titulo_limpio,
        "anio": anio,
        "generos": generos_limpios
    }
    return True, "Videojuego añadido correctamente."

#Devuelve lista de los videojuegos que tenemos
def obtener_todos(catalogo):
    lista_juegos = []
    for juego in catalogo.values():
        lista_juegos.append(juego)
    return lista_juegos

#Devuelve la busqueda de un juego
def obtener_videojuego(catalogo, titulo):
    clave = normalizar_titulo(titulo)
    if clave in catalogo:
        return catalogo[clave]
    return None

#Actualiza los atributos de un juego que ya teniamos anteriormente
def actualizar_videojuego(catalogo, titulo_actual, nuevo_titulo, nuevo_anio, nuevos_generos):
    clave_actual = normalizar_titulo(titulo_actual)
    if clave_actual not in catalogo:
        return False, "No se encontró el videojuego que deseas modificar."

    titulo_limpio = nuevo_titulo.strip()
    if titulo_limpio == "":
        return False, "El nuevo título no puede estar vacío."

    if type(nuevo_anio) is not int or nuevo_anio <= 0:
        return False, "El año debe ser un número entero positivo."

    generos_limpios = set()
    for g in nuevos_generos:
        g_limpio = g.strip().capitalize()
        if g_limpio != "":
            generos_limpios.add(g_limpio)

    if len(generos_limpios) == 0:
        return False, "El videojuego debe tener al menos un género."

    nueva_clave = normalizar_titulo(titulo_limpio)

    # Si ha cambiado el nombre, comprobamos que el nuevo no choque con otro juego distinto
    if nueva_clave != clave_actual and nueva_clave in catalogo:
        return False, "Ya existe otro videojuego con ese nuevo título."

    # Si cambió la clave, borramos la antigua
    if nueva_clave != clave_actual:
        del catalogo[clave_actual]

    catalogo[nueva_clave] = {
        "titulo": titulo_limpio,
        "anio": nuevo_anio,
        "generos": generos_limpios
    }
    return True, "Videojuego actualizado correctamente."

#Eliminar el  videojuego de raiz
def eliminar_videojuego(catalogo, titulo):
    clave = normalizar_titulo(titulo)
    if clave in catalogo:
        del catalogo[clave]
        return True, "Videojuego eliminado correctamente."
    return False, "No se encontró ningún videojuego con ese título."