#Prog1 - 17/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 12111084
#DIFERENÇA ENTRE LISTAS: calculando os elementos diferentes entre as listas

def auxiliar(x, y):
    for i in y:
        if i == x:
            return True
    return False


def diferenca_listas(lista1, lista2):
    for i in range(len(lista1)-1, -1 ,-1):
        if auxiliar(lista1[i],lista2):
            lista1.pop(i)

    return lista1
