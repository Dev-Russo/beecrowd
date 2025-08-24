hora = int(input())
velocidade_media = int(input())

km_total = hora * velocidade_media
total_de_litros = km_total/12

print(f"{total_de_litros:.3f}")