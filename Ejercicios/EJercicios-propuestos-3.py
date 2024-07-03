def duplicate(lista):
    contar = {}
    duplicados = []

    for num in lista:
        if num in contar:
            contar[num] += 1
        else:
            contar[num] = 1
    
    for num, cuenta in contar.items():
        if cuenta > 1:
            duplicados.append(num)
    
    return duplicados

def patata():
    print("Hola")

patata()

Puntajes_Matemáticas = (55, 17, 93, 75, 88, 55)
Puntajes_Química = (10, 85, 75, 88, 91, 75)
Puntajes_Programación = (68, 78, 85, 68, 82, 10)
        

duplicado_Mate = sorted(Puntajes_Matemáticas)
duplicado_Quimica = sorted(Puntajes_Química)
duplicado_progra = sorted(Puntajes_Programación)

print("El puntaje duplicado en Matematicas es ",duplicate(duplicado_Mate))
print("El puntaje duplicado en Quimica es ",duplicate(duplicado_Quimica))
print("El puntaje duplicado en Programacion es ",duplicate(duplicado_progra))

print("La primera tupla ordenada en una lista (Matematicas) es ", duplicado_Mate)
print("La primera tupla ordenada en una lista (Quimica) es ", duplicado_Quimica)
print("La primera tupla ordenada en una lista (Programacion) es ", duplicado_progra)

lista_con_dupli = duplicado_Mate + duplicado_progra + duplicado_Quimica
Remover_duplicados = set(lista_con_dupli)
lista_sin_dupli = sorted(list(Remover_duplicados))
print("Combinacion de las tuplas en listas ",lista_sin_dupli)

print(f"El puntaje mas alto es {max(lista_sin_dupli)} y el mas bajo es {min(lista_sin_dupli)}")

