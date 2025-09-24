while True:
    valor = int(input())
    soma = 0
    
    if valor == 0:
        break
    
    for i in range(5):
        if valor % 2 == 0:
            soma += valor
            valor += 2
        else:
            valor += 1
            soma += valor
            valor += 2
    print(soma)