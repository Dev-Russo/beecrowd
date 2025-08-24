n1, n2, n3, n4 = [float(x) for x in input().split(" ")]

media1 = (n1 *2  + n2 * 3 + n3 * 4 + n4 * 1) / 10

print(f"Media: {media1:.1f}")

if(media1 >= 7):
    print(f"Aluno aprovado.")
elif(media1 < 5):
    print(f"Aluno reprovado.")
else:
    print(f"Aluno em exame.")

    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    
    media1 = (nota_exame + media1) / 2
    
    if(media1 >= 5):
        print(f"Aluno aprovado.")
    else:
        print(f"Aluno reprovado")

    print(f"Media final: {media1:.1f}")