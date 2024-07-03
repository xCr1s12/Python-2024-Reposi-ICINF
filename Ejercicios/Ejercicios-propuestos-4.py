Cadena = input("Ingrese un texto cual sea: ").lower()

letras = {"a": 0,"e": 0,"i": 0,"o": 0,"u": 0}

Buscar= ["a","e","i","o","u"]
for x in Cadena:
    if x == Buscar[0]:
        letras["a"] += 1
    elif x == Buscar[1]:
        letras["e"] += 1
    elif x == Buscar[2]:
        letras["i"] += 1
    elif x == Buscar[3]:
        letras["o"] += 1
    elif x == Buscar[4]:
        letras["u"] += 1
print(f"La letra 'a' se repitio  {letras["a"]}")
print(f"La letra 'e' se repitio  {letras["e"]}")
print(f"La letra 'i' se repitio  {letras["i"]}")
print(f"La letra 'o' se repitio  {letras["o"]}")
print(f"La letra 'u' se repitio  {letras["u"]}")
