# criando variavel
temperatura = float(input("Digite a temperatura em celsius: "))

# verificando a condição da temperatura
if temperatura < 10:
    print("Muito frio")
elif temperatura < 20:
    print("Frio")
elif temperatura < 30:
    print("Agradável")
else:
    print("esta muito quente")