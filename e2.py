matriz = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

cont = 0
respuesta = ''

while cont < len(matriz[0]):
    col = 0

    for x in matriz:
        col += x[cont]
    respuesta += F"Columna {cont + 1}: {str(col)}"
    cont += 1

    if cont < len(matriz[0]):
        respuesta += ", "

print(respuesta)