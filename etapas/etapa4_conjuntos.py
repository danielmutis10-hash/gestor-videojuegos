"""Mostrar generos que tenemos"""
def mostrar_generos(generos, titulo):
    print("\n--- " + titulo + " ---")
    if len(generos) == 0:
        print("No hay géneros en este conjunto.")
    else:
        for genero in generos:
            print("- " + genero)

"""Agregar más generos a los propios"""
def agregar_genero(generos, nuevo_genero):
    genero_limpio = nuevo_genero.strip().capitalize()
    if genero_limpio != "":
        generos.add(genero_limpio)

"""Eliminar generos de la lista"""
def eliminar_genero(generos, genero_objetivo):
    genero_limpio = genero_objetivo.strip().capitalize()
    if genero_limpio in generos:
        generos.remove(genero_limpio)
        return True
    else:
        return False

"""Comprobar si un genero solicitado existe en el nuestro"""
def comprobar_genero(generos, genero_buscado):
    genero_limpio = genero_buscado.strip().capitalize()
    if genero_limpio in generos:
        return True
    else:
        return False

"""Union, interseccion y diferencia entre nuestro conjunto y otro externo"""
def obtener_operaciones(conjunto1, conjunto2):
    union = conjunto1.union(conjunto2)
    interseccion = conjunto1.intersection(conjunto2)
    diferencia = conjunto1.difference(conjunto2)
    return union, interseccion, diferencia