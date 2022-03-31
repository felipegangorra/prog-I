#Prog1 - 30/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#TOPPL: retirando alunos invalidos 


def meu_in(elemento, seq):
    for e in seq:
        if e == elemento:
            return True
    
    return False


def  filtra_alunos(alunos, inscritos, media):
    invalidos = 0
    for i in range(len(alunos)-1, -1, -1):
        if meu_in(alunos[i][0], inscritos):
            if alunos[i][1] >= media:
                continue
            else:
                alunos.pop(i)
                invalidos += 1
        else:
            alunos.pop(i)
            invalidos += 1
        
    return invalidos