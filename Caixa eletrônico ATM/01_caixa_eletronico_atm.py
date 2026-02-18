# =============================================================
# PROJETO: SIMULADOR DE CAIXA ELETRÔNICO (ATM)
# Autor: Ricardo Santos
# Objetivo: Estudo de controle de fluxo e estado
# =============================================================

# Inicializamos o saldo fora do loop para que ele não seja resetado
saldo = 0.0

while True:
    # Exibição do Menu de Interação
    print("\n=== BANCO PYTHON INTERATIVO ===")
    print("1 - Ver Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    #Encerra o programa
    if opcao == "4":
        print("Finalizando sessão... Tenha um ótimo dia!")
        break

    #Visualização de Saldo
    if opcao == "1":
        print(f"Saldo disponível: R$ {saldo:.2f}")

    #Entrada de Capital (Depósito)
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        
        # Verificamos se o depósito é um número positivo
        if valor_deposito > 0:
            saldo += valor_deposito # Atualiza o saldo somando o valor
            print(f"Sucesso! R$ {valor_deposito:.2f} adicionados à conta.")
        else:
            print("Operação cancelada: O valor deve ser maior que zero.")

    #Saída de Capital (Saque)
    elif opcao == "3":
        valor_saque = float(input("Digite o valor do saque: R$ "))

        #Impedir saque maior que o saldo
        if valor_saque > saldo:
            print(f"Saldo insuficiente! Você possui apenas R$ {saldo:.2f}")
        
        #Impedir valores negativos ou zero
        elif valor_saque <= 0:
            print("Operação inválida: O valor do saque deve ser positivo.")
        
        #Se passar nas regras, autoriza o saque
        else:
            saldo -= valor_saque # Atualiza o saldo subtraindo o valor
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

    #Tratamento para opções inexistentes no menu
    else:
        print("Opção inválida. Tente novamente.")