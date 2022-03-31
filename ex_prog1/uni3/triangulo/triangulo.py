#Prog1 - UFCG - 22/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#Verificando se o triangulo é valido de acordo com a regra.

#ENTRADA
a = int(input())
b = int(input())
c = int(input())

#CÁLCULO

triangulo = a + b + c

if ((b - c) < a < b + c):
    print(f'triangulo valido. {triangulo}')
elif ((a - c) < b < a + c):
    print(f'triangulo valido. {triangulo}')
elif ((a - b) < c < a + b):
    print(f'triangulo valido. {triangulo}')
else:
    print('triangulo invalido.')
