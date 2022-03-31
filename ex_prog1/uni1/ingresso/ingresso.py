#Programação 1 - UFCG - 15/dezembro/2021
#Aluno: Felipe da Silva Gangorra
#Calculando ingressos do cinema com três entradas: adultos, crianças e preço.

adultos = float(input())
crianças = float(input())
ingresso = float(input())

preço = (adultos * ingresso) + (crianças * (ingresso / 2))

print(f'Total: R$ {preço:.2f}')