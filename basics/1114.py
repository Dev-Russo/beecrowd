SENHA_CORRETA = "2002"
MENSAGEM_SUCESSO = "Acesso Permitido"
MENSAGEM_ERRO = "Senha invalida"

def verifica_senha(senha):
    return senha == SENHA_CORRETA

def main():
    while True:
        senha = input()
        if verifica_senha(senha):
            print(MENSAGEM_SUCESSO)
            break
        else:
            print(MENSAGEM_ERRO)

if __name__ == "__main__":
    main()