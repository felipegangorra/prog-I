#Prog1 - UFCG - 24/mar/2022 
#Aluno: Felipe da Silva Gangorra - 121111084    
#REMOVE OCORRENCIAS: removendo elemento x da lista

def remove_ocorrencias(lista, elemento):
    achou = False
    for i in range(len(lista)-1, -1, -1):
        if lista[i] == elemento:
            lista.pop(i)
            achou = True

    if achou == True:
        return elemento
    else:
        return None
    
