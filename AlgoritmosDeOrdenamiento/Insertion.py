# Python program for implementation of Insertion Sort
  
# Function to do insertion sort
def insertionSort(arr):
  
    tamanio=len(arr)

    # Solo va a dar una vuelta
    for i in range(1, tamanio):
  
        # Agarra un numero clave para iterar      
        key = arr[i]

        # Crea un indice con el que va a comparar el numero clave
        # Como empieza a iterar desde 1 el indice es i-1 (0 al principio)
        j = i-1

        # Ahora itera desde el numero clave para atras hasta que llegue al 
        # principio o el mismo sea mayor al apuntado 
        # Va reemplazando los numeros que son menores por el numero clave
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        # Finalmente ubica el numero clave cuando llegua al principio o se 
        # encuentra un numero menor
        arr[j+1] = key
  
arr = [12, 11, 13, 5, 6, 4,14,-43,-13,-2,7]
insertionSort(arr)
print ("Sorted array is:")
print(arr)
  
# PSEUDO

# insertionSort(array)
#   mark first element as sorted
#   for each unsorted element X
#     'extract' the element X
#     for j <- lastSortedIndex down to 0
#       if current element j > X
#         move sorted element to the right by 1
#     break loop and insert X here
# end insertionSort  

# Explicacion con imagenes: https://www.geeksforgeeks.org/insertion-sort/