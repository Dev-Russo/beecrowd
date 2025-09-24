valores = []
while True:
    valor = int(input())
    if valor >= 0:
        valores.append(valor)
    else:
        break
    
media = sum(valores)/len(valores)
print(f"{media:.2f}")