def fatorial(numero):
    if numero > 1:
        return fatorial(numero - 1) * numero
    else: return 1
   

def main():
    valor = int(input())
    resultado = fatorial(valor)
    print(resultado)

if __name__ == "__main__":
    main()