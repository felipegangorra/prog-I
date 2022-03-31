#Prog1 - UFCG - 17/FEV/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#Calculando menor palavra dos extremos

#ENTRADA
valores = int(input())
menor = []
lista = []
menor_1 = 0
maior_1 = 0

#CÁLCULO
for x in range(valores):
    valor = input()
    lista.append(valor)

if len(lista[0]) > len(lista[valores - 1]):
    menor.append(lista[valores - 1])

elif len(lista[0]) < len(lista[valores - 1]):
    menor.append(lista[0])
else:
    menor.append(lista[0])
    menor.append(lista[valores - 1])

for valor in lista:
    if len(valor) < len(menor[0]):
        menor_1 += 1
    elif len(valor) > len(menor[0]):
        maior_1 += 1

#SAÍDA
if len(menor) == 2:
    print(f'Menor palavra dos extremos: {menor[0]}, {menor[1]} ({len(menor[0])} letras)')
else:
    print(f'Menor palavra dos extremos: {menor[0]} ({len(menor[0])} letras)')


print(f'{menor_1} palavra(s) com tamanho menor')
print(f'{maior_1} palavra(s) com tamanho maior') 