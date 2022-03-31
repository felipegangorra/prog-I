#Prog1 - UFCG - 02/mar/2022
#Aluno: Felipe da Silva Gangorra - 121111084    
#ENCONTRA MENORES: função que diz o menor valor

def encontra_menores(num, lista):
    for i in lista:
        if i < num:
            return i

    else:
        return -1