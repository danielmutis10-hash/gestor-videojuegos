
"""ESTRUCTURA CATALOGO:
Clave: identificador único obtenido a partir del título normalizado, ignorando
mayúsculas, minúsculas y espacios adicionales.
Valor: diccionario con los siguientes datos:
◦ titulo: título del videojuego (cadena).
◦ anio: año de lanzamiento (entero).
◦ generos: géneros del videojuego (conjunto de cadenas).
"""



#buscar por título completo o parcial, primero eliminamos espacios y convertimos a minúsculas y luego vamos añadiendo los juegos encontrados a la lista vacia
def buscarPorTitulo (catalogo, texto):
    texto = texto.strip().casefold()
    resultados = []
    for videojuego in catalogo.values():
        if texto in videojuego["titulo"].casefold():#comprueba si el texto está dentro del título                   
            resultados.append(videojuego)
    return resultados

#Un videojuego podrá pertenecer a varios géneros (ya que es un conjunto de cadenas)
def buscarPorGenero(catalogo, genero):
    genero = genero.strip().casefold()
    resultados = []
    for videojuego in catalogo.values():
        encontrado = False
        for generoCatalogo in videojuego["generos"]:
            generoCatalogo = generoCatalogo.casefold()#tambien normalizo el genero en el catalogo para comparar
            if generoCatalogo == genero:
                encontrado = True
        if encontrado:
            resultados.append(videojuego)
    return resultados



#buscar entre dos años
def buscarPorAnios(catalogo,inicio,fin):
    resultados = []
    for videojuego in catalogo.values():
        if inicio <= videojuego["anio"] <= fin:
            resultados.append(videojuego)
    return resultados


