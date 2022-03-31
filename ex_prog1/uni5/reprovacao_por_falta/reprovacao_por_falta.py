#Prog1 - 17/fev/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084    
#REPROVADOS POR FALTA: calculando alunos reprovados por falta.

reprovados = 0
while True:
    aluno = input()
    if aluno == '-': break
    falta = 0
    da_vez = 0

    while da_vez < len(aluno):
        if aluno[da_vez] == 'f':
            falta += 1
        da_vez += 1

        if falta > 8:
            reprovados += 1
            break
    

print(f'{reprovados} aluno(s) reprovado(s) por falta.')