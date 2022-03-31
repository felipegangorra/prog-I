#Prog1 - 30/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#DIAGONAIS: retirando diagonais da matriz


def diagonais(matriz):

    matriz_saida = []
    linha1 = []
    linha2 = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:                              
                linha1.append(matriz[i][j])
            
            if i + j == len(matriz) - 1:
                linha2.append(matriz[i][j])

    matriz_saida.append(linha1)
    matriz_saida.append(linha2)

    return matriz_saida