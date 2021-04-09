def shellSort(arr):
    """
    Este ordenamiento se basa en la comparacion entre dos numeros separados por
    un salto que cada iteracion se va achicando hasta llegar a 1 (pareciendose 
    al insertion pero con la ventaja de haber sido ordenado por iteraciones an-
    teriores).
    """
    tamanio = len(arr)
    salto = int(tamanio/2)

    """
    Ahora iteramos hasta que el salto sea cero (Se va a ir dividiendo por 2 hasta llegar a 1)
    Cuando llega a 1 funciona IGUAL que el insertion, pero gracias a los saltos ya esta media-
    namente mas ordenado, lo que agiliza mucho el ordenamiento
    """

    while salto > 0:
  
        for i in range(salto,tamanio):
  
            """
            Comenzamos a iterar con el numero clave que es el salto
            (tamaño/2 al principio y luego /2 hasta llegar a 1)
            """
            clave = arr[i]
  
            """
            Preguntamos si el numero clave es mayor a arr[posActual-salto]
            Ejemplo si el salto es 5 empezamos comparando posicion 5 con 0,
            luego 6 con 1, 7 con 2, asi. Si por ejemplo tenemos saltos de 2 
            y encontramos que el arr[8] es mayor al arr[6], se seguira ite-
            rando para abajo como si fuera un insertion, solo que se ira
            restando el indice menos el salto, en este caso, se iterara el 
            arr[6] vs el arr[4] (Tambien se reemplaza el indice al final
            como en el insertion).
            """
            j = i
            while  j >= salto and arr[j-salto] >clave:
                arr[j] = arr[j-salto]
                j -= salto
  
            # Aca termina de meter el valor clave (como en el insertion)
            arr[j] = clave
        salto=int(salto/2)

    return arr

array=shellSort([2,48,283,82,71,23,82,73,12,33,14,518,1,23,2,93,19])
print(array)