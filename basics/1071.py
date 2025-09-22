def getImpares(ini, fim):
    numeros_impares = []
    for i in range(min(ini, fim)+1, max(ini, fim)):
        if i%2 != 0:
            numeros_impares.append(i)
    
    return numeros_impares

def soma(lista):
    return sum(lista)
        
        
def main():
    num = int(input())
    fim = int(input())
    lista_impares = getImpares(num, fim)
    print(soma(lista_impares))
    
if __name__ == "__main__":
    main()