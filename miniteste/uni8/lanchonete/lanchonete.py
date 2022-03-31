#Prog1 - 31/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#LANCHONETE DO ERNANI: 

def organiza_pedido(lista):

    for i in range(len(lista) -1):
        for e in range(len(lista) - 1 - i):
            seguinte = lista[e + 1]
            da_vez = lista[e]


            if da_vez == "s" and seguinte == "p":
                lista[e], lista[e + 1] = lista[e + 1], lista[e]

            if da_vez == "s" and seguinte == "d":
                lista[e], lista[e + 1] = lista[e + 1], lista[e]

            if da_vez == "p" and seguinte == "d":
                lista[e], lista[e + 1] = lista[e + 1], lista[e]

