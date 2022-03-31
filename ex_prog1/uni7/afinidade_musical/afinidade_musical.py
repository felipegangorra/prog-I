#Prog1 - 09/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#AFINIDADE MUSICAL: verificando se tem afinidade 

def tem_afinidade(l1, l2):
    afinidade = 0
    for i in l1:
        if i in l2:
            afinidade += 1

    if afinidade >= 3:
        return True
    else:
        return False