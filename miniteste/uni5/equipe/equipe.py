#Prog1 - UFCG - 24/FEV/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#EQUIPE: determine qual modalidade é cada equipe

cont = 0
while True:
    jogador = input()
    if jogador == '-': break
    cont += 1
    
if cont == 5:
    print('Modalidade -> Basquete')
elif cont == 6:
    print('Modalidade -> Vôlei')
elif cont == 7:
    print('Modalidade -> Handebol')
elif cont == 11:
    print('Modalidade -> Futebol')
else:
    print('Equipe Inválida')