

from gestor.catalogo import (obtener_todos,obtener_videojuego,crear_videojuego,
    actualizar_videojuego,eliminar_videojuego)

from gestor.consultas import (buscar_por_titulo_parcial,filtrar_por_genero,
    filtrar_por_rango_anios,calcular_estadisticas)


#FUNCIONES PARA MOSTRAR VIDEOJUEGO O LISTA
#Funcion general para mostrar datos
def mostrar_videojuego(juego):
    print(f"\nTítulo: {juego['titulo']}")
    print(f"Año: {juego['anio']}")
    print(f"Géneros: {', '.join(juego['generos'])}")

#Mostrar varios videojuegos si existen
def mostrar_lista_videojuegos(videojuegos):
    if len(videojuegos) == 0:
        print("\nNo hay videojuegos para mostrar.")
        return
    for juego in videojuegos:
        mostrar_videojuego(juego)

#PARA PEDIR DATOS
#Pide un numero hasta que sea positivo
def pedir_anio(mensaje):
    while True:
        try:
            anio = int(input(mensaje))
            if anio > 0:
                return anio
            print("El año debe ser un número positivo.")
        except ValueError:
            print("Debes introducir un número entero.")


#FUNCIONES PARA GESTONIAR VIDEOJUEGOS INEXISTENTES, BUSQUEDAS SIN RESULTADOS Y ENTRADAS INCORRECTAS
#Si no se encuentan videojuegos con ese titulo
def opcion_buscar_exacta(catalogo):
    titulo = input("Introduce el título del videojuego: ")
    juego = obtener_videojuego(catalogo, titulo)

    if juego is None:
        print("No se ha encontrado el videojuego.")
    else:
        mostrar_videojuego(juego)
        
#Si no se encuentan videojuegos con ese titulo
def opcion_buscar_parcial(catalogo):
    texto = input("Introduce el título exacto o parcial: ")
    resultados = buscar_por_titulo_parcial(catalogo, texto)
    if len(resultados) == 0:
        print("No se han encontrado videojuegos.")
    else:
        mostrar_lista_videojuegos(resultados)

#Si no se encuentan videojuegos con ese genero
def opcion_filtrar_genero(catalogo):
    genero = input("Introduce el género que deseas buscar: ")
    resultados = filtrar_por_genero(catalogo, genero)
    if len(resultados) == 0:
        print("No se han encontrado videojuegos de ese género.")
    else:
        mostrar_lista_videojuegos(resultados)


#Combrueba que inicio sea menor que mayor y que haya videojuegos
def opcion_filtrar_anios(catalogo):
    inicio = pedir_anio("Introduce el año inicial: ")
    fin = pedir_anio("Introduce el año final: ")
    if inicio > fin:
        print("El año inicial no puede ser mayor que el año final.")
        return
    resultados = filtrar_por_rango_anios(catalogo, inicio, fin)
    if len(resultados) == 0:
        print("No se han encontrado videojuegos en ese rango.")
    else:
        mostrar_lista_videojuegos(resultados)


#de crear, modificar o eliminar videojuego no hae falta generar mensajes de error aqui porque ya estan en la propia funcion. Solo ponemos los input
def opcion_añadir(catalogo):
    titulo = input("Introduce el título: ")
    anio = pedir_anio("Introduce el año: ")
    generos = input("Introduce los géneros separados por comas: ").split(",")
    #la funcion devuleve un boolean y el texto
    correcto, mensaje = crear_videojuego(catalogo, titulo, anio, generos)
    print(mensaje)



def opcion_modificar(catalogo):
    titulo_actual = input("Introduce el título del videojuego que deseas modificar: ")
    nuevo_titulo = input("Introduce el nuevo título: ")
    nuevo_anio = pedir_anio("Introduce el nuevo año: ")
    nuevos_generos = input("Introduce los nuevos géneros separados por comas: ").split(",")
    correcto, mensaje = actualizar_videojuego(catalogo, titulo_actual, nuevo_titulo, nuevo_anio, nuevos_generos)
    print(mensaje)



def opcion_eliminar(catalogo):
    titulo = input("Introduce el título del videojuego que deseas eliminar: ")
    correcto, mensaje = eliminar_videojuego(catalogo, titulo)
    print(mensaje)



#Escribe cuando no haya generos o no este el mas antiguo o reciente
def opcion_estadisticas(catalogo):
    estadisticas = calcular_estadisticas(catalogo)
    print(f"Total de videojuegos: {estadisticas['total']}")

    print("\nVideojuegos por género:")
    if len(estadisticas["conteo_generos"]) == 0:
        print("No hay géneros registrados.")
    else:
        for genero, cantidad in estadisticas["conteo_generos"].items():
            print(f"Hay {cantidad} que pertenecen al género de {genero}")
    #Si hay videojuegos, mostramos el más antiguo y el más reciente (y si hay solo uno sera el mismo)
    if estadisticas["mas_antiguo"] is not None and estadisticas["mas_reciente"] is not None:
        print(f"\nVideojuego más antiguo: {estadisticas['mas_antiguo']}")
        print(f"\nVideojuego más reciente: {estadisticas['mas_reciente']}")
    else:
        print("\nNo hay videojuegos")


# Ejecuta el menú principal
def mostrar_menu(catalogo):
    opcion = ""

    while opcion != "0":
        print("\n Elige una opción:")
        print("1. Mostrar videojuegos")
        print("2. Buscar por título exacto")
        print("3. Buscar por título parcial o exacto")
        print("4. Filtrar por género")
        print("5. Filtrar por rango de años")
        print("6. Añadir videojuego")
        print("7. Modificar videojuego")
        print("8. Eliminar videojuego")
        print("9. Mostrar estadísticas")
        print("0. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            videojuegos = obtener_todos(catalogo)
            mostrar_lista_videojuegos(videojuegos)

        elif opcion == "2":
            opcion_buscar_exacta(catalogo)

        elif opcion == "3":
            opcion_buscar_parcial(catalogo)

        elif opcion == "4":
            opcion_filtrar_genero(catalogo)

        elif opcion == "5":
            opcion_filtrar_anios(catalogo)

        elif opcion == "6":
            opcion_añadir(catalogo)

        elif opcion == "7":
            opcion_modificar(catalogo)

        elif opcion == "8":
            opcion_eliminar(catalogo)

        elif opcion == "9":
            opcion_estadisticas(catalogo)

        elif opcion == "0":
            print("Se ha termina el programa")
            break

        else:
            print("Opción no válida")
