#Prog1 - UFCG - 02/mar/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#SOMA INTERVALO

def soma_intervalo(a, b):
    soma = 0
    if a == b:
        soma = a
        return soma
    
    elif a < b:
        for i in range((b - a) + 1):
            soma += a
            a += 1
        return soma
