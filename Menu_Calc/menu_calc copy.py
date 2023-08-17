# # Como que printa uma mensagem na tela
# print("Hello world")

name = input('Nome: ')
msg = f'Hello, {name}!!!'
print(msg)


# # Receber dados do usuário e salvar em uma variável
# name = input("\nNome: ")


# # Concatenar strins
# print("Seja bem vindo", name)
# print("Seja bem vindo {}".format(name))
# print(f"Seja bem vindo {name}")


# Somar 2 números
# num1 = float(input("Primeiro número: ")) # num1 = input("Primeiro número: ")
# num2 = float(input("Segundo número: "))
# soma = num1 + num2 

# print(f"A soma dos dois números é: {soma}")

# Somar vários números
# numeros = list()
# soma = 0
# num = input("Digite os números a somar (vázio finaliza e realiza a soma): ")
# numeros.append(num)
# while True:
#     try:
#         num = float(input(" "))
#         numeros.append(num)
#     except Exception as e:
#         break

# for num in numeros:
#     soma = soma + float(num)

# print(f"A soma dos números é: {soma}\n")


num1 = (input('Digite o primeiro número: '))
num2 = input('Digite o segundo número: ')

soma = num1+num2

print(f'A soma de {num1} e {num2} é {soma}')


####################

operator = input('Escolha um operador (+ - * /): ')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if operator == '+':
    result = num1+num2

elif operator == '-':
    result = num1-num2

elif operator == '*':
    result = num1*num2

elif operator == '/':
    result = num1/num2

else:
    print(f'{operator} não é um operador')



print(f'O resultado entre {num1} e {num2} é {result}')

# Condicional para escolher operação
#Sem while True

#Montar função 
def soma_numeros(lista_de_numeros):
    soma = 0
    for num in lista_de_numeros:
        soma = soma + float(num)
    return soma

numeros = list()
num = input("Digite os números a somar (vázio finaliza e realiza a soma): ")
numeros.append(num)
while True:
    try:
        num = float(input(" "))
        numeros.append(num)
    except Exception as e:
        break

print(f"A soma dos números é: {soma_numeros(numeros)}\n")

# while True:
#     selecao = int(input("""
# Qual operação deseja realizar?

# 1- Soma
# 2- Subtração
# 3- Multiplicação
# 4- Divisão
# 5- Sair

# Serviço: """))

#     if selecao == 1: #soma
#         num1 = int(input('Digite o primeiro número: '))
#         num2 = int(input('Digite o segundo número: '))
#         soma = num1 + num2
#         print(f'\nO resultado da soma entre {num1} e {num2} é {soma}!!\n')

#     elif selecao == 2: #subtração
#         num1 = int(input('Digite o primeiro número: '))
#         num2 = int(input('Digite o segundo número: '))
#         sub = num1 - num2
#         print(f'\nO resultado da subtração entre {num1} e {num2} é {sub}!!\n')

#     elif selecao == 3: #multiplicação
#         num1 = int(input('Digite o primeiro número: '))
#         num2 = int(input('Digite o segundo número: '))
#         mult = num1 * num2
#         print(f'\nO resultado da multiplicação entre {num1} e {num2} é {mult}!!\n')

#     elif selecao == 4: #divisão
#         num1 = int(input('Digite o primeiro número: '))
#         num2 = int(input('Digite o segundo número: '))
#         div = num1 / num2
#         print(f'\nO resultado da divisão entre {num1} e {num2} é {div}!!\n')

#     elif selecao == 5: #sair
#         resp = input('Digite "sim" para sair: ')
#         if resp[0] in "sS":
#             print('\nSaindo... Obrigado!!\n')
#             break
#         else:
#             print('\nVoltando...\n')
    

