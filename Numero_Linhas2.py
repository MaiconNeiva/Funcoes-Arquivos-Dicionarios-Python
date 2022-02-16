arquivo = open("school_prompt.txt", "r")

num_lines = 0

for linhas in arquivo:
    print(linhas)
    num_lines += 1
print(num_lines)

arquivo.close()
