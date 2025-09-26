def main():
    par = []
    impar = []

    for _ in range(15):
        valor = int(input())

        if valor % 2 == 0:
            par.append(valor)
            if len(par) == 5:
                for i, v in enumerate(par):
                    print(f"par[{i}] = {v}")
                par.clear()
        else:
            impar.append(valor)
            if len(impar) == 5:
                for i, v in enumerate(impar):
                    print(f"impar[{i}] = {v}")
                impar.clear()

    for i, v in enumerate(impar):
        print(f"impar[{i}] = {v}")
    for i, v in enumerate(par):
        print(f"par[{i}] = {v}")


if __name__ == "__main__":
    main()
