# Cria o arquivo e grava 3 frases usando o modo 'w' (write - sobrescreve o arquivo)
with open("minhas_notas.txt", "w") as arquivo:
    arquivo.write("Primeira frase: aprendendo Python na Escola da Nuvem.\n")
    arquivo.write("Segunda frase: praticando com arquivos.\n")
    arquivo.write("Terceira frase: usando o modo write.\n")

# Adiciona 2 frases novas usando o modo 'a' (append - acrescenta no final)
with open("minhas_notas.txt", "a") as arquivo:
    arquivo.write("Quarta frase: agora usando o modo append.\n")
    arquivo.write("Quinta frase: continuando a prática.\n")

# Lê e imprime o conteúdo do arquivo
with open("minhas_notas.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)