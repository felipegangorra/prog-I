#Prog1 - 28/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#MATRIZ MENOR: retornando matriz com os menores elementos de ambas

def matriz_menor(M1, M2):
    M3 = []
    for i in range(len(M1)):
        linha = []
        for j in range(len(M1[i])):
            if M1[i][j] > M2[i][j]:
                linha.append(M2[i][j])
            else:
                linha.append(M1[i][j])

        M3.append(linha)

    return M3