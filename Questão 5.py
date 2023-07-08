5) Escreva um programa que inverta os caracteres de um string.

Importante:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;


string = input("Digite a string que voce deseja reverter:")
storeInvertida = []
tamanhoInput = len(string)

for i in string:
    storeInvertida.append(string[tamanhoInput-1])
    tamanhoInput -= 1

print(''.join(storeInvertida))


