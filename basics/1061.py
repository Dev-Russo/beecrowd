def convert_to_seconds(dia, hora, minuto, segundo):
    return (24 * 60 * 60) * dia + 3600 * hora + 60 * minuto + segundo

def get_values():
    dia = int(input().split(" ")[1])
    horas, minutos, segundos = [int(x) for x in input().split(" : ")]
    
    return dia, horas, minutos, segundos

def return_values(segundos_iniciais, segundos_finais):
    duracao = segundos_finais - segundos_iniciais
    
    dias = int(duracao/86400)
    sobra_dias = duracao%86400
    
    horas = int(sobra_dias/3600)
    sobra_horas = sobra_dias%3600
    
    minutos = int(sobra_horas/60)
    sobra_minutos = sobra_horas%60
    
    segundos = int(sobra_minutos)

    return dias, horas, minutos, segundos

def print_values(dias, horas, minutos, segundos):
    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")

def main():
    di, hi, mi, si = get_values()
    df, hf, mf, sf = get_values()
    
    sti = convert_to_seconds(di, hi, mi, si)
    stf = convert_to_seconds(df, hf, mf, sf)
    
    dp, hp, mp, sp = return_values(sti, stf)
    print_values(dp, hp, mp, sp)
    

if __name__ == "__main__":
    main()
    
    