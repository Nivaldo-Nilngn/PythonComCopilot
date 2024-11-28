# 1 - Concatenando Dados 🐾

## Descrição

Este script em Python recebe duas informações diferentes do usuário e as concatena em uma única string.

## O que aprenderemos?

* Manipulação de Strings (string)
* Concatenação
* Entrada de dados
* Utilização eficiente do Github Copilot

## Como funciona?

1. O script solicita ao usuário que digite duas informações.
2. As informações fornecidas são armazenadas em variáveis.
3. As duas informações são concatenadas em uma única string, separadas por um espaço.
4. A string concatenada é exibida na tela.

## Código

```python
# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

info1 = input("Digite a primeira informação: ")
info2 = input("Digite a segunda informação: ")

info_concatenada = info1 + " " + info2

print("Informações concatenadas: ", info_concatenada)

```

# 2 - Repetindo Textos ✏️

## Descrição

Este script em Python solicita uma string e um número inteiro como entrada do usuário e retorna a string repetida o número de vezes informado.

## O que aprenderemos?

* Manipulação de Strings (string)
* Números Inteiros (int)
* Múltiplas repetições
* Entrada de dados
* Utilização eficiente do Github Copilot

## Como funciona?

1. O script solicita ao usuário que digite uma string.
2. Em seguida, solicita ao usuário que digite um número inteiro.
3. A string fornecida é repetida o número de vezes informado, com cada repetição separada por um espaço.
4. O resultado é exibido na tela.

## Código

```python
# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

resultado = ' '.join([string] * numero)

print("Resultado da multiplicação: ", resultado)

```

# 3 - Operações Matemáticas 🧮

## Descrição

Este script em Python solicita dois números inteiros do usuário e realiza uma operação matemática simples entre eles, conforme a escolha do usuário.

## O que aprenderemos?

* Manipulação de Números Inteiros (int)
* Operações Matemáticas Básicas (+, -, *, /)
* Entrada de dados
* Condicionais (if-elif-else)
* Utilização eficiente do Github Copilot

## Como funciona?

1. O script solicita ao usuário que digite dois números inteiros.
2. Em seguida, solicita ao usuário que escolha uma operação matemática a ser realizada entre os números: adição (+), subtração (-), multiplicação (*) ou divisão (/).
3. O script realiza a operação escolhida e exibe o resultado na tela.
4. Se a operação escolhida for inválida, o script informa que a operação é inválida.

## Código

```python
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

```

# 4 - Verificação de Par ou Ímpar 🔢

## Descrição

Este script em Python solicita um número inteiro do usuário e verifica se ele é par ou ímpar, exibindo a resposta ao usuário.

## O que aprenderemos?

* Manipulação de Números Inteiros (int)
* Operadores Modulares (%)
* Condicionais (if-else)
* Entrada de dados
* Utilização eficiente do Github Copilot

## Como funciona?

1. O script solicita ao usuário que digite um número inteiro.
2. O script verifica se o número é par ou ímpar utilizando o operador modular (%).
3. Se o número for divisível por 2 (resto da divisão igual a 0), ele é par.
4. Caso contrário, o número é ímpar.
5. O resultado é exibido na tela.

## Código

```python
#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar Utilize condicionais para realizar a verificação e exibir a resposta ao usuário.

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

```
# 5 - Cálculo da Média 📊

## Descrição

Este script em Python solicita três notas do usuário e calcula a média aritmética dessas notas.

## O que aprenderemos?

* Manipulação de Números de Ponto Flutuante (float)
* Operadores Aritméticos (+, /)
* Entrada de dados
* Utilização eficiente do Github Copilot

## Como funciona?

1. O script solicita ao usuário que digite três notas.
2. As notas fornecidas são armazenadas como números de ponto flutuante.
3. O script calcula a média aritmética das três notas.
4. A média é exibida na tela.

## Código

```python
#Agora vamos calcular a média de três notas fornecidas na entrada do usuário Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é: {media}")

```

# 6 - Verificação de Palíndromos 🔄

## Descrição

Este script em Python verifica se uma palavra fornecida pelo usuário é um palíndromo, ou seja, se a palavra é igual quando lida de trás para frente.

## O que aprenderemos?

* Manipulação de Strings (string)
* Verificação de Palíndromos
* Entrada de dados
* Utilização do módulo `difflib` para comparação de diferenças
* Utilização eficiente do Github Copilot

## Como funciona?

1. O script solicita ao usuário que digite uma palavra.
2. A palavra fornecida é invertida.
3. O script compara a palavra original com a palavra invertida.
4. Se as palavras forem iguais, a palavra é um palíndromo.
5. Caso contrário, a palavra não é um palíndromo.
6. O script exibe a palavra original, a palavra invertida e as diferenças entre elas.

## Código

```python
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

```
