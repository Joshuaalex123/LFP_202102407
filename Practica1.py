import csv
import graphviz as gv
import os


# Función para leer el archivo .lfp y guardar la información en una lista de diccionarios
def leer_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("El archivo no existe.")
        return None
    peliculas = []
    with open(nombre_archivo, "r") as archivo:
        reader = csv.reader(archivo, delimiter=";", skipinitialspace=True)
        for linea in reader:
            pelicula = {"nombre": linea[0], "actores": linea[1].split(","), "anio": linea[2], "genero": linea[3]}
            peliculas.append(pelicula)
    return peliculas



def menu_filtrado(peliculas):
    print("Opciones de filtrado:")
    print("a. Filtrado por actor")
    print("b. Filtrado por año")
    print("c. Filtrado por género")
    opcion = input("Seleccione una opción: ")
    if opcion == "a":
        actor = input("Ingrese el nombre del actor: ")
        peliculas_actor = [pelicula for pelicula in peliculas if actor in pelicula["actores"]]
        if len(peliculas_actor) == 0:
            print(f"No se encontraron películas en las que participe {actor}.")
        else:
            print(f"Películas en las que participa {actor}:")
            for pelicula in peliculas_actor:
                print(f"- {pelicula['nombre']}")
    elif opcion == "b":
        anio = input("Ingrese el año: ")
        peliculas_anio = [pelicula for pelicula in peliculas if anio in pelicula["anio"] == anio]
        if len(peliculas_anio) == 0:
            print(f"No se encontraron películas del año {anio}.")
        else:   
            print(f"Películas estrenadas en {anio}:")
            for pelicula in peliculas_anio:
                print(f"- {pelicula['nombre']}, {pelicula['genero']}")
    elif opcion == "c":
        genero = input("Ingrese el género: ")
        peliculas_genero = [pelicula for pelicula in peliculas if genero in pelicula["genero"] == genero]
        if len(peliculas_genero) == 0:
            print(f"No se encontraron películas del género {genero}.")
        else:   
            print(f"Películas del género {genero}:")
            for pelicula in peliculas_genero:
                print(f"- {pelicula['nombre']}")
             
          
    else:
        print("Opción no válida.")


# Función para mostrar los actores de las películas
def mostrar_actores(peliculas):
    for pelicula in peliculas:
        print("--La pelicula {} tiene los siguientes actores: {}".format(pelicula["nombre"], ", ".join(pelicula["actores"])))

# Función para mostrar los años de estreno de las películas
def mostrar_anios(peliculas):
    for pelicula in peliculas:
        print("--La pelicula {} fue estrenada en el año {}".format(pelicula["nombre"], pelicula["anio"]))

# Función para mostrar los géneros de las películas
def mostrar_generos(peliculas):
    for pelicula in peliculas:
        print("--La pelicula {} es de género {}".format(pelicula["nombre"], pelicula["genero"]))

# Función para generar un diagrama de Graphviz que muestre las relaciones entre los actores y las películas
def generar_diagrama(peliculas):
    graph = gv.Digraph(format="png")
    for pelicula in peliculas:
        with graph.subgraph(name="cluster_{}".format(pelicula["nombre"])) as subgraph:
            subgraph.attr(label=pelicula["nombre"])
            for actor in pelicula["actores"]:
                subgraph.node(actor)
    graph.view()

# Menú principal
print("Joshua Alexander Vasquez del Aguila Lenguajes Formales y de Programación, sección A-, carné 202102407")
input("Presione cualquier tecla para continuar...") 
while True:
        print("1) Cargar archivo de entrada")
        print("2) Mostrar actores")
        print("3) Mostrar años de estreno")
        print("4) Mostrar géneros")
        print("5) Generar diagrama")
        print("6) Filtrar")
        print("0) Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 0:
            print("El programa ha completado su ejecución")

            break
        elif opcion == 1:
            nombre_archivo = input("Introduzca el nombre del archivo: ")
            peliculas = leer_archivo(nombre_archivo)
            if peliculas is None:
                continue
        
            input("Archivo cargado correctamente. Presione Enter para continuar...")
        elif opcion == 2:
            mostrar_actores(peliculas)
            input("Presione Enter para continuar...")
        elif opcion == 3:
            mostrar_anios(peliculas)
            input("Presione Enter para continuar...")
        elif opcion == 4:
            mostrar_generos(peliculas)
            input("Presione Enter para continuar...")
        elif opcion == 5:
            generar_diagrama(peliculas)
        elif opcion == 6:
            menu_filtrado(peliculas)
        else:
            print("Opción inválida")


