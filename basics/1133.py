def divByFive(numero1, numero2):
    numeros_validos = []
    for i in range (min(numero1, numero2) + 1, max(numero2, numero1)):
        if i%5 == 2 or i%5 == 3:
            numeros_validos.append(i)
        
    return numeros_validos

def printValues(allnumber):
    for i in allnumber: print(i)
    
def main():
    x = int(input())
    y = int(input())
    
    all_numebers = divByFive(x, y)
    
    printValues(all_numebers)
    
if __name__ == "__main__":
    main()