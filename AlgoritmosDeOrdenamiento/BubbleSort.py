def bubbleSort(arr):
    tamanio = len(arr)
  
    # Vamos a dar 1 vuelta por numero cada item 
    # Es decir si son 10 elementos dariamos 10 vueltas
    for i in range(tamanio-1):

        # Una vuelta por cada item pero vamos terminando siempre 
        # una posicion antes (para no hacer tan ineficiente el programa)
        # Ej: la primera llega a tamaño-0-1, la segunda a tamaño-1-1,
        # tercera tamaño-2-1
        for j in range(0, tamanio-i-1):
  
            # Intercambia si el numero siguiente es menor
            
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)

# PSEUDO

# bubbleSort(array)
#   for i <- 1 to indexOfLastUnsortedElement-1
#     if leftElement > rightElement
#       swap leftElement and rightElement
# end bubbleSort

# Explicacion con imagenes: https://www.geeksforgeeks.org/bubble-sort/