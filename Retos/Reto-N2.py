#Importo OS para un detalle estetico :3
import os

#Guardo las notas de los lab 
Nota1_Historia = float(input("Inrese la nota del Lab1 de Historia: "))
Nota2_Historia = float(input("\nInrese la nota del Lab2 de Historia: "))
Nota3_Historia = float(input("\nInrese la nota del Lab3 de Historia: "))

os.system("cls")

Nota1_Lenguaje = float(input("Inrese la nota del Lab1 de Lenguaje: "))
Nota2_Lenguaje = float(input("\nInrese la nota del Lab2 de Lenguaje: "))
Nota3_Lenguaje = float(input("\nInrese la nota del Lab3 de Lenguaje: "))

os.system("cls")

Nota1_Matematicas = float(input("Inrese la nota del Lab1 de Matematicas: "))
Nota2_Matematicas = float(input("\nInrese la nota del Lab2 de Matematicas: "))
Nota3_Matematicas = float(input("\nInrese la nota del Lab3 de Matematicas: "))


#Creo sets con las notas
Historia_set = {Nota1_Historia , Nota2_Historia , Nota3_Historia}
Lenguaje_set = {Nota1_Lenguaje , Nota2_Lenguaje , Nota3_Lenguaje}
Matematicas_set = {Nota1_Matematicas , Nota2_Matematicas , Nota3_Matematicas}
os.system("cls")
#saco los promedios 

Prom_Historia = (Nota1_Historia*0.30)+(Nota2_Historia*0.50)+(Nota3_Historia*0.20)
Prom_Lenguaje = (Nota1_Lenguaje*0.30)+(Nota2_Lenguaje*0.50)+(Nota3_Lenguaje*0.20)
Prom_Matematicas = (Nota1_Matematicas*0.30)+(Nota2_Matematicas*0.50)+(Nota3_Matematicas*0.20)

#Almaceno la informacion en una tupla 
Historia_Tupl = ("Historia",Historia_set,round(Prom_Historia,1))
Lenguaje_Tupl = ("Lenguaje",Lenguaje_set,"{:.1f}".format(Prom_Lenguaje))
matematicas_Tupl = ("Matematicas",Matematicas_set,"{:.1f}".format(Prom_Matematicas))

#Creo la lista que contiene cada tupla con su informacion
Informacion = [Historia_Tupl,Lenguaje_Tupl,matematicas_Tupl]

#Y por ultimo creo el diccionario con el nombre del estudiante
calificaion= { "Diego" : Informacion}

print(calificaion["Diego"])