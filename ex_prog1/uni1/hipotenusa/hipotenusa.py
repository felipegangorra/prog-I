#Programação 1 - UFCG - 15/dezembro/2021
#Aluno: Felipe da Silva Gangorra
#Cálculo da Hipotenusa: Escreva um programa que leia os valores dos catetos de um triângulo retângulo e que imprima o valor da sua hipotenusa.

cateto1 = float(input('Cateto 1? '))
cateto2 = float(input('Cateto 2? '))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5

print(f'Hipotenusa: {hipotenusa:.1f}')