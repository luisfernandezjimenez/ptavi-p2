import calcoo
import sys

def main():
    pass

class CalculadoraHija(calcoo.CalculadoraPadre):
	def dividir(self):
		if self.b == 0:
			sys.exit("Division by zero is not allowed");
		return (self.a/self.b)
	def multiplicar(self):	
		return (self.a*self.b)
	def leerfichero (self, fichero):
		self.fichero = fihcero

if __name__ == '__main__':
	Calculadora = CalculadoraHija()
	Calculadora.introAgmt(sys.argv[1],sys.argv[3],sys.argv[2])
	if Calculadora.op == "dividir" or Calculadora.op == "divide":
		print(Calculadora.dividir())
	if  Calculadora.op == "multiplicar" or Calculadora.op == "multiplica":
		print(Calculadora.multiplicar())
	if  Calculadora.op == "sumar" or Calculadora.op == "suma":
		print(Calculadora.sumar())
	if  Calculadora.op == "restar" or Calculadora.op == "resta":
		print(Calculadora.restar())
