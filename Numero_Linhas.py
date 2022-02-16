arquivo = open("emotion_words.txt", "r")

num_lines = 0

for linha in arquivo.readlines():
    num_lines += 1
print(num_lines)

arquivo.close()
