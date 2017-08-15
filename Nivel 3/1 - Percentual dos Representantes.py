cont = 0
while cont <=9:
    p = int(input("Digite a quantidade de pedidos:"))
    if p <= 19:
        print("O percentual de comissão desse representante é 10%")
    elif 20 <= p <= 49:
        print("O percentual de comissão desse representante é 15%")
    elif 50 <= p <= 74:
        print("O percentual de comissão desse representante é 20%")
    elif p >= 75:
        print("O percentual de comissão desse representante é 25%")
    cont += 1
