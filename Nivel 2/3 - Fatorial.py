n = int(input("Digite um número menor ou igual a 20:"))

cont=1  
n_fat = 1

while cont <= n:
    n_fat = n_fat * cont
    cont = cont + 1

print("%d! = %d" %(n, n_fat)) 
