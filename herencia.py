class cargar:
        def __init__(self): #no ingresamos los datos en el self ya que seran 0
            self.dato1 = 0
            self.dato2 = 0
            self.resultado = 0

        def ingresar(self): #creamos la funcion de ingresar para tomar valores desde el teclado
            self.dato1 = int(input("ingrese el primero valor: "))
            self.dato2 = int(input("ingrese el segundo valor:"))

        def resultado_total(self): #aqui solo almacena e imprime segun la funcion a utilizar desde las clases suma o resta
            print("self.resultado")

class suma(cargar): #heredamos los atributos de cargar para luego utilizar la funcion sumar y almacenar en resultado
        def sumar(self):
            self.resultado = self.dato1+self.dato2
            
class restar(cargar):#heredamos los atributos de cargar para luego utilizar la funcion restar y almacenar en resultado
        def sumar(self):
            self.resultado = self.dato1-self.dato2


suma1 = suma() #seleccionamos la funcion que haremos llamando la clase
suma1.ingresar() #ingresamos al atributo lo cual nos pedira sus datos 
suma1.sumar() #llamamos al atributo de sumar para sumar los datos solicitados
suma1.resultado_total() #llamamos al atributo de resultato_total para mostrar la operacion y su resultado