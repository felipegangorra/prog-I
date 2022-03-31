#Prog1 - 09/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#comparando posição dos caracteres de duas senhas, se sao iguais

def compara_senhas(senha1, senha2):
    dife = 0

    if len(senha1) < len(senha2):
        senha = len(senha1)
    if len(senha1) > len(senha2):
        senha = len(senha2)
    else:
        senha = len(senha1)

    for i in range(senha):
        if senha1[i] != senha2[i]:
            dife += 1
    
    return dife
