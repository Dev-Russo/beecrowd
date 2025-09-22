# 1. Leitura dos 100 valores de forma concisa usando List Comprehension
vetor = [float(input()) for _ in range(100)]

# 2. Itera sobre o vetor para verificar e imprimir
# Esta parte do seu código já é a melhor forma de fazer.
for index, numero in enumerate(vetor):
    if numero <= 10:
        print(f"A[{index}] = {numero:.1f}")