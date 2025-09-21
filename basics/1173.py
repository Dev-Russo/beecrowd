def preenchevector(number):
    vetor = []
    for i in range(10):
        vetor.append(number)
        number *= 2
        print(f"X[{i}] = {vetor[i]}")

def main():
    numero = int(input())
    preenchevector(numero)

if __name__ == "__main__":
    main()