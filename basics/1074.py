def getValues(numero):
    listanumeros = []
    while len(listanumeros) < numero:
        x = int(input())
        listanumeros.append(x)
        
    return listanumeros

def imparParPositivoNegativo(listanumeros):
    for numero in listanumeros:
        string = ""
        if numero == 0:
            string = "NULL"
        elif numero%2 == 0:
            string = "EVEN"
        else:
            string = "ODD"
        if numero > 0:
             string += " POSITIVE"
        elif numero < 0:
            string += " NEGATIVE"
            
        print(string)
        
def main():
    x = int(input())
    lista = getValues(x)
    
    imparParPositivoNegativo(lista)
    
if __name__ == "__main__":
    main()