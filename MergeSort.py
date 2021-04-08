def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # Va a ir cortando los arrays hasta llegar a 1
        mergeSort(lefthalf) 
        mergeSort(righthalf)

        # Cuando llega a 1, vuelve a la pila de llamadas de cuando eran 2, despues 4 y asi a la primera

        i=0
        j=0
        k=0
       
        # Ahora empieza a comparar entre las dos partes hasta que el indice de un array llegue al tamaño (es decir, que no queden mas elementos para comparar, porque se terminan de reemplazar luego)

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
 
        # Luego de ir comparando entre los dos arrays, termina de vaciar el que quede con algo (porque ya esta ordenado)
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)