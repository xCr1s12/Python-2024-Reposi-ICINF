Temperaturas_Mínimas = {9, 5, 2, 7, 6, 1}
Temperaturas_Máximas = {12, 14, 11, 10, 15, 9}


#Letra A)
buscar = 9
if buscar in Temperaturas_Máximas and 9 in Temperaturas_Mínimas:
    print(f"La temperatura {buscar}°C si esta en ambos conjuntos ")
else:
    print(f"La temperatura {buscar}°C no esta en ambos conjuntos")

#Letra B) 
Temperaturas = list(Temperaturas_Máximas) + list(Temperaturas_Mínimas)
Temperaturas_set = set(Temperaturas)
print(Temperaturas_set)

#Letra C)
Temperaturas = list(Temperaturas)
Maxima = 0
minima = 100000000000
for x in Temperaturas:
    if x < minima:
        minima = x

    if x > Maxima:
        Maxima = x

print(f" EL valor Maximo es {Maxima}")
print(f" El Valor Minimo es {minima}")


#Letra D)

Claves = "Maxima: ", "Minima:"
Valores = Maxima , minima

new_tupla = tuple(zip(Claves,Valores))
print(new_tupla)

#Letra E)


dic_Temperaturas= {
    "1": 1,
    "2": 1,
    "5": 1,
    "6": 1,
    "7": 1,
    "9": 2,
    "10": 1,
    "11": 1,
    "12": 1,
    "14": 1,
    "15": 1
 
}

print(dic_Temperaturas.items())


