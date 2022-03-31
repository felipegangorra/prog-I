#Prog1 - 28/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#BUSCA LINEAR: buscando elemento na lista e retornando o indice

def busca(seq, valor):

    saida = -1
    for i in range(len(seq)):
        if seq[i] == valor:
            saida = i
            break

    return saida