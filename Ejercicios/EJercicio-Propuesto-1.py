while True:
    achu = input("Ingresa 150 caracteres")
    if len(achu) >= 150 :
        break

countar = 0
buscar = "a"
for x in achu:
    if x == buscar:
        countar += 1
print(f"ingresaste la letra {buscar} una cantidad de {countar} veces ")