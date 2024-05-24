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
print(Dia[5])# Trunca y imprime los 5 caracteres
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

#COndicionales

if pescado == False: 
    print("El pescado esta malo")
if pescado == True: 
    print("El pescado esta bueno")

#Bucle While 
while pescado == False:  #Mientras el pescado sea Falso
    print("El pescado esta malo") #Escribr el pescado esta malo
    break# cerrar el bucle

while pescado == 2:  #Mientras el pescado sea Falso    -------- LA CONDICION HARA QUE SE REPITA MIENTRAS LA CONDICION ESTE ACTIVA
    print("El pescado esta Bueno") #Escribr el pescado esta Bueno