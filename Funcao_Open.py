arquivo = open("school_prompt2.txt", "r")

contador = 0

for palavra in arquivo:
    for letra in palavra:
        contador += 1

num_char = contador
print(num_char)

arquivo.close()
