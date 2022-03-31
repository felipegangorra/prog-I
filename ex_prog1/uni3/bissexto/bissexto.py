#Pro1 - UFCG - 22/dezembro/2021 - 
#Aluno: Felipe Gangorra - 121111084
#Define se um dado ano é bissexto - Um ano é bisssexto se ele for divisível por 400 ou se for divisível por 4 e não por 100

#ENTRADA
ano  = int(input())

#CÁLCULO - SAIDA
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')