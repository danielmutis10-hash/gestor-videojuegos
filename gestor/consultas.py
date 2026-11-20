#Devuelve una lista con los videojuegos cuyo título contenga el texto buscado
def buscar_por_titulo_parcial(catalogo, texto_busqueda):
    resultados = []
    busqueda = texto_busqueda.strip().lower()
    if busqueda == "":
        return resultados

    for juego in catalogo.values():
        if busqueda in juego["titulo"].lower():
            resultados.append(juego)

    return resultados

#Devuelve una lista con los videojuegos que pertenezcan al género indicado
def filtrar_por_genero(catalogo, genero_buscado):
    resultados = []
    genero_limpio = genero_buscado.strip().capitalize()

    for juego in catalogo.values():
        if genero_limpio in juego["generos"]:
            resultados.append(juego)

    return resultados

#Devuelve una lista con los videojuegos lanzados entre anio_inicio y anio_fin (ambos incluidos)
def filtrar_por_rango_anios(catalogo, anio_inicio, anio_fin):
    resultados = []
    for juego in catalogo.values():
        if anio_inicio <= juego["anio"] <= anio_fin:
            resultados.append(juego)
    return resultados

#Calcula y devuleve un diccionario con un total de videojuegos, total de generos, el juego más antiguo y el mas reciente
def calcular_estadisticas(catalogo):
    total = len(catalogo)
    conteo_generos = {}
    mas_antiguo = None
    mas_reciente = None

    for juego in catalogo.values():
        # Contar cada género
        for genero in juego["generos"]:
            if genero in conteo_generos:
                conteo_generos[genero] = conteo_generos[genero] + 1
            else:
                conteo_generos[genero] = 1

        # Comprobar más antiguo
        if mas_antiguo is None or juego["anio"] < mas_antiguo["anio"]:
            mas_antiguo = juego

        # Comprobar más reciente
        if mas_reciente is None or juego["anio"] > mas_reciente["anio"]:
            mas_reciente = juego

    return {
        "total": total,
        "conteo_generos": conteo_generos,
        "mas_antiguo": mas_antiguo,
        "mas_reciente": mas_reciente
    }
