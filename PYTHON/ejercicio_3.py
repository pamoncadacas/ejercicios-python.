#PAULA ALEJANDRA MONCADA CASTIBLANCO
class calculadora:
    def __init__(self):
        self.numero1 = int(input("ingrese el primer valor"))
        self.numero2 = int(input("ingrese el segundo valor"))
    def suma (self):
        suma=self.numero1+self.numero2
        print ("la suma de los dos valores es: ", suma)
    def resta (self):
        resta=self.numero1-self.numero2
        print("la resta de los dos valores es: ", resta)
    def multiplicacion (self):
        multiplicacion=self.numero1*self.numero2
        print("la mulriplicacion de los dos valores fue de: ", multiplicacion)
    def division (self):
        division=self.numero1/self.numero2
        print("el resultado de la division de los dos numeros fue de: ", division)
    def mostrar(self):
        print("los valores son: ", self.numero1, "y", self.numero2)


#bloque principal
calcular=calculadora()
calcular.mostrar()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.division()



            
