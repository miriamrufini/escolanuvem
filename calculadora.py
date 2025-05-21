# Calculadora (4 operaçoes)


# Função para somar dois números
def somar(a, b):
    return a + b


# Função para subtrair dois números
def subtrair(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicar(a, b):
    return a * b

# Função para dividir dois números
def dividir(a, b):
    # Verifica se o segundo número é zero para evitar erro
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b

# Exibe o menu de operações
print("Calculadora Básica")
print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Entrada do usuário para escolher a operação
operacao = input("Digite o número da operação desejada (1/2/3/4): ")

# Entrada dos dois números que o usuário deseja calcular
# Usamos float para aceitar números decimais também
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Estrutura condicional para realizar a operação escolhida
if operacao == "1":
    resultado = somar(numero1, numero2)
    print("Resultado da soma:", resultado)
elif operacao == "2":
    resultado = subtrair(numero1, numero2)
    print("Resultado da subtração:", resultado)
elif operacao == "3":
    resultado = multiplicar(numero1, numero2)
    print("Resultado da multiplicação:", resultado)
elif operacao == "4":
    resultado = dividir(numero1, numero2)
    print("Resultado da divisão:", resultado)
else:
    # Mensagem de erro para operação inválida
    print("Operação inválida. Por favor, escolha 1, 2, 3 ou 4.")
