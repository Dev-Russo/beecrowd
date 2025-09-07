def calcular_duracao_jogo(h_ini, m_ini, h_fim, m_fim):
    MINUTOS_EM_UM_DIA = 24 * 60

    tempo_inicial_total = h_ini * 60 + m_ini
    tempo_final_total = h_fim * 60 + m_fim

    duracao_minutos = tempo_final_total - tempo_inicial_total

    if duracao_minutos <= 0:
        duracao_minutos += MINUTOS_EM_UM_DIA

    horas = duracao_minutos // 60
    minutos = duracao_minutos % 60
    
    return horas, minutos

def main():
    h_ini, m_ini, h_fim, m_fim = map(int, input().split())
    
    horas_duracao, minutos_duracao = calcular_duracao_jogo(h_ini, m_ini, h_fim, m_fim)
    
    print(f"O JOGO DUROU {horas_duracao} HORA(S) E {minutos_duracao} MINUTO(S)")

if __name__ == "__main__":
    main()