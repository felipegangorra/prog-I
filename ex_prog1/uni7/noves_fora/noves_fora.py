#Prog1 - 16/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#NOVES_FORA: utilizando o metodo noves fora em python

def ordem_lista(lista):
    ordem_lista = []
    final = len(lista)

    while len(ordem_lista) < final:
        maior = lista[0]
        remover = 0
        for valor in range(len(lista)):
            if lista[valor] > maior:
                maior = lista[valor]
                remover = valor
        lista.pop(remover)
        ordem_lista.append(maior)
    
    return ordem_lista


#PRINCIPAL
def noves_fora(lista):
    verificandos = [lista]
    veri = 0

    if len(lista) == 1:
        if lista[0] == 9:
            verificandos.append([0])
            return veri, verificandos
        
        else:
            veri = lista[0]
            return veri, verificandos

    while True:
        if len(lista) == 1:
            if lista[0] == 9:
                verificandos.append([0])
                break
            else: 
                break

        nova_lista = []
        for i in range(2, len(lista)):
            nova_lista.append(lista[i])

        veri = (lista[0] + lista[1]) % 9
        lista = [veri] + nova_lista
        lista = ordem_lista(lista)
        verificandos.append(lista) 
    
    return veri, verificandos