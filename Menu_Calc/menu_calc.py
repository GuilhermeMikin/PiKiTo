while True:
    selecao = int(input("""
Qual operação deseja realizar?

1- Soma
2- Subtração
3- Multiplicação
4- Divisão
5- Sair

Serviço: """))

    if selecao == 1: #soma
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        soma = num1 + num2
        print(f'\nO resultado da soma entre {num1} e {num2} é {soma}!!\n')

    elif selecao == 2: #subtração
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        sub = num1 - num2
        print(f'\nO resultado da subtração entre {num1} e {num2} é {sub}!!\n')

    elif selecao == 3: #multiplicação
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        mult = num1 * num2
        print(f'\nO resultado da multiplicação entre {num1} e {num2} é {mult}!!\n')

    elif selecao == 4: #divisão
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        div = num1 / num2
        print(f'\nO resultado da divisão entre {num1} e {num2} é {div}!!\n')

    elif selecao == 5: #sair
        resp = input('Digite "sim" para sair: ')
        if resp[0] in "sS":
            print('\nSaindo... Obrigado!!\n')
            break
        else:
            print('\nVoltando...\n')
    

