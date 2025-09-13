def getValues():
    number_list = []
    while len(number_list) < 6:
        numero = float(input())
        number_list.append(numero)
        
    return number_list

def getPositivos(lista):
    positive_list = []
    for number in lista:
        if number >= 0:
            positive_list.append(number)

    return positive_list

def mean(lista):
    qntd = len(lista)
    resultado = sum(lista)/qntd
    return resultado, qntd

def main():
    lista = getValues()
    positiva = getPositivos(lista)
    resultado, qntd = mean(positiva)

    print(f"{qntd} valores positivos")
    print(f"{resultado:.1f}")    
    
if __name__ == "__main__":
    main()