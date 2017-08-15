numero = 2
p = 0
print ("Primos: "),
while numero < 16:
    i = numero -1
    while i > 1:
        if numero % i == 0:
            break
        i -= 1
    else:
        print (numero),
        p += 1
    numero += 1

print ("\n\nForam encontrados %d números primos." %p)
