def quadrante(x, y):
    if x > 0 and y > 0:
        return "primeiro"
    elif x < 0 and y > 0:
        return "segundo"
    elif x < 0 and y < 0:
        return "terceiro"
    else:
        return "quarto"

def main():
    while True:
        x, y = [int(n) for n in input().split(" ")]
        if x == 0 or y == 0:
            break
        else:
            resultado = quadrante(x, y)
            print(resultado)

if __name__ == "__main__":
    main()