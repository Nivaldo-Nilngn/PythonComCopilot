#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar Utilize condicionais para realizar a verificação e exibir a resposta ao usuário.

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")