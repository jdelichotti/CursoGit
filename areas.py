import math
import doctest

def raizCuadrada(listaNumeros):
	"""Devuelve el cuadrado de los nuneris
	>>> lista=[]
	>>> for i in [4,9,16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]
	
	>>> for i in [4,-9,16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
  	...
  	ValueError: math domain error
	"""
	return [math.sqrt(n) for n in listaNumeros]


print (raizCuadrada([9,16,25]))

#doctest.testmod()#
