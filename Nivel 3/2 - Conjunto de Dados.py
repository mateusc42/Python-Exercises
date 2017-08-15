maior_altura = 0
menor_altura = 0
media_alturasM = 0
num_homens = 0
num_mulheres = 0
sexo_alta = ""

cont = 0
while cont <=5:
    sexo = input("Qual o seu sexo(M ou F)?:")
    while True:
        if sexo=="M" or sexo=="F":
            break
        else:
            sexo = input("Sexo Invalido! Digite Novamente(M ou F):")
    altura = float(input("Digite sua altura:"))
    if altura > maior_altura:
        maior_altura = altura
        sexo_alta = sexo
    elif altura < menor_altura:
        menor_altura = altura
    elif sexo == "M":
        num_homens += 1
    elif sexo == "F":
        num_mulheres += 1
        media_alturasM = media_alturasM + altura
    cont += 1

print(" A maior altura é: %f" % maior_altura)
print("A menor altura é: %f" % menor_altura)
print("A média de altura das mulheres é: %.2f" % (media_alturasM/num_mulheres))
print("O número de Homens é: %i" % num_homens)
print("O número de Mulheres é: %i" % num_mulheres)
print("O sexo da pessoa mais alta é: %s" % sexo_alta)

