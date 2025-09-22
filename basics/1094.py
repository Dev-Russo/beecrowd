## receber uma tupla [[10, C], [25, R] ...]
## Olhar a posição da tupla 
## Separar por tipos e somar
def getValues(numero):
    lista = []
    while len(lista) < numero:
        num, cobaia = input().split(" ")
        lista.append([int(num), cobaia])
        
    return lista

def somarCobaias(lista):
    rato = cobra = sapo =0
    for experimento in lista:
        if experimento[1] == "R":
            rato += experimento[0]
        elif experimento[1] == "C":
            cobra += experimento[0]
        elif experimento[1] == "S":
            sapo += experimento[0]
            
    return rato, cobra, sapo

def computarEstatistiacas(r, c, s):
    lista = [r, c, s]
    soma_total = sum(lista)
    porcentagem_rato = r/soma_total * 100
    porcentagem_cobra = c/soma_total * 100
    porcentagem_sapo = s/soma_total * 100
    
    return soma_total, porcentagem_rato, porcentagem_cobra, porcentagem_sapo

def main():
    x = int(input())
    lista_experimentos = getValues(x)
    rato, cobra, sapo = somarCobaias(lista_experimentos)
    soma, pr, pc, ps = computarEstatistiacas(rato, cobra, sapo)
    
    print(f"Total: {soma} cobaias")
    print(f"Total de coelhos: {cobra}")
    print(f"Total de ratos: {rato}")
    print(f"Total de sapos: {sapo}")
    print(f"Percentual de coelhos: {pc:.2f} %")
    print(f"Percentual de ratos: {pr:.2f} %")
    print(f"Percentual de sapos: {ps:.2f} %")
    
    
if __name__ == "__main__":
    main()