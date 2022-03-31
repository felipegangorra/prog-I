#Prog1 - UFCG - 10/fevereiro/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#calculando media final do aluno

mp = float(input())

if mp >= 7.0:
    print(f'média final: {mp}')
elif mp < 4.0:
    print(f'média final: {mp}')
elif 4.0 <= mp < 7.0:
    mf = float(input())
    nota = (mp * 6 + mf * 4) / 10
    print(f'média final: {nota:.1f}')

