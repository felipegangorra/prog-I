#Prog1 - 09/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#MULTIPLICA LISTA: multiplicar 

def multiplica_lista(n,lista):
    segunda_lista = []
    if n == 0:
        return segunda_lista

    else:
        for i in range(n):
            for x in lista:
                segunda_lista.append(x)
        return segunda_lista