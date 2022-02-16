arquivo = open("travel_plans.txt", "r")

num = 0

for linhas in arquivo:
    for letra in linhas:
        num += 1

print(num)

arquivo.close()
