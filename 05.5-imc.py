# definindo variaveis
 
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# calculando o imc
imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f"Seu IMC:{imc}")
    print("abaixo do peso")
    print("Tudo ok")
elif imc <= 24.9:
    print(f"Seu IMC:{imc}")
    print("Peso normal")
    print("Tudo ok")
elif imc <= 29.9:
    print(f"Seu IMC:{imc}")
    print("Sobrepeso")
    print("Cuidado com a Saúde")
elif imc <= 34.9:
    print(f"Seu IMC:{imc}")
    print("Obesidade grau 1")
    print("Cuidado com a Saúde")
elif imc <= 39.9:
    print(f"Seu IMC:{imc}")
    print("Obesidade grau 2")
    print("Cuidado com a Saúde")
else:
    print(f"Seu IMC:{imc}")
    print("Obesidade grau 3")
    print("Cuidado com a Saúde")