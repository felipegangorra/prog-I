#Prog1 - 30/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#BUSCA TODOS: pecorrer matriz buscando elemento


def busca_matriz(matriz, num):
    saida = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == num:
                saida.append((i, j))

    return saida