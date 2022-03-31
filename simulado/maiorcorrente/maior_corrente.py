#Prog1 - 09/fevereiro/2022 - UFCG
#Aluno: Felipe da Silva Gangorra
#Calcule em qual das variaveis tem a maior corrente eletrica

t1 = int(input())
r1 = int(input())

t2 = int(input())
r2 = int(input())

t3 = int(input())
r3 = int(input())

cond1 = t1 / r1 
cond2 = t2 / r2 
cond3 = t3 / r3 

if cond1 >= cond2 and cond3:
    print('condutor com maior corrente: 1')
    if cond1 < 0.001:
        print(f'maior corrente: {(cond1 * 1000):.2f} µA')
    elif cond1 < 1:
        print(f'maior corrente: {(cond1 * 1000):.2f} mA')
    else:
        print(f'maior corrente: {(cond1 * 1000):.2f} A')

if cond2 >= cond1 and cond3:
    print('condutor com maior corrente: 2')
    if cond2 < 0.001:
        print(f'maior corrente: {(cond2 * 1000):.2f} µA')
    elif cond2 < 1:
        print(f'maior corrente: {(cond2 * 1000):.2f} mA')
    else:
        print(f'maior corrente: {(cond2 * 1000):.2f} A')

if cond3 >= cond1 and cond2:
    print('condutor com maior corrente: 3')
    if cond3 < 0.001:
        print(f'maior corrente: {(cond3 * 1000):.2f} µA')
    elif cond3 < 1:
        print(f'maior corrente: {(cond3 * 1000):.2f} mA')
    else:
        print(f'maior corrente: {(cond3 * 1000):.2f} A')


