vetor = [float(input()) for _ in range(100)]

for index, numero in enumerate(vetor):
    if numero <= 10:
        print(f"A[{index}] = {numero:.1f}")