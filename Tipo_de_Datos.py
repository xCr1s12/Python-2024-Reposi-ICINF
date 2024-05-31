
#Bibliotecas
import math


#Strings 
Dia = "Lunes"
Mes = 'Mayo'
Asignaturas = """
Taller Introduccion ing civil inf
Programacion
"""
#INDICES 
print(Dia[3]) # imprimira el caracter en la posicion 4 ya que cuenta desde el 0 
print(Dia[-3]) #Imprimira a la inversa desde el 0   
print(len(Dia))
print(Dia[:5])# Trunca y imprime los 5 caracteres
"""
print(Dia * 4)
Salida de texto va a ser LunesLunesLunesLunes 
""" 
#Numeros

pi=3.14159
print("{:.2f}".format(pi))


#Boleanos
pescado= True
print(type(pescado))

#salidas Condicionales
print(1 >= 0)
print(100 <= 10)
print(10 == 10)

##Listas
papas= ["rayada","blanca","roja"]
cocinapapas= list(["papa al horno","papa rellena","papa papa papa de una papa","papa rellena"])
papaFrita = ["papas", 2, True]
listanum = list(range(10))


##Funciones de listas
print(type(papas))
print(len(papas))
print(cocinapapas.count("papa rellena")) #Cuenta cuantos elementos de los seleccionados hay 
print(papaFrita[1])#Imprime una posicion de una lista
print(listanum)


#TUPLAS
zanahoria = tuple()
vegetales = ("zanahoria","lechuga","repollo")
print(type(vegetales))
print(vegetales.index("lechuga"))#Imprime la posicion de un elemento

papasnuevas = tuple(cocinapapas) # se puede convertir una lista en una tupla 
print(type(cocinapapas))# cocicna papas era una lista 
print(type(papasnuevas))# papas nuevas es una tupla con los contenidos de cocinapapas 
"""
al convertir una tupla en lista se pueden cambiar valores ya que al ser tuplas son inmutables
"""


