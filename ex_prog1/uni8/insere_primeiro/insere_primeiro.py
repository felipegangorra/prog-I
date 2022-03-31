#Prog1 - 28/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#INSERE PRIMEIRO: ordenando lista

def insere_ordenado_primeiro(lista):

    for i in range(len(lista) - 1):
        if lista[i] >= lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
        else: break