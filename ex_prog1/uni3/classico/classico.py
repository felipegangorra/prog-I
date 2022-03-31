#Prog1 - UFCG - 22/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#Calculando vencedor a partir do número de gols.

#ENTRADA
gols1 = int(input())
gols2 = int(input())

#CÁLCULO - SAIDA
if gols1 > gols2:
    print('Campinense')
elif gols1 < gols2:
    print('Treze')
else:
    print('Empate')
