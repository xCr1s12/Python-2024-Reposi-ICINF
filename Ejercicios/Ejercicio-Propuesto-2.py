import os

Advinar = int(input("numero a adivinar"))
os.system("cls")

while True:
    Respuesta = int(input(" Ingresa un Numero "))
    if Respuesta == Advinar:
        print(f"Adivinaste si era {Advinar}")
        break
    elif Respuesta < Advinar:
        print("El numero que escogiste es menor a el que tienes que adivinar")
    elif Respuesta > Advinar:
        print("El numero que escogiste es mayor al numero que tienes que adivinar") 