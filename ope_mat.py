# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

numero1 = abs(int(input("Digite o primeiro número inteiro: ")))
numero2 = abs(int(input("Digite o segundo número inteiro: ")))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    resultado = "Operação inválida"

print("Resultado da operação: ", resultado)