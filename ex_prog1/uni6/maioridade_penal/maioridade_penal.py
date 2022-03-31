#Prog1 - 09/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#MAIORIDADE PENAL: função que determina quem é maior que 18 anos.

def maioridade_penal(nome, idade):
    nomes = nome.split()    #lista
    idades = idade.split()  #lista

    resultado = ""
    for i in range(len(idades)):
        if int(idades[i]) >= 18 and i < len(idades)-1:
            resultado += nomes[i] + " "
        elif int(idades[i]) >= 18:
            resultado += nomes[i]    
    return resultado