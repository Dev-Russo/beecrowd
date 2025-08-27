number_cases = int(input())
cases = 0
numeros_no_intervalo = []
resultados = []

while cases < number_cases:
    x, y = [int(n) for n in input().split(" ")]
    numeros_no_intervalo = []

    for number in range(min(x,y) + 1, max(x, y)):
        if number%2 != 0:
            numeros_no_intervalo.append(number)
    
    resultados.append(sum(numeros_no_intervalo))
    cases += 1

for resultado in resultados:
    print(f"{resultado}")