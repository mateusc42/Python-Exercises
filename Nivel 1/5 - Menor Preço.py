p1 = input("Digite o 1° preço: ")
p2 = input("Digite o 2° preço: ")
p3 = input("Digite o 3° preço: ")

if p1 < p2 and p1 < p3:
    menor = p1
elif p2 < p1 and p2 < p3:
    menor = p2
else:
    menor = p3
    
print ("O menor preço é:", menor)
