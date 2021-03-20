import random

i=j=contador=0
x=y=3;
exitos=[0,0,0,0,0]
nroExito=0

while (i!=x or j!=y) or nroExito<5:
    i=random.randint(1,5000)
    j=random.randint(1,5000)
    contador=contador+1
    if(i==x and j==y):
        exitos[nroExito]=contador
        nroExito+=1


print("El intento mas largo de los ",exitos.__len__(),
    " fue ",max(exitos)," y el mas corto fue ",min(exitos))