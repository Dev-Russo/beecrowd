number = int(input())

vetor = [int(x) for x in input().split()]

menor_valor = min(vetor)
posicao = vetor.index(menor_valor)

print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")