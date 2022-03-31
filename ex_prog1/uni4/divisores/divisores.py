#Prog1 - UFCG - 03/fevereiro/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#Escreva o programa que calcula os divisores próprios de um número inteiro maior do que zero.

#ENTRADA
num = int(input())

#CÁLCULO
for x in range(1, num):        #começa do indice 1 do valor
    if num % x == 0:
        print(x)