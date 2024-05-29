#Precios Unitarios 
PmU = 100 
PpU = 250 
PdU = 300

#Cantidad 
Cm = 150
Cp = 80 
Cd = 120 

#Valor de cada fruta 
Total_Manzana = PmU * Cm 
Total_Pera = PpU * Cp 
Total_Durazno = PdU * Cd 

#Salida a pantalla
print("########################################TOTAL############################################")
print(f"El total por todas las manzanas es {Total_Manzana} y cada una tiene un valor de {PmU}")
print(f"El total por todas las peras es {Total_Pera} y cada una tiene un valor de {PpU}")
print(f"El total por todos los Duraznos es {Total_Durazno} y cada uno tiene un valor de {PdU}")

print(f"El total a pagar si se compran las peras y las manzanas es {Total_Manzana + Total_Pera}")
print(f"El Valor mas alto entre los 3 totales es de {max(Total_Durazno,Total_Manzana,Total_Pera)}")
print(f"El el Valor minimo entre los 3 totales es de {min(Total_Durazno,Total_Manzana,Total_Pera)}")
print(f"Y el Promedio entre los precios unitarios de las frutas es de {(PmU + PdU + PpU)/3}")