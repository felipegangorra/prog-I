#Prog1 - UFCG - 22/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#Calculando a qualidade da água de acordo com sua %.

#ENTRADA
peso1 = float(input())
peso2 = float(input())

#CÁLCULO - SAIDA
porcentagem = ((peso1 - peso2) / peso1) * 100
final = peso1 - peso2

#SAIDA
if final < (peso1 * 5 / 100):
    print(f'{porcentagem:.1f}% do peso do produto é de água congelada.\nProduto qualis A.')
elif final < (peso1 * 10 / 100):
    print(f'{porcentagem:.1f}% do peso do produto é de água congelada.\nProduto em conformidade.')
else:
    print(f'{porcentagem:.1f}% do peso do produto é de água congelada.\nProduto não conforme.')
