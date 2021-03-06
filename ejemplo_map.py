class Empleado:
	def __init__(self,nombre, cargo, salario):
		self.nombre = nombre
		self.cargo = cargo
		self.salario =salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)



listaEmpleados=[
Empleado("Juan","Director", 67000),
Empleado("Ana","Presidenta", 7500),
Empleado("Antonio","Administrativo", 27000),
Empleado("Sara","Secretaria", 2100),
Empleado("Mario","Botones", 1800)]


def calculo_comision(empleado):
	empleado.salario=empleado.salario*1.03

	return empleado



### Le aplica la funcion a toda la lista
listaEmpleadosComision=map(calculo_comision,listaEmpleados)


for empleado in listaEmpleadosComision:
	print (empleado)