#Prog1 - UFCG - 22/dezembro/2021
#Aluno: Felipe Gangorra - 121111084 
#Calculando se o recorde de quantidade de comida foi quebrado.

#ENTRADA
atual = float(input())
novo = float(input())

#CÁLCULO - SAIDA
if novo < atual:
    print('recorde mantido')
elif novo > atual:
    print(f'recorde quebrado ({novo} kg)')
else:
    print('recorde empatado')