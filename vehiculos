class Vehiculo():
    def __init__(self, color, ruedas): 
        self.color = color
        self.ruedas = ruedas

    def __str__(self): #utilizamos la clase STR para mostrar el texto o cadena de caracteres
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo): #aquie stamos heredandoatributos como color y ruedas desde la clase vehiculo

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )


coche = Coche("azul", 150, 4, 1200)
print(coche)
