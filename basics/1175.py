vetor = []
for _ in range(20):
    vetor.append(int(input()))

vetor.reverse()
for index, number in enumerate(vetor):
    print(f"N[{index}] = {vetor[index]}")
