def getValues():
    lista_numeros = []
    for _ in range(5):
        numero = int(input())
        lista_numeros.append(numero)
        
    return lista_numeros

def maxAndPosition(numeros):
    max_value = max(numeros)
    number_index = numeros.index(max_value)
    
    return max_value, number_index

def main():
    lista = getValues()
    maior, nindex = maxAndPosition(lista)
    
    print(f"{maior}\n{nindex + 1}")
    
if __name__ == "__main__":
    main()