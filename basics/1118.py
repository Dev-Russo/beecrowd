NOTA_INVALIDA = "nota invalida"

def validar_nota():
    while True:
        try:
            nota = float(input())
            if 0 <= nota <= 10:
                return nota
            else:
                print(NOTA_INVALIDA)
        except ValueError:
            print(NOTA_INVALIDA) 

def calcular_media():
    nota1 = validar_nota()
    nota2 = validar_nota()
    
    return (nota1 + nota2) / 2

def obter_opcao_valida(prompt, opcoes_validas):
    while True:
        try:
            print(prompt)
            escolha = int(input())
            if escolha in opcoes_validas:
                return escolha
        except ValueError:
            pass

def main():
    while True:
        media = calcular_media()
        print(f"media = {media:.2f}") 
        
        escolha = obter_opcao_valida("novo calculo (1-sim 2-nao)", [1, 2])
        
        if escolha == 2:
            break

if __name__ == "__main__":
    main()