def nao_multiplos_no_intervalo(intervalo1, intervalo2, numero_multiplo):
    lista_de_num_nao_multiplos = []
    for i in range(min(intervalo1, intervalo2), max(intervalo1, intervalo2) + 1):
        if i%numero_multiplo != 0:
            lista_de_num_nao_multiplos.append(i)
    return lista_de_num_nao_multiplos

def main():
    inicio = int(input())
    fim = int(input())

    todos_os_valores = nao_multiplos_no_intervalo(inicio, fim, 13)
    print(sum(todos_os_valores))

if __name__ == "__main__":
    main()