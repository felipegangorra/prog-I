#Prog1 - 30/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#QUANTIDADE DE USUÁRIOS: retornando quantidade de usuários 


def quantidade_usuarios(cadastro):

    saida = 0
    for chave in cadastro:
        for e in cadastro[chave]:
            if chave != 9999:
                saida += 1

    return saida