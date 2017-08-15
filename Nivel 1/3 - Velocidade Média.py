distancia= int(input("Digite a distância em km.\n"))
tempo= int(input("Digite o tempo em horas.\n"))

if (distancia/tempo) > 110:
    print("A velocidade média foi superior ao limite!")
else:
    print("Velocidade está dentro do limite")
