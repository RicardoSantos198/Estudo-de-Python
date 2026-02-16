#======================================================================================================
#CALCULADORA EM PYTHON - MENU INTERATIVO
#Autor: Ricardo Santos
#Descrição: Calculadora simples com menu,
#utilizando loop, condicionais e entrada
#de dados do usúario.
#
#=======================================================================================================

while True:
    #Exibe o menu de operações
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração ")
    print("3 - Multiplicação ")
    print("4 - Divisão ")
    print("5 - Sair ")

    opcao = input("Escolha uma opção:")

    #Encerra o programa
    if opcao == "5":
        print("Encerrando a calculadora...")
        break
    
    #Entrada de dados
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))

    #Processando a operação

    if opcao == "1":
        resultado = num1 + num2

    elif opcao == "2":
        resultado = num1 - num2
    
    elif opcao == "3":
        resultado = num1 * num2

    elif opcao == "4":
        resultado = num1 / num2

    else:
        print("Opção inválida!")

    #Saída
    print(f"Resultado: {resultado}")
