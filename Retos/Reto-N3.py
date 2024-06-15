#Listas con ciudad y INDICE DE CALIDAD DE AIRE
ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
I_C_A = [134, 99 , 245 , 50]

#Diccionario con Categoria (Mouskeherramienta Misteriosa)
Categoria={
    "I.C.A_minima" : "",
    "I.C.A_maxima" : "", 
}
#Valores minimos y maximos
Min_ICA = min(I_C_A)
max_ICA = max(I_C_A)

#Indice de el lugar
min_Ciudad_ICA= ciudades[I_C_A.index(Min_ICA)]
max_Ciudad_ICA= ciudades[I_C_A.index(max_ICA)]

#Printeo el nombre de cada una
print("LA ciudad con el indice mas bajo es ",min_Ciudad_ICA)
print("La ciudad con el indice mas alto es ",max_Ciudad_ICA)

#Reconoce y lo categoriza


#Para el indice minimo
if Min_ICA >= 0 and Min_ICA <= 50:
    print(f" La calidad de aire de {min_Ciudad_ICA} es Buena")
    Categoria.update({"I.C.A_minima": "Buena"})
elif Min_ICA >= 51 and Min_ICA <= 100:
    print(f" La calidad de aire de {min_Ciudad_ICA} es Moderada")
    Categoria.update({"I.C.A_minima": "Moderada"})
elif Min_ICA >= 101 and Min_ICA <= 150:
    print(f" La calidad de aire de {min_Ciudad_ICA} es Dañina para algunos grupos sensibles")
    Categoria.update({"I.C.A_minima": "Dañina(Grupos sensibles)"})
elif Min_ICA >= 151 and Min_ICA <= 200:
    print(f" La calidad de aire de {min_Ciudad_ICA} es Dañina a la salud")
    Categoria.update({"I.C.A_minima": "Dañina a la salud)"})
elif Min_ICA >= 201 and Min_ICA <= 300:
    print(f" La calidad de aire de {min_Ciudad_ICA} es Muy Dañina para la salud")
    Categoria.update({"I.C.A_minima": "Muy Dañina a la salud)"})
else:
    print(f"la calidad del aire de {min_Ciudad_ICA} es peligrosa")
    Categoria.update({"I.C.A_minima": "Peligrosa"})

#para el indice maximo
if max_ICA >= 0 and max_ICA <= 50:
    print(f" La calidad de aire de {max_Ciudad_ICA} es Buena")
    Categoria.update({"I.C.A_maxima": "Buena"})
elif max_ICA >= 51 and max_ICA <= 100:
    print(f" La calidad de aire de {max_Ciudad_ICA} es Moderada")
    Categoria.update({"I.C.A_maxima": "Moderada"})
elif max_ICA >= 101 and max_ICA <= 150:
    print(f" La calidad de aire de {max_Ciudad_ICA} es Dañina para algunos grupos sensibles")
    Categoria.update({"I.C.A_maxima": "Dañina(Grupos sensibles)"})
elif max_ICA >= 151 and max_ICA <= 200:
    print(f" La calidad de aire de {max_Ciudad_ICA} es Dañina a la salud")
    Categoria.update({"I.C.A_maxima": "Dañina a la salud)"})
elif max_ICA >= 201 and max_ICA <= 300:
    print(f" La calidad de aire de {max_Ciudad_ICA} es Muy Dañina para la salud")
    Categoria.update({"I.C.A_maxima": "Muy Dañina a la salud"})
else:
    print(f"la calidad del aire de {max_Ciudad_ICA} es peligrosa")
    Categoria.update({"I.C.A_maxima": "Peligrosa"})

#Para ver la categoria de cada I.C.A
print(Categoria.items())