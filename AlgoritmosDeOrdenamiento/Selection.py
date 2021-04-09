array = [64, 25, 12, 22, 11]
tamanio=len(array)

# Una vuelta general
for i in range(tamanio):
      
    """
    Vamos a buscar el numero mas bajo y a guardar su índice
    Al encontrarlo, lo pondremos al principio, y luego comenzaremos
    a iterar desde la segunda posicion (porque la primera ya tiene)
    al menor numero. Al contrario que con el insertion, comenzamos a 
    "cortar" la parte de atras y no la de adelante. Es decir, empezamos
    a iterar desde 0 a tamaño, luego 1 a tamaño, luego 2 a tamaño... 
    """
    min_idx = i
    for j in range(i+1, tamanio):
        if array[min_idx] > array[j]:
            min_idx = j
              
    # Intercambiamos el numero mas bajo encontrado por el primero
    array[i], array[min_idx] = array[min_idx], array[i]
  
print ("Sorted array")
print(array)