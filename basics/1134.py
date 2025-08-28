def verifica_votos(todos_os_votos):
    alcool = disel = gasolina = 0    
    for i in range(len(todos_os_votos)):
        if todos_os_votos[i] == 1:
            alcool += 1
        elif todos_os_votos[i] == 2:
            gasolina += 1
        elif todos_os_votos[i] == 3:
            disel += 1
    return alcool, gasolina, disel

def imprimir(a, b, c):
    print("MUITO OBRIGADO")
    print(f"Alcool: {a}")
    print(f"Gasolina: {b}")
    print(f"Diesel: {c}")

def main():
    lista_voto = []
    while True:
        voto = int(input())
        if 1 <= voto <= 3:
            lista_voto.append(voto)
        elif voto == 4:    
            alcool, gasolina, disel = verifica_votos(lista_voto)
            break
    imprimir(alcool, gasolina, disel)

if __name__ == "__main__":
    main()

