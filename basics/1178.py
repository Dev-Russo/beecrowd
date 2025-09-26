primeiro = float(input())

vetor = []
vetor.append(primeiro)

print(f"N[{0}] = {vetor[0]:.4f}")
for i in range(1, 100):
    valor = vetor[i-1]/2
    vetor.append(valor)
    print(f"N[{i}] = {valor:.4f}")