# Vamos testar se uma palavra é um palíndromo Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

import difflib

palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")

print(f"Palavra original: {palavra}")
print(f"Palavra invertida: {palavra_invertida}")

# Comparando as diferenças
diferencas = difflib.ndiff(palavra, palavra_invertida)
print('\n'.join(diferencas))
