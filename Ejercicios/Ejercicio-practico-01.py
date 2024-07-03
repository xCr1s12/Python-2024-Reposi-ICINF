def repetidos(lista):
    repetidodos = {}
    lata = []
    for numero in lista:
        if numero in repetidodos:
            repetidodos[numero] += 1
        else:
            repetidodos[numero] = 0
    
    for x , k in repetidodos.items():
        if k > 0 :
            lata.append(x)
    return lata

Alturas_en_Zona_Central = (8848, 8611, 8586, 8200, 8460, 8200)
Alturas_en_Zona_Sur = (8848, 5567, 8125, 4560, 8051, 4560)
Alturas_en_Zona_Austral = (2200, 2500, 1000, 2200, 3623, 990)

A_Z_C_lista = list(Alturas_en_Zona_Central)
A_Z_S_lista = list(Alturas_en_Zona_Sur)
A_Z_A_lista = list(Alturas_en_Zona_Austral)

A_c_set = set(A_Z_C_lista)
A_S_set = set(A_Z_S_lista)
A_a_set = set(A_Z_A_lista)


print("Las Alturas repetidas en la zona central son ",repetidos(A_Z_C_lista))
print("Las Alturas repetidas en la zona Sur son ",repetidos(A_Z_S_lista))
print("Las Alturas repetidas en la zona Austral son ",repetidos(A_Z_A_lista))

Buscar = 8848
verificar = 0
for x in range(1):
    for x in A_c_set:
        if x == Buscar:
            verificar +=1

    for x in A_S_set:
        if x == Buscar:
            verificar +=1

    for x in A_a_set:
        if x == Buscar:
            verificar +=1

    if verificar == 3:
        print("La Altura Buscada esta en las 3 Zonas (tuplas)")
    else :
        print("La Altura no esta en las 3 zonas (tuplas)")

lista_tuplas = A_Z_C_lista + A_Z_S_lista + A_Z_A_lista

print(lista_tuplas)

set_sin_dupli = set(lista_tuplas)

tupla = tuple(set_sin_dupli)
print(tupla)

lista_final = list(tupla)
print(lista_final)
