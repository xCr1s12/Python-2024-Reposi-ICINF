#cosita q ocupo
h_Los_rios = 404432 # Los rios
h_Magallanes = 166533 # Magallanes

s_Los_rios = 18429 # Los rios
s_magallanes = 1382291  # Magallanes
#LETRA A
censo_2017= {
    "14" : {
        "nombre_region" : "Los Rios",
        "superficie" : s_Los_rios,
        "habitantes": h_Los_rios,
    },
    "12" : {
        "nombre_region" : "Magallanes",
        "superficie" : s_magallanes,
        "habitantes": h_Magallanes,
    },
}


#LETRA B
#Densidad
densidad_1 = round((h_Los_rios/ s_Los_rios), 1)
densidad_2 = round((h_Magallanes / s_magallanes), 1)

censo_2017["14"].update({"densidad":densidad_1})
censo_2017["12"].update({"densidad":densidad_2})

#Capital y comunas
#LETRA c
censo_2017["14"].update({"capital":"Valdivia"})
censo_2017["12"].update({"capital":"Punta Arenas"})
#Letra D
censo_2017["14"].update({"comunas": ["Río Bueno", "La Unión", "Paillaco"]})
censo_2017["12"].update({"comunas": ["Cabo de Hornos", "Puerto Williams","Porvenir"]})

#Letra E
censo_2017["14"].update({"provincias": ( "Ranco", "Valdivia")})
censo_2017["12"].update({"provincias": ("Antártica Chilena","Magallanes", "Tierra del Fuego", "Última Esperanza")})

#letra F
censo_2017["12"].update({"nombre_region":"Magallanes y Antártica Chilena"})

#Letra G

#Letra Gtuple(zip(claves_14,valores_14))
claves_14 = (censo_2017["14"].keys())
valores_14 = (censo_2017["14"].values())
claves_12 = (censo_2017["12"].keys())
valores_12 = (censo_2017["12"].values())
tupla1 =tuple(zip(claves_14,valores_14))
tupla2 = tuple(zip(claves_12,valores_12))
lista = [tupla1 ,tupla2]
print(lista)






