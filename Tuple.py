from TupleFunction import *;

def ingrese(msj):
    respuesta=input(msj)
    return respuesta
    
laTupla = ("Manzana","Banana","Melon","Sandia","Kiwi");

respuesta=''

while respuesta!='0':
    letra=input("Ingrese la letra a buscar: ").lower()

    cantidadLetra=iterarLetras(laTupla,letra)

    print("En la tupla hay",cantidadLetra,"letras",letra)

    respuesta=ingrese("Queres seguir? Sino toca 0:");

print("Saliste gil")

    