data = 0

while True:
    idade = int(input("Digite a idade:"))
    altura = float(input("Digite a altura:"))
    if altura == 0:
        break
    else:
        if idade > 13:
            if altura < 1.5:
                data = data + 1

print ("\nTotal de Alunos: %d" %	(data))
