def registrar_notas():
    notas = []

    print("=== Registro de Notas da Turma ===")
    print("Digite as notas de 0 a 10. Para encerrar, digite 'fim'.\n")

    while True:
        entrada = input("Digite a nota: ").strip()

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("?? Nota inválida. Digite um número entre 0 e 10.")
        except ValueError:
            print("?? Entrada inválida. Digite um número ou 'fim' para encerrar.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\n?? Média da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

# Executa o programa
registrar_notas()