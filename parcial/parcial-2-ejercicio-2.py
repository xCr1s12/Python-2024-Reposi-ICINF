palabra = input("Ingrese una palabra para verificar si es un palindromo:").lower()
palabra = palabra.strip
palabras = " "
for x in palabra[::-1]:
    palabras += x
nueva_Palabra = palabras.strip()
print(nueva_Palabra)
if palabra== nueva_Palabra:
    print("es un palindromo ")
else: 
    print("No es un palindromo")