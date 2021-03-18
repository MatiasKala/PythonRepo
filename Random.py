import random

i=j=contador=0
x=y=3;


while i!=x or j!=y:
    i=random.randint(1,5000)
    j=random.randint(1,5000)
    contador=contador+1

print("Hubieron ",contador," intento/s para que salga los numeros ",x," y ",y)