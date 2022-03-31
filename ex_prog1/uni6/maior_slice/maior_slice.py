#Prog1 - 20/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#MAIOR SLICE: determinando maior sequencia crescente

def maior_slice(lista):
    sequencia = [lista[0]]
    maior = []
    if len(lista) == 1:
        return lista

    for x in range(1, len(lista)):
        if lista[x - 1] < lista[x]:
            sequencia.append(lista[x])
        if lista[x] <= lista[x - 1]:
            sequencia = [lista[x]]
        if (len(maior) <= len(sequencia)):
            maior = sequencia
        
    return maior