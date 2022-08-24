class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)




def run ():
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadradro = Cuadrado(lado=5)
    print(cuadradro.area())

if __name__== "__main__":
    run()