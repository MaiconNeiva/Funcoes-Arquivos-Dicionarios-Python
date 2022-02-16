
arquivo = open("emotion_words.txt", "r")

num_words = 0

for linhas in arquivo:
    palavras = linhas.split()
    print(palavras)
    for palavra in palavras:
        num_words += 1

print(num_words)

arquivo.close()
