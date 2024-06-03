
menu = """
 Selecione uma opção:
 [1] Depositar
 [2] Sacar
 [3] Transferir
 [4] Extrato
 [5] Finalizar Operação

 Opção: """

saldo_A = 0
saldo_B = 0
limite = 500
extrato_A = ""
extrato_B = ""
numero_saques = 0
LIMITE_SAQUES = 3

print(" Olá, Seja bem vindo ao Banco Pobre Coitado.")

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo_A += valor
            extrato_A += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo_A
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo_A -= valor
            extrato_A += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "3":
        conta_origem = input("Informe a conta de origem (A/B): ").upper()
        conta_destino = input("Informe a conta de destino (A/B): ").upper()
        valor = float(input("Informe o valor da transferência: "))

        if conta_origem == conta_destino:
            print("Operação falhou! A conta de origem e destino são iguais.")
        elif valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        else:
            if conta_origem == "A" and conta_destino == "B":
                if valor > saldo_A:
                    print("Operação falhou! Você não tem saldo suficiente na conta A.")
                else:
                    saldo_A -= valor
                    saldo_B += valor
                    extrato_A += f"Transferência para conta B: R$ {valor:.2f}\n"
                    extrato_B += f"Transferência da conta A: R$ {valor:.2f}\n"
                    print("Transferência realizada com sucesso!")
            elif conta_origem == "B" and conta_destino == "A":
                if valor > saldo_B:
                    print("Operação falhou! Você não tem saldo suficiente na conta B.")
                else:
                    saldo_B -= valor
                    saldo_A += valor
                    extrato_B += f"Transferência para conta A: R$ {valor:.2f}\n"
                    extrato_A += f"Transferência da conta B: R$ {valor:.2f}\n"
                    print("Transferência realizada com sucesso!")
            else:
                print("Operação falhou! Conta de origem ou destino inválida.")


    elif opcao == "4":
        print("\n================ EXTRATO ================")
        print("Conta A:")
        print("Não foram realizadas movimentações." if not extrato_A else extrato_A)
        print(f"\nSaldo: R$ {saldo_A:.2f}")
        print("\nConta B:")
        print("Não foram realizadas movimentações." if not extrato_B else extrato_B)
        print(f"\nSaldo: R$ {saldo_B:.2f}")
        print("==========================================")
        

    elif opcao == "5":
        print(" Muito obrigado foi um prazer te atender!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
      