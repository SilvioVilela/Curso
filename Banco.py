saldo = 0
limite = 500
extrato = ""
n_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input("\nMenu\n\n[D]eposito\n[S]acar\n[E]xtrato\n[Q]Sair\n\nDigite uma opcao: ")

    if opcao == "D":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"\nValor depositado: {valor:.2f}"

        else:

            print("Digite um valor valido")

    elif opcao == "S":

        valor = float(input("Digite o valor a ser sacado: "))

        if valor > saldo:
            print("O valor solicitado excede o saldo!")

        elif n_saque >= LIMITE_SAQUE:
            print("Numero de saques excedido por dia!")

        elif valor > limite:
            print("O valor solicitado excede o limite peritido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"\nValor sacado: {valor:.2f}"
            n_saque += 1

        else:
            print("Operação falhou, valor invalido!")

    elif opcao == "E":

        print("Extrato")
        print("Não houve movimentaçoes!" if not extrato else extrato)
        print("Saldo: {}".format(saldo))
        print("_______")

    elif opcao == "Q":
        break

    else:
        print("Opcao invalida")