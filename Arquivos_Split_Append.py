arquivo = open("school_prompt.txt", "r")

p_words = []

for linhas in arquivo:
    palavras = linhas.split()

    for palavra in palavras:
        if "p" in palavra:
            p_words.append(palavra)

print(p_words)

arquivo.close()
