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


def main():
    generos = {
        "Aventura",
        "Simulación",
        "Simulación",
        "Acción",
        "Carreras"
    }
    mostrar_generos(generos, "Géneros")

    #Pruebas

    # Añadir nuevos géneros al conjunto
    agregar_genero(generos, "Plataformas")
    agregar_genero(generos, "Puzle")
    agregar_genero(generos, "aventura")  # No se duplicará porque ya existe
    mostrar_generos(generos, "Después de añadir Plataformas y Puzle")

    # Eliminar algún género del conjunto
    eliminado = eliminar_genero(generos, "Puzle")
    if eliminado:
        print("\nSe ha eliminado 'Puzle' correctamente.")
    else:
        print("\nNo se pudo eliminar 'Puzle' porque no estaba.")
    mostrar_generos(generos, "Después de eliminar Puzle")

    #Solicitar un género y comprobar si pertenece al conjunto
    print("\n--- 4. Comprobación de género ---")
    busqueda = input("Escribe un género para ver si está en tu colección: ")
    if comprobar_genero(generos, busqueda):
        print("¡Sí! Ese género pertenece a tu colección.")
    else:
        print("No, ese género no está en tu colección.")

    # Crear otro conjunto con los géneros favoritos de otra persona
    generos_otro = {"Rpg", "Deportes", "Terror", "Acción", "Estrategia"}
    mostrar_generos(generos_otro, "5. Géneros favoritos de otra persona")

    # 6. Realizar unión, intersección y diferencia
    union, interseccion, diferencia = obtener_operaciones(generos, generos_otro)

    mostrar_generos(union, "Unión (Todos los géneros de ambos)")
    mostrar_generos(interseccion, "Intersección (Géneros en común)")
    mostrar_generos(diferencia, "Diferencia (En mi colección, pero no en la suya)")

if __name__ == "__main__":
    main() 