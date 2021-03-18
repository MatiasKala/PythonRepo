from Auto import Auto as A

class AutoVolador(A):

    def _init_(objeto,nombre,marca,cantAlas):
        super()._init_(nombre,marca)
        objeto.cantAlas=cantAlas

    def presentacion(objeto):
        print("Soy ",objeto.nombre," de marca ",objeto.marca," y tengo ",objeto.cantAlas," alas")

autoVolador=AutoVolador()
autoVolador._init_("Audi","A4",4)
autoVolador.presentacion()
autoVolador.mostrate()