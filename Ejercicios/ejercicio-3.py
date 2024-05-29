#primer producto
lapiz = input("Escribe la descripcion del lapiz: ").upper()
while len(lapiz)<40 :

    lapiz = input("vuelve a escribir la descripcion del lapiz: ").upper()
Costo1= int(input("Ingrese el costo de los lapices"))
reservas1 = int(input("Ingresa la cantidad de producto de los lapices"))



#Segundo producto
goma = input("Escribe la descripcion de la goma: ").upper()
while len(goma)<40 :
    
    goma = input("vuelve a Escribir la descripcion de la goma ").upper()
Costo2= int(input("Ingrese el costo de las gomas")) 
reservas2 = int(input("Ingresa la cantidad de producto de las Gomas"))

#costo total 
costoTotal1 = Costo1 * reservas1 
costoTotal2 = Costo2* reservas2 

print(f"El costo total es de los lapices es ${costoTotal1} CLP ")
print(f"El costo total de las gomas es de ${costoTotal2}CLP")

print()