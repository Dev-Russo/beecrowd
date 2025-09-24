def main():
    valores = list(map(int, input().split()))
    A = valores[0]

    # pega o primeiro N > 0
    N = None
    for v in valores[1:]:
        if v > 0:
            N = v
            break

    # soma A + (A+1) + ... + (A+N-1)
    soma = sum(A + i for i in range(N))
    print(soma)

if __name__ == "__main__":
    main()
