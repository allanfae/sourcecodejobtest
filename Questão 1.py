Pergunta 1 de 3
Observe o trecho de código abaixo:
int INDICE = 13, SOMA = 0, K = 0;
enquanto K < INDICE faça
{
K = K + 1;
SOMA = SOMA + K;
}
imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?"""

A resposta para a pergunta é 91.


Utilizando Python temos:

INDICE  = 13   #Variável global contendo o tamanho do índice(len).
sum = 0        #Variável global que vai armazenar os valores somados durante o loop(WHILE neste caso).
K = 0          #Variável global para ser nosso contador durante o loop.

while K < INDICE: #Condição do loop. Enquanto o valor de k for menor que o valor do índice a condição de execução do loop é válida.
   K = K + 1 #Incremento de 1 no contador K
   sum = sum + K #Esta linha soma o valor total acumulado com o indice atual e armazena.

print(sum) #Simples comando de exibição do resultado da soma(sum)

Obtemos o resultado de 91 no print da variável sum
