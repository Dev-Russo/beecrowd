def getImpares(numero):
    numeros_impares = []
    for i in range(numero+1):
        if i%2 != 0:
            numeros_impares.append(i)
    
    return numeros_impares

def mostrarImpares(lista):
    for num in lista:
        print(num)
        
        
def main():
    num = int(input())
    lista_impares = getImpares(num)
    mostrarImpares(lista_impares)
    
if __name__ == "__main__":
    main()