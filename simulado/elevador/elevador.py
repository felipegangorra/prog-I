#Prog1 - UFCG - 16/dezembro/2021
#Aluno: Felipe Gangorra - Matrícula: 121111084
#Calculando capacidade máxima de peso de um elevador

capacidade = int(input())
peso = int(input())

pessoas =  capacidade // peso

print(f'O elevador pode transportar {pessoas} pessoas com segurança.')