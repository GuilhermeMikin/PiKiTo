while True:
    sexo = str(input("Digite o sexo [M/F]: "))
    if sexo in 'MF':
        break
    else: 
        print("Digite M ou F..")

idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))
ativ = str(input("Tipo de atividade: "))

imc = peso/(altura*altura)
if imc < 18.5:
    print("\nAbaixo do peso ideal...")
elif imc < 24.5:
    print("\nPeso ideal...")
elif imc < 30:
    print("\nSobrepeso...")
else:
    print("\nObesidade...")

print(f"Valor IMC: {round(imc,2)}")
