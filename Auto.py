class Auto:
    
    def _init_(self,nombre,marca):
        
        self.nombre=nombre
        self.marca=marca

    # def ingresoNombre(self):
    #     nombre=input("Ingrese nombre :")
    #     return nombre

    # def ingresoMarca(self):
    #     marca=input("Ingrese marca :")
    #     return marca

    def mostrate(self):
        print("Soy el auto",self.nombre," de marca ",self.marca)
