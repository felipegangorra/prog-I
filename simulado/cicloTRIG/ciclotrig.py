#Prog1 - 03 - fevereiro - 2022 
#Aluno: Felipe da Silva Gangorra - 121111084
#Calculando ângulo maior ou igual a zero e informando quadrante.

#ENTRADA
angulo = int(input())

#CÁLCULO
if angulo > 360:                #se ele for maior que 360 a contagem passa mais de uma vez!
    angulo = angulo % 360

if 0 < angulo < 90:
    print('Quadrante 1')
elif 90 < angulo < 180:
    print('Quadrante 2')
elif 180 < angulo < 270:
    print('Quadrante 3')
elif 270 < angulo < 360:
    print('Quadrante 4')
else:
    print('Sobre eixos')
