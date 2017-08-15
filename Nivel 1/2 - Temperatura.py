temp = int(input("Digite a temperatuda\n"))

if temp >= 39:
    print ("Febre Alta")
elif 39 > temp >= 37:
    print ("Febril")
elif temp < 37:
    print ("Sem Febre")
