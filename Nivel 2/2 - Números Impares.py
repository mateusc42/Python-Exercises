data = ""

while True:
    num = int(input("Digite a idade:"))
    if num == 99:
        break
    else:
        if num % 2 == 0:
            continue
        else:
            data = data + str(num) + "\n"

print(data)


