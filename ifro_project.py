total_alunos = 0
aprovados = 0
reprovados = 0

continuar = "s"

while continuar == "s":
    print(f"\n--- Cadastro do aluno {total_alunos + 1} --- ")
    nome = input("Nome do Aluno:")

    while not nome.replace(" ", "").isalpha():
        print("Nome inválido, Digite apenas letras.")
        nome = input("Digite o nome novamente:")

    nota_p = float(input("Nota de Língua Portuguesa:"))
    while nota_p < 0 or nota_p > 10:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        nota_p = float(input("Nota de Língua Portuguesa:"))

    nota_m = float(input("Nota de Matemática:"))
    while nota_m < 0 or nota_m > 10:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        nota_m = float(input("Nota de Matemática:"))

    nota_c = float(input("Nota de Ciências:"))
    while nota_c < 0 or nota_c > 10:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        nota_c = float(input("Nota de Ciências:"))

    nota_h = float(input("Nota de História:"))
    while nota_h < 0 or nota_h > 10:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        nota_h = float(input("Nota de História:"))

    nota_g = float(input("Nota de Geografia:"))
    while nota_g < 0 or nota_g > 10:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        nota_g = float(input("Nota de Geografia:"))

    media = (nota_p + nota_m + nota_c + nota_h + nota_g) / 5
    total_alunos += 1

    print(f"A média do aluno {nome} é: {media:.2f}")

    if media >= 6 and media <= 10:
        print(f"O aluno {nome} foi aprovado.")
        aprovados += 1
    else:
        print(f"O aluno {nome} foi reprovado.")
        reprovados += 1
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()

print(f"\n ---Resultados Finais--- ")
print(f"Total de alunos cadastrados: {total_alunos}")
print(f"Total de alunos aprovados: {aprovados}")
print(f"Total de alunos reprovados: {reprovados}")