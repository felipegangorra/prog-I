#Programação 1 - UFCG - 14/dezembro/2021
#Aluno: Felipe da Silva Gangorra
#Calculando a área (altura e largura) de uma parede e atribuindo 20 reais a cada metro quadrado.


altura = float(input())
largura = float(input())

area = altura * largura
valor = area * 20

print(f'R$ {valor:.2f}')