# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

resultado = ' '.join([string] * numero)

print("Resultado da multiplicação: ", resultado)