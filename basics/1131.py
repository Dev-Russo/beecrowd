MSG_VITORIA_INTER = "Inter venceu mais"
MSG_VITORIA_GREMIO = "Gremio venceu mais"
MSG_EMPATE = "Nao houve vencedor"

def computar_estatisticas(jogos):
    vitorias_inter = vitorias_gremio = empates = 0
    for placar in jogos:
        gols_inter, gols_gremio = placar[0], placar[1]
        if gols_inter > gols_gremio:
            vitorias_inter += 1
        elif gols_gremio > gols_inter:
            vitorias_gremio += 1
        else:
            empates += 1
    return vitorias_inter, vitorias_gremio, empates

def determinar_vencedor_geral(vitorias_inter, vitorias_gremio):
    if vitorias_inter > vitorias_gremio:
        return MSG_VITORIA_INTER
    elif vitorias_gremio > vitorias_inter:
        return MSG_VITORIA_GREMIO
    else:
        return MSG_EMPATE

def imprimir_resultado_final(total_jogos, v_inter, v_gremio, empates):
    print(f"{total_jogos} grenais")
    print(f"Inter:{v_inter}")
    print(f"Gremio:{v_gremio}")
    print(f"Empates:{empates}")
    
    vencedor_geral = determinar_vencedor_geral(v_inter, v_gremio)
    print(vencedor_geral)

def main():
    todos_os_jogos = []

    while True:
        gols_inter, gols_gremio = map(int, input().split())
        todos_os_jogos.append([gols_inter, gols_gremio]) 

        print("Novo grenal (1-sim 2-nao)")
        opcao = int(input())
        if opcao == 2:
            break
            
    v_inter, v_gremio, empates = computar_estatisticas(todos_os_jogos)
    imprimir_resultado_final(len(todos_os_jogos), v_inter, v_gremio, empates)

if __name__ == "__main__":
    main()