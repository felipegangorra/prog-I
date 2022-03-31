#Prog1 - UFCG - 16/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#Calculando circunferência de um quadrado.
import math

quadrado = float(input())

raio = (quadrado * (2 ** 0.5)) / 2
perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2

print(f'Perímetro: {perimetro:.5f}')
print(f'Área: {area:.5f}')