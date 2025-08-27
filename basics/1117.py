NOTA_INVALIDA = "nota invalida"

def verifica_valido(number):
    return 0 <= number <= 10

def mean(lista_validos):
    return sum(lista_validos)/len(lista_validos)

def main():
    lista_notas = []
    while len(lista_notas) < 2:
        numero = float(input())
        if verifica_valido(numero):
            lista_notas.append(numero)
            qnt_valido += 1
        else:
            print(NOTA_INVALIDA)

    resultado = mean(lista_notas)
    print(f"media = {resultado:.2f}")

if __name__ == "__main__":
    main()