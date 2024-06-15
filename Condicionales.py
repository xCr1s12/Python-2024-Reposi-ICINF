Edad = int(input(" Ingrese una edad"))


if Edad < 0 or Edad >= 120:
    categoria = "Edad no valida"
elif Edad <= 12 and Edad >= 0:
    categoria = "Niño/a"
elif Edad  <= 17 and Edad >= 12:
    categoria = "Adolecente"
elif Edad <= 84 and Edad >= 17:
    categoria = "Adulto"
elif Edad  <= 120 and Edad >= 84:
    categoria = "Adulto Mayor"    
print(f"La persona es {categoria}")

