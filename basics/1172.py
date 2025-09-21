def getValues():
    lista = []
    for _ in range(10):
        lista.append(int(input()))
    
    return lista

def returnvalues(lista):
    for index, number in enumerate(lista):
        if number <= 0:
            lista[index] = 1
        print(f"X[{index}] = {lista[index]}")


def main():
    lista = getValues()
    returnvalues(lista)

if __name__ == "__main__":
    main()