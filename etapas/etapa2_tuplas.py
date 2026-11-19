from etapa1_listas import lista_juegos

#primero creo las 4 tuplas
tuplaVideojuego1 = (lista_juegos[0], 1998, "Aventura")
tuplaVideojuego2 = (lista_juegos[1], 2011, "Simulación")
tuplaVideojuego3 = (lista_juegos[2], 2016,"Simulación")
tuplaVideojuego4 = (lista_juegos[3], 2011,"Accion")
tuplaVideojuego5 = (lista_juegos[4], 2005, "Carreras")

#ahora creo la lista de tuplas
lista_juegos2 = [
    tuplaVideojuego1,
    tuplaVideojuego2,
    tuplaVideojuego3,
    tuplaVideojuego4,
    tuplaVideojuego5
]
#hacemos una  función que reciba una tupla y devuelva una cadena con la información del videojuego formateada
def lineaVideojuego(tuplaVideojuego):
    titulo = tuplaVideojuego[0]
    anio = tuplaVideojuego[1]
    generos = tuplaVideojuego[2]
    return f"{titulo} del {anio} pertenece al género de {generos}"

#la utilizamos para mostrar
for videojuego in lista_juegos2:
    print(lineaVideojuego(videojuego))