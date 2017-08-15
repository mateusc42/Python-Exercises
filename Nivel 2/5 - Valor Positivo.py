cont = 0
while cont <=4:
    n = int(input("Digite um valor positivo:"))
    if n < 0:
        print("Valor Negativo!")
        break
    else:
        cont += 1
    print("Dados Inseridos com Sucesso")
