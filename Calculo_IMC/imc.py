print("Bem vindo ao seu calculador de IMC!!")

altura = float(input("Digite a altura (m): "))
peso = float(input("Digite o peso (Kg): "))
imc = peso/(altura**2)

print(f"\nValor IMC: {round(imc,2)}")

print("\nDe acordo com o IMC a pessoa está ", end="")
if imc < 18.5:
    print("abaixo do peso ideal.")
elif imc < 24.5:
    print("no peso ideal.")
elif imc < 30:
    print("acima do peso ideal.")
elif imc < 40:
    print("em risco de obesidade.")
else:
    print("em risco de obesidade morbida.")

