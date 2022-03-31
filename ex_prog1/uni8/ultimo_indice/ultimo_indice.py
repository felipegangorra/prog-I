#Prog1 - 28/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#Ultimo Indice: vendo ultimo num da lista, retorna indice.

def ultimo_indice(num, lista):

    saida = -1
    for i in range(len(lista)):
        if lista[i] == num:
            saida = i
        
    return saida