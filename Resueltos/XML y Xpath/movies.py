
# Crea un script de python que solicite por pantalla:
# - Un rating de edad
# - un genero
# - Una duracion minima
# Muestre las peliculas que cumplen los requisitos

#Si es un atributo se le pone un arroba antes, los elementos NO

from lxml import etree

"""
tree = etree.parse ("movies.xml")
root = tree.getroot()


duracionMinima=input("Dime la duracion minima: ")
ratingEdad=input("Dime un rating de edad: ")
genero=input("Dime el genero a buscar: ")


print(root.xpath(f"Movie[@rating='{ratingEdad}'][Genre='{genero}']/Titles[@runtime>='{duracionMinima}']/text()"))
"""
# Crea un script de python que muestre por pantalla:
# 1 - La pelicula mas larga
# 2 - La pelicula mas corta
# 3 - La duracion media de las peliculas
# 4 - Ten en cuenta que no todas las peliculas disponen del dato de duracion.
#
# Ademas, el script debe solicitar por pantalla el nombre de una pelicula.
# y mostrar por pantalla si esta por encima o por debajo de la media.
#
# Si la pelicula solicitada no tiene duracion, debe solicitar una pelicula nueva hasta que sea valida.


tree = etree.parse ("movies.xml")
root = tree.getroot()

duracionPeliculas=root.xpath(f"Movie/Title/@runtime")

# Coger la pelicula mas corta:

peliculaMasCortaDuracion=min(duracionPeliculas)
print("La pelicula mas corta es: ")
print(root.xpath(f"Movie/Title[@runtime='{peliculaMasCortaDuracion}']/text()"))


# Coger la pelicula mas larga

peliculaMasLargaDuracion=max(duracionPeliculas)
print("La pelicula mas corta es: ")
print(root.xpath(f"Movie/Title[@runtime='{peliculaMasLargaDuracion}']/text()"))

# Hacer la media de todas las pelis
duracionTotalPeliculas=0

for pelicula in duracionPeliculas:
    duracionTotalPeliculas+=int(pelicula)

numTotalPeliculas=len(duracionPeliculas)
mediaPeliculas=duracionTotalPeliculas//numTotalPeliculas

print(f"La media de todas las peliculas es: {mediaPeliculas}")

# SOLICITAR PELICULA Y ESO

peliculaSolicitada=input("Dime el nombre de una pelicula a buscar: ")
duracionPeliculaSolicitada=duracionPeliculas.index(peliculaSolicitada)

while duracionPeliculaSolicitada == "":
    peliculaSolicitada=input("Error, esa pelicula no tiene duracion. Dime el nombre de una pelicula a buscar: ")
    duracionPeliculaSolicitada=duracionPeliculas.index(peliculaSolicitada)

if duracionPeliculaSolicitada>mediaPeliculas:
    print(f"La pelicula {peliculaSolicitada} es mas larga que la media de peliculas en la lista ({mediaPeliculas} mins.). ")
elif duracionPeliculaSolicitada<mediaPeliculas:
    print(f"La pelicula {peliculaSolicitada} es mas corta que la media de peliculas en la lista ({mediaPeliculas} mins.). ")