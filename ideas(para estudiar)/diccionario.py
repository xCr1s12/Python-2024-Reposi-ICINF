def div(X):
    return X//2
Comida= dict(
    Papas = 12,
    Dulces = 14,
    otro  = 0,
)
print(Comida)
comidas = input("Ingresa una Comida")
cantidad = int(input("Ingresa una cantidad"))
Comida.update({"otro" :cantidad})
print(Comida)
Comida[comidas] = Comida.pop("otro")
print(Comida)
pasd = list(map(str,Comida.values()))
pips = list(map(int,Comida.values()))
peps = list(map(div,Comida.values()))
print(pasd)
print(pips)
print(peps)