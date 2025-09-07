def reajuste_salarial(salario):
    if (salario >= 0 and salario <= 400 ):
        reajuste = 0.15
    elif(salario > 400 and salario <= 800):
        reajuste = 0.12
    elif(salario > 800 and salario <= 1200):
        reajuste = 0.10
    elif(salario > 1200 and salario <= 2000):
        reajuste = 0.07
    elif salario > 2000:
        reajuste = 0.04

    novo_salario = salario * (1 + reajuste)
    
    return novo_salario, reajuste

def main():
    salario_atual = float(input())
    novo_salario, porcentagem = reajuste_salarial(salario_atual)

    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {novo_salario - salario_atual:.2f}")
    print(f"Em percentual: {int(porcentagem * 100)} %")

if __name__ == "__main__":
    main()
