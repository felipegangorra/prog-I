#Prog1 - 23/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#MAIOR PALAVRA DA FRASE: retornando a maior palavra da frase.

def maior_palavra(frase):

    frase = frase + " "
    frase_lista = []
    palavra = ""
    for i in range(len(frase)):
        if frase[i] != " ":
            palavra += frase[i]

        if frase[i] == " ":
            frase_lista.append(palavra)
            palavra = ""

    maior = ""
    for i in frase_lista:
        if len(i) >= len(maior):
            maior = i

    return maior



