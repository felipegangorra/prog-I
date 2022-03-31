#Prog1 - UFCG - 19/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#Calculando a superfície de um cilindro.
import math

#ENTRADA
print('Cálculo da Superfície de um Cilindro')
print('---')
diametro = float(input('Medida do diâmetro? '))
altura = float(input('Medida da altura? '))

#CÁLCULO
raio = diametro / 2
area = 2 * math.pi * raio * (raio + altura)

#SAIDA
print('---')
print(f'Área calculada: {area:.2f}')