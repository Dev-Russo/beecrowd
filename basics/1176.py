def fibonnachi(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnachi(n - 1) + fibonnachi(n - 2)
    
count = 0
cases = int(input())

while count < cases:
    valor = int(input())
    
    resultado = fibonnachi(valor)
    print(f"Fib({valor}) = {resultado}")

    count += 1