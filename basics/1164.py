cases = int(input())
count = 0

while count < cases:
    valor = int(input())
    divisible = []
    
    for i in range(1, valor):
        if valor%i == 0:
            divisible.append(i)
            
    check_number = sum(divisible)
    if check_number == valor:
        print(f"{valor} eh perfeito")
    else:
        print(f"{valor} nao eh perfeito")
        
    count += 1