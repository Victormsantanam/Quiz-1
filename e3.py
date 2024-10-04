import random

palabras = ["python", "astronauta", "melodia", "horizonte",
"quimera", "chocolate", "galaxia", "oportuno",
"pradera", "zigzag"]

palabra_seleccionada = random.choice(palabras)
print(palabra_seleccionada)
intentos = 3
pantallaInicial = ""

for x in palabra_seleccionada:
    pantallaInicial += "_"

print(f"\nIntentos: {intentos}\nPantalla inicial: {pantallaInicial}")

respuesta = input("Ingrese una letra o la palabra: ").lower()

if len(respuesta) == 1 and respuesta in palabra_seleccionada:
    aux = ""
    for i in range(len(palabra_seleccionada)):
        if palabra_seleccionada[i] == respuesta:
            aux += respuesta
        elif palabra_seleccionada[i] == pantallaInicial[i]:
            aux += palabra_seleccionada[i]
        else:
            aux += "_"
    pantallaInicial = aux

elif len(respuesta) > 1:
    if palabra_seleccionada == respuesta:
        print(f"\nHas ganado! Acertaste la palabra '{palabra_seleccionada}'!")
        exit()
    else:
        intentos -=1

elif respuesta not in palabra_seleccionada:
    intentos -=1

while intentos > 0 and random.choice(palabras) != respuesta:
    print(f"\nIntentos: {intentos}\nPantalla: {pantallaInicial}")
    respuesta = input("Ingrese una letra o la palabra: ").lower()

    if len(respuesta) == 1 and respuesta in palabra_seleccionada:
        aux = ""
        for i in range(len(palabra_seleccionada)):
            if palabra_seleccionada[i] == respuesta:
                aux += respuesta
            elif palabra_seleccionada[i] == pantallaInicial[i]:
                aux += palabra_seleccionada[i]
            else:
                aux += "_"
        pantallaInicial = aux
    
        if palabra_seleccionada == pantallaInicial:
            print(f"\nHas ganado! Acertaste la palabra '{palabra_seleccionada}'!")
            break

    elif len(respuesta) > 1:
        if palabra_seleccionada == respuesta:
            print(f"\nHas ganado! Acertaste la palabra '{palabra_seleccionada}'!")
            break
        else:
            intentos -=1
        
    elif respuesta not in palabra_seleccionada:
        intentos -=1

if intentos == 0:
    print("\nFin del juego! Te has quedado sin intentos.")