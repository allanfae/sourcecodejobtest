3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json
from statistics import mean

file = open('dados.json')
data = json.load(file)


lista = []
z=0
x=0
acimadaMedia=0
for i in data:
    if data[z]['valor'] != 0:
        lista.append(data[z]['valor'])
    z+=1


print(f'O valor minimo encontrado na lista (excluindo os feriados e finais de semana) foi de {round(min(lista))}\n')
print(f'O valor máximo encontrado na lista (excluindo os feriados e finais de semana) foi de {round(max(lista))}\n')
print(f'O valor médio encontrado na lista (excluindo os feriados e finais de semana) foi de {round(mean(lista))}\n')

for i in lista:
    if lista[x] > mean(lista):
        acimadaMedia +=1
    x+=1


print(f'O total de dias do mes acima da média foi de: {acimadaMedia}')
