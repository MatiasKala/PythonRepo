def iterarLetras(laTupla,letra):
    cantidadLetra=0
    for item in laTupla: 
        
        cantidadPorItem=0
        
        for letter in item: 
            if letter.lower() == letra:
                cantidadPorItem+=1
        
        if cantidadPorItem==0:
           print("No hay letras '",letra,"' en",item)
        else:
           cantidadLetra+=cantidadPorItem
           print("En ",item," hay ",cantidadPorItem,"'",letra,"'")
           
    return cantidadLetra;
   




                    