#Prog1 - UFCG - 16/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#Calculando total de caixas de morango

morangos = int(input())

caixas = morangos // 400
resto = morangos % 400
perda = (resto * 100) / morangos

print(f'{caixas} caixa(s) completa(s) para embalar os morangos.')
print(f'{perda:.1f}% dos morangos serão perdidos.')