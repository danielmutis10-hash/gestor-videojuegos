
generos_juegos = {}

def mostrarGeneros(generos_juegos):
    return print(generos_juegos)

def añadirGenero(generos_juegos):
    generos_juegos.add(input("Genero a añadir"))

    return generos_juegos

def eliminarGenero(generos_juegos):
    try:
        
        print(generos_juegos),
        eliminar = input("Genero a eliminar")
        generos_juegos.discard(eliminar)
    except ValueError:
        print(f"Error con el nombre seleccionado {eliminar}")
    except Exception as e:
        print(f"Ha ocurrido un error {e}")

    return generos_juegos


