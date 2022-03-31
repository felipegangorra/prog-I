#Prog1 - UFCG - 20/dezembro/2021
#Aluno: Felipe da Siva Gangorra - 121111084
#Calculando o volume em m3 de uma piscina.

#ENTRADA
comprimento = float(input())
largura = float(input())
profundidade = float(input())

#CÁLCULO
m3 = comprimento * largura * profundidade
litros = m3 * 1000

#SAIDA
print(f'A piscina comporta {litros:.2f} litros de água.')