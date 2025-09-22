matriz = []

numero_linha = int(input())
metodo = input().upper()

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

def resolveMatriz(matriz, linha):
    if metodo == "S":
        return sum(matriz[linha])
    elif metodo == "M":
        return sum(matriz[linha])/12
    
resultado = resolveMatriz(matriz, numero_linha)
print(f"{resultado:.1f}")
    