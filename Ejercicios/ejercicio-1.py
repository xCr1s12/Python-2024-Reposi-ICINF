#Notas de Joel
jn1 = float(input("Ingrese tu primera nota joel "))
jn2 = float(input("Ingrese tu segunda nota joel "))
jn3 = float(input("Ingrese tu tercera nota joel "))

#Notas De Alondra
an1 = float(input("Ingrese tu primera nota Alondra "))
an2 = float(input("Ingrese tu segunda nota Alondra "))
an3 = float(input("Ingrese tu tercera nota Alondra "))
#Notas de Paz
pn1 = float(input("Ingresa tu primera nota Paz "))
pn2 = float(input("Ingresa tu segunda nota Paz "))
pn3 = float(input("Ingresa tu tercera nota Paz "))

#Promedios
pp = (pn1 + pn2 + pn3)/3
Jp = (jn1 + jn2 + jn3)/3
ap = (an1 + an2 + an3)/3

print("Joel tu nota es {:.3f}".format(Jp))
print("tu nota mas baja es ",min(jn1,jn2,jn3))

print("Alondra tu nota es {:.3f}".format(ap))
print("tu nota mas baja es ",min(an1,an2,an3))

print("Paz tu nota es {:.3f}".format(pp))
print("tu nota mas baja es ",min(pn1,pn2,pn3))


pf= (pp + Jp + ap)/3
print("el promedio final de los 3 estudiantes es {:.3f}".format(pf))


