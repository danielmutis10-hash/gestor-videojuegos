#Los juegos elegidos en un array
lista_juegos = [
    "TLOZ Ocarina of Time",
    "Cooking Mama 4",
    "Stardew Valley",
    "Dark Souls",
    "Mario Kart DS",
]

#***********FUNCIONES**************

def anadir_videojuego(juegos, titulo): #Pide el array y el juego, y lo mete al fial
    juegos.append(titulo)

def insertar_videojuego(juegos, posicion, titulo): #Para meterlo en una posición determinada
    juegos.insert(posicion, titulo)

def eliminar_videojuego(juegos, titulo):
    if titulo in juegos: #Si no existe, el remove da error así que comprobamos primero
        juegos.remove(titulo)
        return True
    return False
    #Si lo puede eliminar devuelve true, y si no false

def ordenar_videojuegos(juegos):
    return sorted(juegos, key=str.lower) #Por si acaso usamos key=str.lower para comparar entre mayus y minus
    #Devuelve el array ordenado

def mostrar_numerados(juegos):
    for i in range(len(juegos)):
        print(f"{i + 1}. {juegos[i]}") #Por cada juego, me devuelve su titulo y me indica su posición


def main():

    juegos = list(lista_juegos) #COPIAMOS LA LISTA así no se modifica la real

    #PRUEBAS DE LAS FUNCIONES:
    print("Lista inicial:")
    mostrar_numerados(juegos)

    anadir_videojuego(juegos, "Elden Ring")
    insertar_videojuego(juegos, 1, "Dave the Diver")
    
    print("Tras la inserción:")
    mostrar_numerados(juegos)

    if eliminar_videojuego(juegos, "Cooking Mama 4"):
        print("Tras eliminar:")
    else:
        print("No se encontró el videojuego a eliminar:")
    mostrar_numerados(juegos)

    print("Ordenados alfabéticamente:")
    mostrar_numerados(ordenar_videojuegos(juegos))

#De esta forma la prueba se queda aquí, si se llama desde fuera no se ejecutan las pruebas
if __name__ == "__main__":
    main()