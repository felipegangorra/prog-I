#Prog1 - UFCG - 10/fevereiro/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#soma de numeros impares

n1 = int(input())
n2 = int(input())
n3 = int(input())

soma = 0
if (n1 % 2) != 0 and n1 > 0:
    soma += n1
if (n2 % 2) != 0 and n2 > 0:
    soma += n2
if (n3 % 2) != 0 and n3 > 0:
    soma += n3

if soma > 100:
    print('A soma ultrapassou o limite')
else:
    print(soma)