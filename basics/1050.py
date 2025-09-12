def getValue():
    x = int(input())
    return x

def getCityByDDD(DDD):
    if DDD == 61:
        return "Brasilia"
    elif DDD == 71:
        return "Salvador"
    elif DDD == 11:
        return "Sao Paulo"
    elif DDD == 21:
        return "Rio de Janeiro"
    elif DDD == 32:
        return "Juiz de Fora"
    elif DDD == 19:
        return "Campinas"
    elif DDD == 27:
        return "Vitoria"
    elif DDD == 31:
        return "Belo Horizonte"
    else:
        return "DDD nao cadastrado"
    
def main():
    ddd = getValue()
    print(getCityByDDD(ddd))
    
if __name__ == "__main__":
    main()