#Prog1 - 20/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#COLAPSA N MENORES: retira N números da lista e add a soma deles ao final.

def menor_numero(lista):
    menor = 0
    for i in lista:
        if menor == 0:
            menor = i
        if i <= menor:
            menor = i
    return menor

def colapsa_n_menores(num, lista):
    cont = 0
    soma = 0
    while cont < num:
        elemento = menor_numero(lista)
        for i in range(len(lista)):
            if lista[i] == elemento:
                soma += lista[i]
                print(soma)
                lista.pop(i) 
                break
        cont += 1

    lista.append(soma)
