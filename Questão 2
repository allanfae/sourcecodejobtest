2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""


while True:
    try:
        inputUser = int(input("Digite um numero:"))
        break
    except ValueError:
        continue

list = []
first = 0
second = 1

for i in range(50 + 1):
    list.append(first)
    fibonacci = first + second
    first = second
    second = fibonacci


if inputUser not in list:
    print(f'O valor {inputUser} não pertence a sequencia de Fibonacci\n')
    print(f'Os primeiros 50 valores da sequencia de fibonacci são respectivamente:\n{list}')

else:
    print(f'O valor {inputUser} pertence a sequencia de Fibonacci\n')
    print(f'Os primeiros 50 valores da sequencia de fibonacci são respectivamente:\n{list}')
