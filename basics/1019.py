N = int(input())

sobra_horas = N%3600
sobra_minutos = sobra_horas%60
segundo = sobra_minutos

print(f"{N//3600}:{sobra_horas//60}:{segundo}")