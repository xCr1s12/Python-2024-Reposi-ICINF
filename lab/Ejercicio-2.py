resumen = input("Ingrese un breve resumen ")
VarBool = len(resumen)<= 60

print(f"La longitud de el resumen es de: {len(resumen)}")
print(resumen.upper())
print(resumen[-10:-1])
print("-".join(resumen.split()))
#Identifica si es verdadero o falso
print(VarBool)