#PAULA ALEJANDRA MONCADA CASTIBLANCO
#inicializo la clase llamada alumno
class alumno:
    #inicializo los atributos de la clase
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.nota=int(input("Ingrese la nota:  "))
        
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)
        
class nota(alumno):
    def __init__(self):
        super().__init__()
        
    def nota_final(self):
        if self.nota >= 3:
            print("su nota es: ", self.nota, "aprobo..")
        else:
            print("su nota es: ", self.nota, "no aprobo")

#bloque principal
nombre=alumno()
nombre.mostrar()
valor=nota()
valor.nota_final()

        
