#Texto
span = "La Universidad de los Lagos es una institución estatal fundada en 1993. Esta universidad regional entrega una contribución significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación democrática."


#Manejar el texto
texto = span.lower()
Buscar = "universidad"
txt = span.split()
txt_min = texto.split()
a = txt_min.count("universidad")

#Buscar y guardar
lista = []

for text1, text2 in zip(txt, txt_min):
    if text2 == Buscar:
        lista.append(text1)

tupla = tuple(lista)
print("La palabra Buscada se repite: ",a)
print(tupla)