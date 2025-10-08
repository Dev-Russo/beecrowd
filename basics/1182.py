matriz = []

numero_coluna = int(input())
metodo = input().upper()

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

def resolveMatriz(matriz, coluna):
    column = [row[coluna] for row in matriz]
    if metodo == "S":
        return sum(column)
    elif metodo == "M":
        return sum(column)/12

resultado = resolveMatriz(matriz, numero_coluna)
print(f"{resultado:.1f}")
    