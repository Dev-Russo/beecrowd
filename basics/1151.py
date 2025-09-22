sequencia = int(input())

def fibonnaci(numero):
    if numero <= 1:
        return numero
    else:
        return fibonnaci(numero - 1) + fibonnaci(numero - 2)
    
print(fibonnaci(sequencia))